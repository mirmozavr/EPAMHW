"""
Classic task, a kind of walnut for you.

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that
A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""

from collections import defaultdict


def check_sum_of_four(a: list, b: list, c: list, d: list) -> int:
    """Count sum of four where sum = 0."""
    cache = defaultdict(int)
    size = len(a)
    count = 0
    for i in range(size):
        for j in range(size):
            remainder = 0 - (a[i] + b[j])
            cache[remainder] += 1

    for i in range(size):
        for j in range(size):
            subtrahend = c[i] + d[j]
            if subtrahend in cache:
                count += cache[subtrahend]
    return count
