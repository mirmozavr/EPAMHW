import pytest

from hw9.hw9_t02 import Suppressor, suppressor


def test_class_context_manager_positive_suppress_index_error():
    with Suppressor(IndexError):
        [][1]
    assert True


def test_class_context_manager_positive_suppress_key_error():
    with Suppressor(KeyError):
        {"a": 1}["b"]
    assert True


def test_class_context_manager_suppress_wrong_error_raise_value_error():
    with pytest.raises(ValueError):  # noqa: PT011,PT012
        with Suppressor(KeyError):
            int("string")


def test_generator_context_manager_positive_suppress_index_error():
    with suppressor(IndexError):
        [][1]
    assert True


def test_generator_context_manager_positive_suppress_key_error():
    with suppressor(KeyError):
        {"a": 1}["b"]
    assert True


def test_generator_context_manager_suppress_wrong_error_raise_value_error():
    with pytest.raises(ValueError):  # noqa: PT011,PT012
        with suppressor(KeyError):
            int("string")
