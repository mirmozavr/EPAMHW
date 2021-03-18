"""
In previous homework task 4, you wrote a cache function that remembers other function output value.

Modify it to be a parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')   # careful with input() in python2, use raw_input() instead

>> f()
? 1
'1'
>> f()     # will remember previous value
'1'
>> f()     # but use it up to two times only
'1'
>> f()
? 2
'2'


"""
import pickle  # noqa: S403
from typing import Any, Callable


def cache_factory(times: int = 3) -> Callable:
    """Cache funcgion.

    Returns a calculated result of a function once, then returns values from
    cache given amount of times.
    """
    times_counter = times

    def cache(func: Callable) -> Callable:
        cache_db = {}

        def wrapper(*args: Any) -> Any:
            nonlocal times_counter
            if times_counter == 0:
                cache_db.clear()
                times_counter = times

            pickle_dump = pickle.dumps(args)

            if pickle_dump not in cache_db:
                cache_db[pickle_dump] = func(*args)
            else:
                times_counter -= 1
            return cache_db[pickle_dump]

        return wrapper

    return cache
