"""
Write a function that merges integer from sorted files and returns an iterator
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
import timeit
from pathlib import Path
from typing import Iterator, List, Union


def open_file_return_map(path: Union[Path, str]):
    with open(path, "r") as file:
        return map(int, file.read().split())


def merge_sorted_files_slower(file_list: List[Union[Path, str]]) -> Iterator:
    list_of_map_objects = [obj for obj in map(open_file_return_map, file_list)]
    result = []
    batch = []
    infinite = float("INF")
    small = -float("INF")

    for item in list_of_map_objects:
        batch.append(next(item, infinite))

    while small != float("INF"):

        small = min(batch)
        small_index = batch.index(small)
        result.append(small)
        batch[small_index] = next(list_of_map_objects[small_index], infinite)

    result.pop()
    return iter(result)


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    result = []

    for obj in map(open_file_return_map, file_list):
        result.extend(obj)
    result.sort()

    return iter(result)


a = timeit.default_timer()
print(
    list(merge_sorted_files_slower(
        [
            "file1.txt",
            "file2.txt",
            "file3.txt",
            "file4.txt",
        ]
    ))
)
b = timeit.default_timer()
print("delta", b - a)


a = timeit.default_timer()
print(
    list(
        merge_sorted_files(
            [
                "file1.txt",
                "file2.txt",
                "file3.txt",
                "file4.txt",
            ]
        )
    )
)
b = timeit.default_timer()
print("delta", b - a)
