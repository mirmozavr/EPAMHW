"""
Given a file containing text.

Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from collections import Counter


def open_file_and_count_chars(file_path: str) -> Counter:
    """Open file and decipher and count chars."""
    counter = Counter()
    with open("data.txt", "r") as text:
        for line in text:
            while "\\u" in line:
                index = line.index("\\u")
                deciphered_char = chr(int("0x" + line[index + 2 : index + 6], 16))
                line = line[:index] + deciphered_char + line[index + 6 :]
            counter.update(Counter(line))
    return counter


def open_file_and_yield_line(file_path: str) -> str:
    with open("data.txt", "r") as text:
        for line in text:
            while "\\u" in line:
                index = line.index("\\u")
                deciphered_char = chr(int("0x" + line[index + 2 : index + 6], 16))
                line = line[:index] + deciphered_char + line[index + 6 :]
            yield line


def get_longest_diverse_words(file_path: str) -> list:
    top_10_words = [["", 0] for _ in range(10)]
    for line in open_file_and_yield_line(file_path):
        for word in line.split():
            word = word.strip(string.punctuation)
            unique_length = len(set(word))
            for i in range(10):
                if unique_length > top_10_words[i][1]:
                    top_10_words[i][0] = word
                    top_10_words[i][1] = unique_length
                    break
    return top_10_words


def get_rarest_char(file_path: str) -> str:
    return open_file_and_count_chars(file_path).most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    punctuation_char_count = 0
    counter = open_file_and_count_chars(file_path)
    for char in counter:
        if char in string.punctuation:
            punctuation_char_count += counter[char]
    return punctuation_char_count


def count_non_ascii_chars(file_path: str) -> int:
    non_ascii_char_count = 0
    counter = open_file_and_count_chars(file_path)
    for char in counter:
        if char not in string.printable:
            non_ascii_char_count += counter[char]
    return non_ascii_char_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter = open_file_and_count_chars(file_path)
    for char in counter:
        if char not in string.printable:
            return char
    return "No non-ascii chars"
