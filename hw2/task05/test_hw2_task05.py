import string

from hw2_task05 import custom_range


def test_custom_range():
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
    assert custom_range(string.digits, "9", "0", -1) == [
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
        "1",
    ]
    assert custom_range(string.ascii_uppercase, "Z", "A", -3) == [
        "Z",
        "W",
        "T",
        "Q",
        "N",
        "K",
        "H",
        "E",
        "B",
    ]

    assert custom_range([1, 2, 3, 4, 5, 6, 7, 8], 2, 7, 2) == [2, 4, 6]
