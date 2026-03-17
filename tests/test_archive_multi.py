from adc.archive import create_adc_archive, extract_adc_archive
from pathlib import Path

def test_multiple_files(tmp_path, monkeypatch):
    files = []
    for i in range(3):
        f = tmp_path / f"file{i}.txt"
        f.write_bytes(f"Content {i}".encode())
        files.append(str(f))

    archive_path = tmp_path / "multi.adc"

    monkeypatch.setattr("builtins.input", lambda _: "n")

    create_adc_archive(files, str(archive_path), format="adc")
    assert archive_path.exists()

    output_dir = tmp_path / "out"
    output_dir.mkdir()

    extracted_folder = output_dir / "multi"

    extract_adc_archive(str(archive_path), str(output_dir))

    for i in range(3):
        extracted_file = extracted_folder / f"file{i}.txt"
        assert extracted_file.exists()
        assert extracted_file.read_bytes() == f"Content {i}".encode()