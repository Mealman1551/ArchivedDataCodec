# libadc - Compression Module
# (c) 2026 Mealman1551


import zlib
from functools import lru_cache
import os


def _normalize_path(path):
    return os.path.normcase(os.path.abspath(path))


@lru_cache(maxsize=256)
def parma_compress(data):
    return zlib.compress(data)


@lru_cache(maxsize=256)
def parma_decompress(compressed_data):
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompress error: {e}")
        return None


@lru_cache(maxsize=128)
def _read_binary_with_stat(file_path, mtime, size):
    with open(file_path, "rb") as file:
        return file.read()


def read_binary_file(file_path):
    normalized_path = _normalize_path(file_path)
    stat = os.stat(normalized_path)
    return _read_binary_with_stat(normalized_path, stat.st_mtime, stat.st_size)


def clear_compression_cache():
    parma_compress.cache_clear()
    parma_decompress.cache_clear()
    _read_binary_with_stat.cache_clear()
