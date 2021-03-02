import os

import pytest
from task05 import find_maximal_subarray_sum

script_dir = os.path.dirname(__file__)


@pytest.mark.parametrize(
    ("data", "length", "expected_result"),
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([], 4, 0),
        ([1], 2, 1),
        ([-1, -2, -3, -4], 2, 0),
        ([1, -2, -3, -4], 3, 1),
        ([1, 3, -1, -3, 5, 3, 6, 7], 0, 0),
    ],
)
def test_find_maximum_and_minimum(data: list, length: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(data, length)

    assert actual_result == expected_result
