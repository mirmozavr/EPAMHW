"""
Given two strings.

Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_word_constructor(sequence: str) -> str:
    stack = []
    for char in sequence:
        if char != "#":
            stack.append(char)
        elif stack:
            stack.pop()
    return "".join(stack)


def backspace_compare(first: str, second: str) -> bool:
    return backspace_word_constructor(first) == backspace_word_constructor(second)
