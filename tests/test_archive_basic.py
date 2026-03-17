from adc.archive import create_adc_archive, extract_adc_archive

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