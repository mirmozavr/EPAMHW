import os

from hw9.hw9_t03 import universal_file_counter

base_dir = os.path.dirname(__file__)


def test_count_lines_in_txt():
    assert universal_file_counter(base_dir, "txt") == 7


def test_count_words_in_txt():
    assert universal_file_counter(base_dir, "txt", str.split) == 17


def test_count_lines_in_py():
    assert universal_file_counter(base_dir, "py") == 25


def test_count_words_in_rst():
    assert universal_file_counter(base_dir, "rst", str.split) == 7


def test_count_lines_in_jpg():
    assert universal_file_counter(base_dir, "jpg") == 0
