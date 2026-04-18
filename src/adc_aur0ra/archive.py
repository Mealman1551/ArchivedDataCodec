# ADC Archiver Aurora Archive Module
# (c) 2026 Mealman1551


import os
import zipfile
import tarfile
import py7zr
import getpass
from progress.bar import Bar
from cryptography.fernet import Fernet

from .compression import parma_compress, parma_decompress, read_binary_file

_list_cache = {}
from .crypto import derive_key_from_password
from .constants import ADC_HEADER, SALT_SIZE


def _list_files_in_path(path):
    if os.path.isdir(path):
        mtime = os.path.getmtime(path)
        cache_key = (path, mtime)
        if cache_key in _list_cache:
            return _list_cache[cache_key]

        files = []
        for root_dir, dirs, file_names in os.walk(path):
            for f in file_names:
                files.append(os.path.join(root_dir, f))
        _list_cache[cache_key] = files
        return files
    else:
        return [path]


def create_adc_archive(file_paths, output_path, format="adc"):
    all_files = []
    for path in file_paths:
        all_files.extend(_list_files_in_path(path))
    if format.startswith("tar"):
        mode = "w"
        if output_path.endswith(".tar.gz"):
            mode = "w:gz"
        elif output_path.endswith(".tar.xz"):
            mode = "w:xz"
        elif output_path.endswith(".tar.bz2"):
            mode = "w:bz2"

        with tarfile.open(output_path, mode) as tar:
            with Bar("Compressing files...", max=len(all_files)) as bar:
                for file_path in all_files:
                    tar.add(
                        file_path,
                        arcname=os.path.relpath(
                            file_path, os.path.dirname(file_paths[0])
                        ),
                    )
                    bar.next()
        print(f"TAR archive created: {output_path}")
        return

    if format == "zip":
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            with Bar("Compressing files...", max=len(all_files)) as bar:
                for file_path in all_files:
                    zf.write(
                        file_path,
                        arcname=os.path.relpath(
                            file_path, os.path.dirname(file_paths[0])
                        ),
                    )
                    bar.next()
        print(f"ZIP archive created: {output_path}")
        return

    if format == "7z":
        with py7zr.SevenZipFile(output_path, "w") as archive:
            with Bar("Compressing files...", max=len(all_files)) as bar:
                for file_path in all_files:
                    if os.path.isdir(file_path):
                        bar.next()
                        continue
                    arcname = os.path.relpath(file_path, os.path.dirname(file_paths[0]))
                    archive.write(file_path, arcname)
                    bar.next()
        print(f"7z archive created: {output_path}")
        return

    use_password = input(
        "Do you want to protect this archive with a password? (y/n): "
    ).strip().lower() in ("y", "yes")
    if use_password:
        pwd = getpass.getpass("Create a password for this archive: ")
        salt = os.urandom(SALT_SIZE)
        key = derive_key_from_password(pwd, salt)
        fernet = Fernet(key)

    with open(output_path, "wb") as archive_file:
        if use_password:
            archive_file.write(ADC_HEADER)
            archive_file.write(salt)

        with Bar("Compressing files...", max=len(all_files)) as bar:
            for file_path in all_files:
                if os.path.isdir(file_path):
                    bar.next()
                    continue

                filename = os.path.relpath(
                    file_path, os.path.dirname(file_paths[0])
                ).encode("utf-8")
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
    print(f"ADC archive created: {output_path}")


def extract_adc_archive(archive_path, output_dir, format=None):
    if not format:
        if archive_path.lower().endswith((".tar", ".tar.gz", ".tar.xz", ".tar.bz2")):
            format = "tar"
        elif archive_path.lower().endswith(".7z"):
            format = "7z"
        elif archive_path.lower().endswith(".zip"):
            format = "zip"
        else:
            format = "adc"

    base_name = os.path.splitext(os.path.basename(archive_path))[0]
    dest_dir = os.path.join(output_dir, base_name)
    os.makedirs(dest_dir, exist_ok=True)

    if format == "tar":
        with tarfile.open(archive_path, "r:*") as tar:
            members = tar.getmembers()
            with Bar("Extracting files...", max=len(members)) as bar:
                for member in members:
                    tar.extract(member, path=output_dir)
                    bar.next()
        print(f"TAR archive extracted to: {output_dir}")
        return

    if format == "zip":
        with zipfile.ZipFile(archive_path, "r") as zf:
            file_list = zf.namelist()
            with Bar("Extracting files...", max=len(file_list)) as bar:
                for f in file_list:
                    zf.extract(f, path=output_dir)
                    bar.next()
        print(f"ZIP archive extracted to: {output_dir}")
        return

    if format == "7z":
        with py7zr.SevenZipFile(archive_path, "r") as archive:
            try:
                allnames = archive.getnames()
            except Exception:
                allnames = []
            with Bar(
                "Extracting files...", max=len(allnames) if allnames else 1
            ) as bar:
                archive.extractall(path=output_dir)
                for _ in allnames or [None]:
                    bar.next()
        print(f"7z archive extracted to: {output_dir}")
        return

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
        print(f"ADC archive extracted to {dest_dir}")
