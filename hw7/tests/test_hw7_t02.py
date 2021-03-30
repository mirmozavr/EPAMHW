from hw7.hw7_t02 import backspace_compare


def test_different_words_no_backspaces():
    assert backspace_compare("asdf", "fdsa") is False


def test_equal_words_no_backspaces():
    assert backspace_compare("asdf", "asdf") is True


def test_backspaces_in_the_middle():
    assert backspace_compare("asdf####asdf", "as00##df") is True


def test_backspaces_at_the_start():
    assert backspace_compare("##asdf#", "#asdd#ff##") is True


def test_only_backspaces_and_empty_string():
    assert backspace_compare("###", "") is True
