import pytest

from hw4.hw4_t01 import read_magic_number


def test_valid_number_1_in_1st_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """1
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is True


def test_valid_number_2_in_1st_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """2
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is True


def test_not_valid_number_3_in_1st_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """3
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is False


def test_not_valid_number_45_in_1st_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """45
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is False


def test_not_valid_no_number_in_any_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """no number at all
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is False


def test_not_valid_number_1_in_2nd_line(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    file = directory / "test_data.txt"
    file.write_text(
        """number is in second line
1
some text
another text
some more text lines
"""
    )
    assert read_magic_number(directory / "test_data.txt") is False


def test_file_doesnt_exist_value_error(tmp_path):
    directory = tmp_path / "sub_directory"
    directory.mkdir()
    with pytest.raises(ValueError):  # noqa: PT011
        read_magic_number(directory / "missing_file.txt")
