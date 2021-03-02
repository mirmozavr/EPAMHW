import pytest
from task02 import check_fib

true_fib_seq = [
    0,
    1,
    1,
    2,
    3,
    5,
    8,
    13,
    21,
    34,
    55,
    89,
    144,
    233,
    377,
    610,
    987,
    1597,
    2584,
    4181,
    6765,
]


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (true_fib_seq, True),
        ([0], True),
        ([0, 1], True),
        ([0, 0], False),
        ([0, -1], False),
        ([0, 1, 1, 2, 3, 5, 8], True),
        ([], False),
        ([-5, 0, 1, 1, 2], False),
        ([1, 1, 2], False),
    ],
)
def test_check_fib(value: list, expected_result: bool):
    actual_result = check_fib(value)

    assert actual_result == expected_result
