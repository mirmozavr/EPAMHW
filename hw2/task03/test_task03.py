import os
import sys

import pytest
from task03 import combinations

sys.path.append(os.path.dirname(os.path.dirname(__file__)))


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        (([1, 2], [3, 4]), [(1, 3), (1, 4), (2, 3), (2, 4)]),
        (([1], [3]), [(1, 3)]),
        (([5, 9], [9, 5]), [(5, 9), (5, 5), (9, 9), (9, 5)]),
        (([0, 0], [0, 0]), [(0, 0), (0, 0), (0, 0), (0, 0)]),
    ],
)
def test_check_fib(value: list, expected_result: bool):
    actual_result = combinations(*value)

    assert actual_result == expected_result
