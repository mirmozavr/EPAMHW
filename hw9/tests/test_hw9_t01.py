import os

from hw9.hw9_t01 import merge_sorted_files

file_dir = os.path.dirname(__file__)


def test_merge_4_sorted_files():
    assert (
        merge_sorted_files(
            [
                file_dir + "/file1.txt",
                file_dir + "/file2.txt",
                file_dir + "/file3.txt",
                file_dir + "/file4.txt",
            ]
        )
        == [1, 2, 3, 4, 5]
    )
