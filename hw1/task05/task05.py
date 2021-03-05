"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""


def find_maximal_subarray_sum(nums: list, k: int) -> int:
    """Max sum of continuous sub-array."""
    yet_max_sum = 0
    size = len(nums)
    # fixing situation where k > N
    k = min(size, k)

    for i in range(size):
        for j in range(1, k + 1):
            yet_max_sum = max(sum(nums[i : i + j]), yet_max_sum)
            if i + j >= size:
                break
    return yet_max_sum
