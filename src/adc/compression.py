# ADC Archiver 1.4.4 LTS - Compression Module
# This code is licensed under the GNU General Public License v3.0.

"""
Compression and decompression functions using zlib.
"""

import zlib


def parma_compress(data):
    """
    Compresses binary data using zlib compression.
    
    Args:
        data: Binary data to compress
        
    Returns:
        Compressed binary data
    """
    return zlib.compress(data)


def parma_decompress(compressed_data):
    """
    Decompresses zlib-compressed binary data.
    
    Args:
        compressed_data: Compressed binary data
        
    Returns:
        Decompressed binary data, or None if decompression fails
    """
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompress error: {e}")
        return None


def read_binary_file(file_path):
    """
    Reads a file in binary mode.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        Binary content of the file
    """
    with open(file_path, "rb") as file:
        return file.read()
