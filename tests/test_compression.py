from adc.compression import parma_compress, parma_decompress

def test_compression_roundtrip():
    data = b"example data"
    compressed = parma_compress(data)
    decompressed = parma_decompress(compressed)
    assert decompressed == data

def test_decompress_invalid():
    bad_data = b"not zlib"
    result = parma_decompress(bad_data)
    assert result is None