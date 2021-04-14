import os

from hw9.hw9_t01 import merge_sorted_files

file_dir = os.path.dirname(__file__)


def test_merge_sorted_files():
    assert (
        list(
            merge_sorted_files(
                [
                    file_dir + "/positive_nums_1.txt",
                    file_dir + "/positive_nums_2.txt",
                    file_dir + "/negative_nums.txt",
                    file_dir + "/empty_file.txt",
                ]
            )
        )
        == [-8, -3, -1, 0, 1, 4, 5, 6]
    )
