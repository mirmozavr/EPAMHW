from unittest.mock import patch

import pytest

from hw4.hw4_t02 import count_dots_on_i


@patch("hw4.hw4_t02.get_url_return_str", return_value="iiiiiiii")
def test_count_dots_on_i_8_symbols(m_get_url_return_str):
    assert count_dots_on_i("any.url.com") == 8


@patch("hw4.hw4_t02.get_url_return_str", return_value="")
def test_count_dots_on_i_zero_symbols(m_get_url_return_str):
    assert count_dots_on_i("any.url.com") == 0


@patch("hw4.hw4_t02.get_url_return_str", return_value="no correct symbol here")
def test_count_dots_on_i_only_other_symbols(m_get_url_return_str):
    assert count_dots_on_i("any.url.com") == 0


@patch(
    "hw4.hw4_t02.get_url_return_str",
    return_value="There are four 'i' symbols in this line",
)
def test_count_dots_on_i_mixed_symbol_string(m_get_url_return_str):
    assert count_dots_on_i("any.url.com") == 4


@patch("hw4.hw4_t02.get_url_return_str", return_value="IIIIIIII")
def test_count_dots_on_i_capital_i_symbols(m_get_url_return_str):
    assert count_dots_on_i("any.url.com") == 0


def test_count_dots_on_i_url_is_unavailable():
    with pytest.raises(ValueError, match="Unreachable unavailable.url.com"):
        count_dots_on_i("unavailable.url.com")
