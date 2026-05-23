import os

from libadc.archive import create_adc_archive, extract_adc_archive, _list_files_in_path
from libadc.compression import read_binary_file

def test_create_and_extract(tmp_path, monkeypatch):
    file_path = tmp_path / "hello.txt"
    file_path.write_bytes(b"Hello ADC!")

    archive_path = tmp_path / "test.adc"

    monkeypatch.setattr("builtins.input", lambda _: "n")

    create_adc_archive([str(file_path)], str(archive_path), format="adc")
    assert archive_path.exists()

    output_dir = tmp_path / "extract"
    output_dir.mkdir()
    extract_adc_archive(str(archive_path), str(output_dir))

    extracted_file = output_dir.joinpath("test").joinpath("hello.txt")
    assert extracted_file.read_bytes() == b"Hello ADC!"


def test_read_binary_file_refreshes_after_write(tmp_path):
    file_path = tmp_path / "data.bin"
    file_path.write_bytes(b"first")

    first_bytes = read_binary_file(str(file_path))
    assert first_bytes == b"first"

    file_path.write_bytes(b"second")
    os.utime(str(file_path), None)

    second_bytes = read_binary_file(str(file_path))
    assert second_bytes == b"second"
    assert first_bytes != second_bytes


def test_list_files_in_path_cache_updates_on_directory_change(tmp_path):
    dir_path = tmp_path / "folder"
    dir_path.mkdir()
    file_a = dir_path / "a.txt"
    file_a.write_text("A")

    first_listing = _list_files_in_path(str(dir_path))
    assert len(first_listing) == 1

    file_b = dir_path / "b.txt"
    file_b.write_text("B")
    os.utime(str(dir_path), None)

    second_listing = _list_files_in_path(str(dir_path))
    assert len(second_listing) == 2
    normalized_b = os.path.normcase(str(file_b))
    assert any(normalized_b == os.path.normcase(item) for item in second_listing)
