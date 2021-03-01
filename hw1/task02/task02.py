"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""


def check_fib(data) -> bool:

    # process short data sequences (2 or less)
    if len(data) == 0:
        return False
    if data[0] != 0:
        return False
    if len(data) == 1:
        return True
    if data[1] != 1:
        return False
    if len(data) == 2:
        return True
    # process longer data sequences(3 or more)
    for i in range(2, len(data)):
        if data[i] != data[i - 1] + data[i - 2]:
            return False
    return True
