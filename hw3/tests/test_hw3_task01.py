from hw3.hw3_task01 import cache_factory


def test_with_number():
    @cache_factory(times=3)
    def func(a, b):
        return (a ** b) ** 2

    val_1 = func(5)
    val_2 = func(5)
    val_3 = func(5)
    assert val_1 == val_2 == val_3
