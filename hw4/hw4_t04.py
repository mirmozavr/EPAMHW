"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*.

Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

>>> fizzbuzz(5)
['1', '2', 'fizz', '4', 'buzz']

>>> fizzbuzz(17)
['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17']

>>> fizzbuzz(0)
[]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    return [
        ((not number % 3) * "fizz" + (not number % 5) * "buzz") or str(number)
        for number in range(1, n + 1)
    ]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
