# ADC Archiver Aurora Compression Module
# (c) 2026 Mealman1551

import zlib
from functools import lru_cache
import os


# Use simple in-memory caches to avoid recomputing compression or reading
# the same data repeatedly within a single run.  The caches are keyed by
# immutable inputs (file path + mtime for file reads, raw bytes for
# compression) so that changes to files automatically invalidate the cache.

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


# internal helper that includes mtime in the cache key
@lru_cache(maxsize=128)
def _read_binary_with_mtime(file_path, mtime):
    with open(file_path, "rb") as file:
        return file.read()


def read_binary_file(file_path):
    mtime = os.path.getmtime(file_path)
    return _read_binary_with_mtime(file_path, mtime)
