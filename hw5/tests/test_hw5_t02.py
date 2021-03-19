from unittest.mock import Mock

from hw5.hw5_t02 import custom_sum, print_result


def test_tuple_of_integers():
    assert custom_sum(1, 2, 3, 4) == 10


def test_three_lists_with_integers():
    assert custom_sum([1, 2, 3], [9, 9], [4, 5]) == [1, 2, 3, 9, 9, 4, 5]


def test_text_arguments():
    assert custom_sum("dragon", "fly") == "dragonfly"


def test_saved_function_is_original_function():
    foo = Mock(__name__="")
    custom_f = print_result(foo)
    assert custom_f.__original_func is foo
