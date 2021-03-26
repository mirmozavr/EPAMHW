"""
Given a dictionary (tree), that can contains multiple nested structures.

Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def parse_collection(parsed_collection: list, element: Any) -> int:
    counter = 0
    for value in parsed_collection:
        if value == element:
            counter += 1
        elif isinstance(value, dict):
            counter += find_occurrences(value, element)
        elif isinstance(value, (list, set, tuple)):
            counter += parse_collection(value, element)
    return counter


def find_occurrences(tree: dict, element: Any) -> int:
    counter = 0
    for value in tree.values():
        if value == element:
            counter += 1
        elif isinstance(value, dict):
            counter += find_occurrences(value, element)
        elif isinstance(value, (list, set, tuple)):
            counter += parse_collection(value, element)

    return counter
