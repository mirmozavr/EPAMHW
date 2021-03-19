"""
Написать декоратор который позволит сохранять информацию из.

исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func.

print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий

До применения вашего декоратор будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция

Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools
from typing import Any, Callable


def print_result(func: Callable) -> Callable:
    # Place for new decorator
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        print(result)  # noqa: T001
        return result

    wrapper.__doc__ = func.__doc__
    wrapper.__name__ = func.__name__
    wrapper.__original_func = func
    return wrapper


@print_result
def custom_sum(*args: Any) -> Any:
    """This function can sum any objects which have __add___."""  # noqa: D401
    return functools.reduce(lambda x, y: x + y, args)
