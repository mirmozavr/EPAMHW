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


def open_file_return_list(path: Union[Path, str]) -> list:
    with open(path, "r") as file:
        return list(map(int, file.read().split()))


def merge_2_sorted_lists(first: list, second: list) -> list:
    i = k = 0
    result = []
    while i < len(first) and k < len(second):
        if first[i] <= second[k]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[k])
            k += 1

    result.extend(first[i:])
    result.extend(second[k:])

    return result


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    queue = deque(map(open_file_return_list, file_list))

    while len(queue) > 1:
        queue.appendleft(merge_2_sorted_lists(queue.pop(), queue.pop()))

    return iter(queue.pop())
