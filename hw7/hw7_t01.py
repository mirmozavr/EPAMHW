"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Union


def parse_collection(parsed_collection: Union[list, set, tuple], element: Any) -> int:
    counter = 0
    for value in parsed_collection:
        if value == element:
            counter += 1
        elif isinstance(value, dict):
            counter += find_occurrences(value, element)
        elif isinstance(value, (list, set, tuple)):
            counter += parse_collection(value, element)
        elif isinstance(element, str) and len(element) == 1 and isinstance(value, str):
            counter += parse_string(value, element)
    return counter


def parse_string(parsed_string: str, element: str) -> int:
    counter = 0
    for char in parsed_string:
        if char == element:
            counter += 1
    return counter


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    for value in tree.values():
        if value == element:
            counter += 1
        elif isinstance(value, dict):
            counter += find_occurrences(value, element)
        elif isinstance(value, (list, set, tuple, str)):
            counter += parse_collection(value, element)

    return counter
