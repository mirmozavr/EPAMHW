import os

import pytest

from hw4.hw4_t01 import read_magic_number


def test_valid_1():
    assert read_magic_number(os.path.dirname(__file__) + "/data1.txt") is True


def test_valid_2():
    assert read_magic_number(os.path.dirname(__file__) + "/data2.txt") is True


def test_not_valid_3():
    assert read_magic_number(os.path.dirname(__file__) + "/data3.txt") is False


def test_not_valid_45():
    assert read_magic_number(os.path.dirname(__file__) + "/data4.txt") is False


def test_not_valid_no_number():
    assert read_magic_number(os.path.dirname(__file__) + "/data5.txt") is False


def test_not_valid_no_number_in_1st_line():
    assert read_magic_number(os.path.dirname(__file__) + "/data6.txt") is False


def test_not_valid_mixed_line():
    assert read_magic_number(os.path.dirname(__file__) + "/data7.txt") is False


def test_file_doesnt_exist_value_error():
    with pytest.raises(ValueError, match="Error text"):
        read_magic_number(os.path.dirname(__file__) + "/doesnt_exist.txt")
