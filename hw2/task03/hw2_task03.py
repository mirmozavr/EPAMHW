"""Write a function.

That takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert comb([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""


def combination_of_lists(*args: list) -> list:
    result = [[]]
    for pool in args:
        result = [base + [suffix] for base in result for suffix in pool]
    return result
