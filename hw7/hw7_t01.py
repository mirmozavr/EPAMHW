"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def parse_list(parsed_list: list, element: Any) -> int:
    counter = 0
    for val in parsed_list:
        if val == element:
            counter += 1
        elif isinstance(val, dict):
            counter += find_occurrences(val, element)
        elif isinstance(val, list):
            counter += parse_list(val, element)
    return counter


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    for val in tree.values():
        if val == element:
            counter += 1
        elif isinstance(val, dict):
            counter += find_occurrences(val, element)
        elif isinstance(val, list):
            counter += parse_list(val, element)

    return counter
