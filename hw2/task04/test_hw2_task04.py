from hw2_task04 import cache, function

cache_func = cache(function)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)


def test_func():
    assert val_1 is val_2
