# ADC Archiver 1.4.5 LTS - Compression Module
# This code is licensed under the GNU General Public License v3.0.

"""
Compression and decompression functions using zlib.
"""

import zlib


def parma_compress(data):

    return zlib.compress(data)


def parma_decompress(compressed_data):
    
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompress error: {e}")
        return None


def read_binary_file(file_path):

    with open(file_path, "rb") as file:
        return file.read()
