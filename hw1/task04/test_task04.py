import pytest
from task04 import check_sum_of_four

all_zero_x5 = [0] * 5
empty = []
max_length = list(range(1000))


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((all_zero_x5, all_zero_x5, all_zero_x5, all_zero_x5), 625),
        ((empty, empty, empty, empty), 0),
        ((max_length, max_length, max_length, max_length), 1),
        (([1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [-3, -12, 0, 0]), 2),
        (([-1], [-1], [-1], [-1]), 0),
        (([-1], [-1], [-1], [3]), 1),
    ],
)
def test_check_sum_of_four(value, expected_result: int):
    actual_result = check_sum_of_four(*value)

    assert actual_result == expected_result
