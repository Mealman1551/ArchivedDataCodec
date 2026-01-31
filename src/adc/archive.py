# ADC Archiver 1.4.4 LTS - Archive Module
# This code is licensed under the GNU General Public License v3.0.

"""
Archive creation and extraction functions.
Supports: ADC (custom format with optional encryption) and ZIP.
"""

import os
import zipfile
import getpass
from progress.bar import Bar
from cryptography.fernet import Fernet

from .compression import parma_compress, parma_decompress, read_binary_file
from .crypto import derive_key_from_password
from .constants import ADC_HEADER, SALT_SIZE


def create_adc_archive(file_paths, output_path, format="adc"):
    """
    Creates an archive from given files.
    
    Args:
        file_paths: List of file paths to include
        output_path: Path where the archive should be created
        format: Archive format (adc or zip)
    """
    # Handle ZIP format
    if format == "zip":
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            with Bar("Compressing files...", max=len(file_paths)) as bar:
                for file_path in file_paths:
                    zf.write(file_path, arcname=os.path.basename(file_path))
                    bar.next()
        print(f"ZIP archive created: {output_path}")
        return

    # Handle ADC format with optional encryption
    use_password = (
        input("Do you want to protect this archive with a password? (y/n): ")
        .strip()
        .lower()
        == "y"
    )
    if use_password:
        pwd = getpass.getpass("Create a password for this archive: ")
        salt = os.urandom(SALT_SIZE)
        key = derive_key_from_password(pwd, salt)
        fernet = Fernet(key)

    with open(output_path, "wb") as archive_file:
        if use_password:
            archive_file.write(ADC_HEADER)
            archive_file.write(salt)

        with Bar("Compressing files...", max=len(file_paths)) as bar:
            for file_path in file_paths:
                filename = os.path.basename(file_path).encode("utf-8")
                original_data = read_binary_file(file_path)
                compressed_data = parma_compress(original_data)

                if use_password:
                    data_to_write = fernet.encrypt(compressed_data)
                else:
                    data_to_write = compressed_data

                archive_file.write(len(filename).to_bytes(2, "big"))
                archive_file.write(filename)
                archive_file.write(len(data_to_write).to_bytes(8, "big"))
                archive_file.write(data_to_write)
                bar.next()
    print(f"Archive created: {output_path}")


def extract_adc_archive(archive_path, output_dir, format=None):
    """
    Extracts files from an archive.
    
    Args:
        archive_path: Path to the archive file
        output_dir: Directory where files should be extracted
        format: Archive format (auto-detected if None)
    """
    base_name = os.path.splitext(os.path.basename(archive_path))[0]
    dest_dir = os.path.join(output_dir, base_name)
    os.makedirs(dest_dir, exist_ok=True)

    # Auto-detect format if not specified
    if not format:
        format = "zip" if archive_path.lower().endswith(".zip") else "adc"

    # Handle ZIP format
    if format == "zip":
        with zipfile.ZipFile(archive_path, "r") as zf:
            file_list = zf.namelist()
            with Bar("Extracting files...", max=len(file_list)) as bar:
                for f in file_list:
                    zf.extract(f, path=dest_dir)
                    bar.next()
        print(f"ZIP archive extracted to: {dest_dir}")
        return

    # Handle ADC format with optional decryption
    with open(archive_path, "rb") as archive_file:
        header = archive_file.read(8)
        if header == ADC_HEADER:
            salt = archive_file.read(SALT_SIZE)
            pwd = getpass.getpass("Enter password for archive: ")
            key = derive_key_from_password(pwd, salt)
            fernet = Fernet(key)
            encrypted = True
        else:
            archive_file.seek(0)
            encrypted = False

        file_count = 0
        files_to_extract = []

        # Read all files from archive
        while True:
            filename_len_bytes = archive_file.read(2)
            if not filename_len_bytes:
                break
            filename_len = int.from_bytes(filename_len_bytes, "big")
            filename = archive_file.read(filename_len).decode("utf-8", errors="ignore")
            data_len_bytes = archive_file.read(8)
            data_len = int.from_bytes(data_len_bytes, "big")
            data = archive_file.read(data_len)

            try:
                if encrypted:
                    data = fernet.decrypt(data)
                files_to_extract.append((filename, data))
                file_count += 1
            except Exception as e:
                print(f"Error decrypting {filename}: {e}")
                continue

        # Extract all files
        with Bar("Extracting files...", max=file_count) as bar:
            for filename, compressed_data in files_to_extract:
                decompressed_data = parma_decompress(compressed_data)
                if decompressed_data is not None:
                    output_path = os.path.join(dest_dir, filename)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as output_file:
                        output_file.write(decompressed_data)
                else:
                    print(f"Error decompressing {filename}")
                bar.next()
        print(f"Extraction complete to {dest_dir}")
