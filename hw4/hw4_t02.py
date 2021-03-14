"""
Write a function that accepts an URL as input.

and count how many letters `i` are present in the HTML by this URL.

Write a test that check that your function works.
Test should use Mock instead of real network interactions.

You can use urlopen* or any other network libraries.
In case of any network error raise ValueError("Unreachable {url}).

Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests

You will learn:
 - how to test using mocks
 - how to write complex mocks
 - how to raise an exception form mocks
 - do a simple network requests


>> count_dots_on_i("https://example.com/")
59

* https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
"""
from unittest.mock import Mock

from requests import get


def get_url_return_str(url: str) -> str:
    try:
        r = get(url)
    except Exception:
        raise ValueError(f"Unreachable {url}")
    return r.text


def count_dots_on_i(url: str) -> int:
    return get_url_return_str(url).count("i")


get_url_return_str = Mock()  # noqa: F811
get_url_return_str.return_value = "22 i symbols in total iiiiiiiiiiiiiiiiiiii"