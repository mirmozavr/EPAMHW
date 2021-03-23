import functools
from unittest.mock import Mock

from hw5.hw5_t02 import print_result


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___."""  # noqa: D401
    return functools.reduce(lambda x, y: x + y, args)


def test_tuple_of_integers():
    assert custom_sum(1, 2, 3, 4) == 10


def test_three_lists_with_integers():
    assert custom_sum([1, 2, 3], [9, 9], [4, 5]) == [1, 2, 3, 9, 9, 4, 5]


def test_text_arguments():
    assert custom_sum("dragon", "fly") == "dragonfly"


def test_saved_function_is_original_function():
    func = Mock(__name__="function name", __doc__="function docstring")
    custom_func = print_result(func)
    assert custom_func.__original_func is func
    assert custom_func.__name__ == func.__name__
    assert custom_func.__doc__ == func.__doc__
