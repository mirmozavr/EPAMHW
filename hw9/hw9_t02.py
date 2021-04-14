"""
Write a context manager, that suppresses passed exception.

Do it both ways: as a class and as a generator.
with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    def __init__(self, exception: Exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # noqa: ANN001
        return exc_type is self.exception


@contextmanager
def suppressor(exception: Exception) -> None:
    try:
        yield
    except exception:
        pass
