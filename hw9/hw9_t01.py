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
import bisect
from pathlib import Path
from typing import Iterator, List, Optional, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    queue = list(map(open_file_return_generator, file_list[1:]))
    result = list(open_file_return_generator(file_list[0]))
    while queue:
        for file in queue:
            digit = load_next_or_remove_generator(file, queue)
            if digit is not None:
                bisect.insort_left(result, digit)
    return iter(result)


def open_file_return_generator(path: Union[Path, str]) -> Iterator:
    with open(path) as file:
        yield from (int(row) for row in file)


def load_next_or_remove_generator(file: Iterator, queue: list) -> Optional[int]:
    try:
        return next(file)
    except StopIteration:
        queue.remove(file)
