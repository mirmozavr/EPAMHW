import os

import pytest
from task01 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)

script_dir = os.path.dirname(__file__)


@pytest.mark.parametrize(
    ("path", "expected_result"),
    [
        (
            (script_dir + "/test.txt"),
            [
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
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path: str, expected_result: list):
    actual_result = get_longest_diverse_words(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("path", "expected_result"),
    [
        (
            (script_dir + "/test.txt"),
            "ä",
        )
    ],
)
def test_get_rarest_char(path: str, expected_result: str):
    actual_result = get_rarest_char(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("path", "expected_result"),
    [
        (
            (script_dir + "/test.txt"),
            36,
        )
    ],
)
def test_count_punctuation_chars(path: str, expected_result: int):
    actual_result = count_punctuation_chars(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("path", "expected_result"),
    [
        (
            (script_dir + "/test.txt"),
            0,
        )
    ],
)
def test_count_non_ascii_chars(path: str, expected_result: int):
    actual_result = count_non_ascii_chars(path)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ("path", "expected_result"),
    [
        (
            (script_dir + "/test.txt"),
            "",
        )
    ],
)
def test_get_most_common_non_ascii_char(path: str, expected_result: str):
    actual_result = get_most_common_non_ascii_char(path)
    assert actual_result == expected_result
