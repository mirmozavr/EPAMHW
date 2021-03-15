from hw4.hw4_t05 import fizzbuzz


def test_5_fizzbuzz_numbers():
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]


def test_20_fizzbuzz_numbers():
    assert list(fizzbuzz(16)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
        "16",
    ]


def test_0_fizzbuzz_numbers():
    assert list(fizzbuzz(0)) == []


def test_negative_fizzbuzz_numbers():
    assert list(fizzbuzz(-10)) == []
