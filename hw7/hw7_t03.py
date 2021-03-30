"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).

Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List, Optional


def check_row_win(board: List[List]) -> Optional[str]:
    for row in range(3):  # noqa: R503
        if board[row].count("x") == 3:
            return "x wins!"
        elif board[row].count("o") == 3:
            return "o wins!"


def check_column_win(board: List[List]) -> Optional[str]:
    for col in range(3):  # noqa: R503
        if [board[row][col] for row in range(3)].count("x") == 3:
            return "x wins!"
        elif [board[row][col] for row in range(3)].count("o") == 3:
            return "o wins!"


def check_diagonal_win(board: List[List]) -> Optional[str]:
    if [board[index][index] for index in range(3)].count("x") == 3:
        return "x wins!"
    elif [board[index][index] for index in range(3)].count("o") == 3:
        return "o wins!"
    elif [board[index][2 - index] for index in range(3)].count("x") == 3:
        return "x wins!"
    elif [board[index][2 - index] for index in range(3)].count("o") == 3:  # noqa: R503
        return "o wins!"


def check_unfinished_or_draw(board: List[List]) -> str:
    for row in range(3):
        if "-" in board[row]:
            return "unfinished"
    return "draw!"


def tic_tac_toe_checker(board: List[List]) -> str:
    return (
        check_row_win(board)
        or check_column_win(board)
        or check_diagonal_win(board)
        or check_unfinished_or_draw(board)
    )
