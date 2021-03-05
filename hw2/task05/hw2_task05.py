"""Custom range.

Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
"""


def custom_range(
    it_obj: str, start: str = None, end: str = None, step: int = 1
) -> list:
    result = []
    if start is None:
        start = 0
    else:
        start = it_obj.index(start)
    if end is None:
        end, start = start, 0
    else:
        end = it_obj.index(end)

    for i in range(start, end, step):
        result.append(it_obj[i])

    return result
