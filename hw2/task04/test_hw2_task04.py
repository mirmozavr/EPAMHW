from hw2_task04 import cache, calc_sum, function

some = 100, 200
cache_function = cache(function)
val_1 = cache_function(*some)
val_2 = cache_function(*some)


def test_func():
    assert val_1 is val_2


cache_calc_sum = cache(calc_sum)
val_3 = cache_calc_sum(*some)
val_4 = cache_calc_sum(*some)


def test_calc_sum():
    assert val_3 is val_4


cache_sum = cache(sum)
v5 = cache_sum(*[100, 200])
v6 = cache_sum(*[100, 200])


def test_sum():
    assert v5 is v6
