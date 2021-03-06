from hw2_task04 import cache, calc_sum, function

cache_function = cache(function)
cache_calc_sum = cache(calc_sum)

some = 100, 200
val_1 = cache_function(*some)
val_2 = cache_function(*some)

val_3 = cache_calc_sum(*some)
val_4 = cache_calc_sum(*some)


def test_func():
    assert val_1 is val_2


def test_calc_sum():
    assert val_3 is val_4
