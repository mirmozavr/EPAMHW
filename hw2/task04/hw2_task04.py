"""Write a function that accepts another function as an argument.

Then it should return such a function, so the every call to initial one
should be cached.

def function(a, b):
    return (a ** b) ** 2

cache_func = cache(function)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2
"""
from typing import Any, Callable


def function(a: int, b: int) -> int:
    return (a ** b) ** 2


def calc_sum(a: int, b: int) -> int:
    return a + b


def cache(func: Callable) -> Callable:
    f_cache = {}

    def wrapper(*args: Any) -> Any:
        print(args)
        if isinstance(args, list):
            args = tuple(*args)
        if args in f_cache:
            return f_cache[args]

        f_cache[args] = func(*args)
        return f_cache[args]

    return wrapper


cache_function = cache(function)
val_1 = cache_function(*[100, 200])
val_2 = cache_function(*[100, 200])
assert val_1 is val_2


some = 100, 200
cache_calc_sum = cache(calc_sum)
val_3 = cache_calc_sum(*[1, 2])
val_4 = cache_calc_sum(*[1, 2])
assert val_3 is val_4


cache_sum = cache(sum)
v1 = cache_sum([100, 200])
v2 = cache_sum([100, 200])
v3 = cache_sum([100, 200])
assert v1 is v2 is v3


cache_sum = cache(sum)
v5 = cache_sum([30, 50, 10, 40])
v6 = cache_sum([30, 50, 10, 40])
assert v5 is v6
