"""Here's a not very efficient calculation function that calculates something important.

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
 Calculation time should not take more than a minute. Use functional capabilities of
multiprocessing module. You are not allowed to modify slow_calculate function."""

import hashlib
import random
import struct
import time
from multiprocessing import Process


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def slow_calculate_batch(*nums):
    for num in nums:
        slow_calculate(num)


def slow_calc_500_numbers():
    if __name__ == "__main__":
        procs = []
        for tens in range(50):
            batch = tuple((tens * 10) + digit for digit in range(10))
            proc = Process(target=slow_calculate_batch, args=batch)
            procs.append(proc)
            proc.start()

        for proc in procs:
            proc.join()
