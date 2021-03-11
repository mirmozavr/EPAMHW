from hw3.hw3_t02 import slow_calc_500_numbers


def test_slow_calc_500_numbers():
    assert sum(slow_calc_500_numbers()) == 1025932
