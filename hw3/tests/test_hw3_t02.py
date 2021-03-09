import time

from hw3.hw3_t02 import slow_calc_500_numbers


def test_slow_calc_500_numbers():
    start_time = time.time()
    slow_calc_500_numbers()
    finish_time = time.time()
    assert finish_time - start_time < 60
