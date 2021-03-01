"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""


def find_maximum_and_minimum(file_name: str) -> tuple:
    value_minimum = float("INF")
    value_maximum = -float("INF")
    with open(file_name) as file:
        for line in file:
            value = int(line)
            if value > value_maximum:
                value_maximum = value
            if value < value_minimum:
                value_minimum = value
    return value_minimum, value_maximum
