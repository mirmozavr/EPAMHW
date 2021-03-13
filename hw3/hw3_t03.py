"""I decided to write a code that generates data filtering object from a list of keyword parameters."""

from functools import partial
from typing import Any, Callable


class Filter:
    """
    Helper filter class.

    Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *args: Callable):
        self.functions = list(args)

    def apply(self, data: Any) -> list:  # noqa: D102
        return [item for item in data if all(foo(item) for foo in self.functions)]


def make_filter(keywords: dict) -> Any:
    """
    Generate filter object for specified keywords.
    """
    filter_funcs = []

    for key, value in keywords.items():

        def keyword_filter_func(data: dict, filter_key: Any, filter_value: Any) -> bool:
            return filter_key in data and data[filter_key] == filter_value

        filter_funcs.append(
            partial(keyword_filter_func, filter_key=key, filter_value=value)
        )
    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

# make_filter(name='polly', type='bird').apply(sample_data) should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
