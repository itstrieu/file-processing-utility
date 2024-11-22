import pytest
from src.file_handler import load_file


def test_load_file():
    # Test with a valid file
    df = load_file("data/sample.csv")
    assert not df.empty

    # Test with a non-existent file
    with pytest.raises(FileNotFoundError):
        load_file("data/non_existent.csv")
