from hw2_task04 import cache


def function(a: int, b: int) -> int:
    return (a ** b) ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def test_func():
    cache_function = cache(function)
    val_1 = cache_function(*(100, 200))
    val_2 = cache_function(*(100, 200))
    assert val_1 is val_2


def test_custom_sum_function():
    cache_calc_sum = cache(calc_sum)
    val_3 = cache_calc_sum(*(22, 44))
    val_4 = cache_calc_sum(*(22, 44))
    assert val_3 is val_4


def test_sum_list_2_numbers():
    cache_sum = cache(sum)
    v1 = cache_sum([100, 200])
    v2 = cache_sum([100, 200])
    v3 = cache_sum([100, 200])
    assert v1 is v2 is v3


def test_sum_list_4_numbers():
    cache_sum = cache(sum)
    v5 = cache_sum([30, 50, 10, -40])
    v6 = cache_sum([30, 50, 10, -40])
    assert v5 is v6


def test_sum_list_1_number():
    cache_sum = cache(sum)
    v5 = cache_sum([3])
    v6 = cache_sum([3])
    assert v5 is v6
