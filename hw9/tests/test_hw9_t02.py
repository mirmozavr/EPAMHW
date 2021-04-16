import pytest

from hw9.hw9_t02 import Suppressor, suppressor

test_subjects = [Suppressor, suppressor]


@pytest.fixture(params=test_subjects, ids=[subj.__name__ for subj in test_subjects])
def function(request):
    return request.param


def test_context_manager_positive_suppress_index_error(function):
    with function(IndexError):
        [][1]
    assert True


def test_context_manager_positive_suppress_key_error(function):
    with function(KeyError):
        {"a": 1}["b"]
    assert True


def test_context_manager_suppress_wrong_error_raise_value_error(function):
    with pytest.raises(ValueError):  # noqa: PT011,PT012
        with function(KeyError):
            int("string")
