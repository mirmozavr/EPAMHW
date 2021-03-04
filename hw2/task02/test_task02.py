import pytest
from task02 import major_and_minor_elem


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ([2, 3, 2, 5, 2, 2, 3, 2, 4, 5, 2, 9], (2, 9)),
        ([5, 5, 0], (5, 0)),
        ([1, 1, -99, 1, 5, 5, 1, 6, 1, 6, 1, 4, 4, 1, 1], (1, -99)),
        ([88, 88, 88, 88, 88, 88, 55, 88], (88, 55)),
        ([-1, 0, -1], (-1, 0)),
    ],
)
def test_check_fib(value: list, expected_result: bool):
    actual_result = major_and_minor_elem(value)

    assert actual_result == expected_result
