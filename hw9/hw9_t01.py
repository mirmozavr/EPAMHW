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
from collections import deque
from pathlib import Path
from typing import Iterator, List, Union


def open_file_return_iterator(path: Union[Path, str]) -> Iterator:
    with open(path) as file:
        yield from (int(row) for row in file)


def merge_2_sorted_iterators(  # noqa: C901,CCR001
    left: Iterator, right: Iterator
) -> Iterator:
    result = []
    try:
        left_item = next(left)
    except StopIteration:
        result.extend(right)
        return iter(result)

    try:
        right_item = next(right)
    except StopIteration:
        result.extend(left)
        return iter(result)

    while True:
        if left_item <= right_item:
            result.append(left_item)
            try:
                left_item = next(left)
            except StopIteration:
                result.append(right_item)
                result.extend(right)
                break
        else:
            result.append(right_item)
            try:
                right_item = next(right)
            except StopIteration:
                result.append(left_item)
                result.extend(left)
                break
    return iter(result)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    queue = deque(map(open_file_return_iterator, file_list))

    while len(queue) > 1:
        queue.appendleft(merge_2_sorted_iterators(queue.pop(), queue.pop()))

    return queue.pop()
