from hw7.hw7_t03 import tic_tac_toe_checker


def test_column_win_by_o():
    assert (
        tic_tac_toe_checker([["x", "x", "o"], ["-", "x", "o"], ["x", "o", "o"]])
        == "o wins!"
    )


def test_row_win_by_x():
    assert (
        tic_tac_toe_checker([["-", "x", "o"], ["x", "x", "x"], ["o", "o", "-"]])
        == "x wins!"
    )


def test_diagonal_win_by_x():
    assert (
        tic_tac_toe_checker([["x", "o", "x"], ["-", "x", "o"], ["x", "o", "-"]])
        == "x wins!"
    )


def test_draw():
    assert (
        tic_tac_toe_checker([["x", "x", "o"], ["o", "x", "x"], ["x", "o", "o"]])
        == "draw!"
    )


def test_unfinished_with_no_winners():
    assert (
        tic_tac_toe_checker([["x", "x", "o"], ["-", "x", "-"], ["x", "o", "o"]])
        == "unfinished"
    )
