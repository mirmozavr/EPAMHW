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
from typing import Callable


def function(a: int, b: int) -> int:
    return (a ** b) ** 2


def cache(func: Callable) -> Callable:
    f_cache = {}

    def wrapper(*args: int) -> int:
        if args in f_cache:
            return f_cache[args]

        f_cache[args] = func(*args)
        return f_cache[args]

    return wrapper
