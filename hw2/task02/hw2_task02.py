"""
Given an array of size n, find the most common and the least common elements.

The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from collections import defaultdict


def major_and_minor_elem(numbers: list) -> tuple:
    counter = defaultdict(int)
    major = minor = None
    major_count = -float("INF")
    minor_count = float("INF")
    for item in numbers:
        counter[item] += 1

    for item, amount in counter.items():
        if amount > major_count:
            major, major_count = item, amount
        if amount < minor_count:
            minor, minor_count = item, amount

    return major, minor
