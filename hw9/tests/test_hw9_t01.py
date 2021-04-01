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
        == [-4, 1, 2, 3, 3, 3, 4, 5, 6, 7, 9]
    )
