from hw4.hw4_t03 import my_precious_logger


def test_stdout_simple_text(capsys):
    my_precious_logger("basically, this is any text")
    out, err = capsys.readouterr()
    assert out == "basically, this is any text\n"
    assert err == ""


def test_stdout_mixed_text(capsys):
    my_precious_logger("please raise error now")
    out, err = capsys.readouterr()
    assert out == "please raise error now\n"
    assert err == ""


def test_stderr_mixed_text(capsys):
    my_precious_logger("error: some text")
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "error: some text\n"
