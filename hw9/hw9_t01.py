"""
Write a function that merges integer from sorted files and returns an iterator.

file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    queue = list(map(open_file_return_iterator, file_list))
    result = []
    while queue:
        for file in queue:
            load_next_or_remove_generator(file, queue, result)
            bubble_single_digit(result)
    return iter(result)


def open_file_return_iterator(path: Union[Path, str]) -> Iterator:
    with open(path) as file:
        yield from (int(row) for row in file)


def load_next_or_remove_generator(file: Iterator, queue: list, result: list) -> None:
    try:
        result.append(next(file))
    except StopIteration:
        queue.remove(file)


def bubble_single_digit(result: list) -> None:
    i = len(result) - 1
    while i > 0 and result[i] < result[i - 1]:
        result[i], result[i - 1] = result[i - 1], result[i]
        i -= 1
