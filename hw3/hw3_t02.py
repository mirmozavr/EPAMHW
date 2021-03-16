"""
Here's a not very efficient calculation function that calculates something important.

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
 Calculation time should not take more than a minute. Use functional capabilities of
multiprocessing module. You are not allowed to modify slow_calculate function.
"""

import hashlib
import random
import struct
import time
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    time.sleep(random.randint(1, 3))  # noqa: S311
    data = hashlib.md5(str(value).encode()).digest()  # noqa: S303
    return sum(struct.unpack("<" + "B" * len(data), data))


def slow_calc_500_numbers() -> list:
    with Pool(processes=50) as pool:
        return pool.map(slow_calculate, range(501))
