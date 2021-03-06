from hw2_task03 import combination_of_lists


def test_combination_of_lists():
    assert combination_of_lists([1, 2], [3, 4]) == [[1, 3], [1, 4], [2, 3], [2, 4]]
    assert combination_of_lists([1], [3]) == [[1, 3]]
    assert combination_of_lists([5, 9], [9, 5]) == [[5, 9], [5, 5], [9, 9], [9, 5]]
    assert combination_of_lists([0, 0], [0, 0]) == [[0, 0], [0, 0], [0, 0], [0, 0]]
