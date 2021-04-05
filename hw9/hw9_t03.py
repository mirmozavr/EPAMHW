"""
Write a function that takes directory path, a file extension and an optional tokenizer.

It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test_dir, "txt")
6
universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional, Union


def count_lines_or_tokens(
    file_path: Union[str, Path], tokenizer: Callable[[str], str]
) -> int:
    counter = 0
    with open(file_path) as file:
        for _item in tokenizer(file.read()):
            counter += 1
        return counter


def universal_file_counter(
    dir_path: Union[str, Path],
    file_extension: str,
    tokenizer: Optional[Callable[[str], str]] = str.splitlines,
) -> int:
    counter = 0
    file_list = [
        name for name in os.listdir(dir_path) if name.endswith("." + file_extension)
    ]

    for name in file_list:
        file_path = "/".join((dir_path, name))
        counter += count_lines_or_tokens(file_path, tokenizer)
    return counter
