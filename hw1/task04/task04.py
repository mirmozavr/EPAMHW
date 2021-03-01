"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""


def check_sum_of_four(a: list, b: list, c: list, d: list) -> int:
    s = {}
    N = len(a)
    ans = 0
    for i in range(N):
        for j in range(N):
            remainder = 0 - (a[i] + b[j])
            if remainder not in s:
                s[remainder] = 1
            else:
                s[remainder] += 1

    for k in range(N):
        for l in range(N):
            subtrahend = c[k] + d[l]
            if subtrahend in s:
                ans += s[subtrahend]
    return ans
