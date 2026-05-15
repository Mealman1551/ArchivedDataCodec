# ADC Archiver - Compression Module
# (c) 2026 Mealman1551


import zlib
from functools import lru_cache
import os


@lru_cache(maxsize=256)
def parma_compress(data):
    """
    Compress data using zlib with caching.
    
    Args:
        data: Bytes to compress
        
    Returns:
        Compressed bytes
    """
    return zlib.compress(data)


@lru_cache(maxsize=256)
def parma_decompress(compressed_data):
    """
    Decompress data using zlib with caching.
    
    Args:
        compressed_data: Compressed bytes
        
    Returns:
        Decompressed bytes, or None if decompression fails
    """
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompress error: {e}")
        return None


@lru_cache(maxsize=128)
def _read_binary_with_mtime(file_path, mtime):
    """
    Internal helper that reads file contents with modification time cache key.
    
    Args:
        file_path: Path to the file
        mtime: File modification time (used as cache key)
        
    Returns:
        File contents as bytes
    """
    with open(file_path, "rb") as file:
        return file.read()


def read_binary_file(file_path):
    """
    Read binary file contents with intelligent caching based on modification time.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File contents as bytes
    """
    mtime = os.path.getmtime(file_path)
    return _read_binary_with_mtime(file_path, mtime)
