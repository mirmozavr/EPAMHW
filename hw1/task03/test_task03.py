import os

import pytest
from task03 import find_maximum_and_minimum

script_dir = os.path.dirname(__file__)


@pytest.mark.parametrize(
    ("data", "expected_result"),
    [
        (script_dir + "/test_data/test_data1.txt", (-20, 14)),
        (script_dir + "/test_data/test_data2.txt", (0, 0)),
        (script_dir + "/test_data/test_data3.txt", (-2, 5000)),
        (script_dir + "/test_data/test_data4.txt", (42, 42)),
        (script_dir + "/test_data/test_data5.txt", (-656, -4)),
        (script_dir + "/test_data/test_data6.txt", (-9, 5)),
    ],
)
def test_find_maximum_and_minimum(data, expected_result: tuple):
    actual_result = find_maximum_and_minimum(data)

    assert actual_result == expected_result
