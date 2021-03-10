from hw2_task04 import cache, calc_sum, function


def test_func():
    cache_function = cache(function)
    val_1 = cache_function(*[100, 200])
    val_2 = cache_function(*[100, 200])
    assert val_1 is val_2


def test_calc_sum():
    some = 100, 200
    cache_calc_sum = cache(calc_sum)
    val_3 = cache_calc_sum([100, 200])
    val_4 = cache_calc_sum([100, 200])
    assert val_3 is val_4


def test_sum_1():
    cache_sum = cache(sum)
    v1 = cache_sum([100, 200])
    v2 = cache_sum([100, 200])
    v3 = cache_sum([100, 200])
    assert v1 is v2 is v3


def test_sum_2():
    cache_sum = cache(sum)
    v5 = cache_sum([30, 50, 10, 40])
    v6 = cache_sum([30, 50, 10, 40])
    assert v5 is v6
