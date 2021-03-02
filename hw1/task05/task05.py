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
    ans = -float("INF")
    index = 0
    n = len(nums)
    # fixing situation where k > N
    k = min(n, k)
    # find max subarray sum and its start index
    for i in range(n - k + 1):
        if sum(nums[i : i + k]) > ans:
            ans = sum(nums[i : i + k])
            index = i

    # exclude negative numbers
    for number in nums[index : index + k]:
        if number < 0:
            ans -= number
    return ans
