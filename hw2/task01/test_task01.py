import os

from task01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

script_dir = os.path.dirname(__file__)


def test_get_longest_diverse_words():
    assert get_longest_diverse_words(script_dir + "/test.txt") == [
        ["anotherverylongword", 13],
        ["oneshorterword", 9],
        ["disapproves", 9],
        ["gentleman's", 9],
        ["Slingsby's", 9],
        ["reluctantly", 9],
        ["prosecute", 8],
        ["Slingsby", 8],
        ["Slingsby", 8],
        ["Slingsby", 8],
    ]


def test_get_rarest_char():
    assert get_rarest_char(script_dir + "/test.txt") == "ä"


def test_count_punctuation_chars():
    assert count_punctuation_chars(script_dir + "/test.txt") == 36


def test_count_non_ascii_chars():
    assert count_non_ascii_chars(script_dir + "/test.txt") == 19


def test_get_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(script_dir + "/test.txt") == "ã"
