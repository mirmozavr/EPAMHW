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
    finished = True
    for row in range(3):
        if board[row].count("-") > 0:
            finished = False
        elif board[row].count("x") == 3:
            return "x wins!"
        elif board[row].count("o") == 3:
            return "o wins!"
    if not finished:  # noqa: R503
        return "unfinished"


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


def tic_tac_toe_checker(board: List[List]) -> str:
    finished = True
    row_check_result = check_row_win(board)
    if row_check_result == "unfinished":
        finished = False
    elif row_check_result:
        return row_check_result

    column_check_result = check_column_win(board)
    if column_check_result:
        return column_check_result

    diagonal_check_result = check_diagonal_win(board)
    if diagonal_check_result:
        return diagonal_check_result

    return "draw!" if finished else "unfinished"
