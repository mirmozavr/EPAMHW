from hw3.hw3_task01 import cache_factory


class TestPlug:
    """Test plug for class object."""


def test_with_number():
    @cache_factory(times=3)
    def f(x):
        return x * 1.1

    val_1 = f(5)
    val_2 = f(5)
    val_3 = f(5)
    assert val_1 == val_2 == val_3


def test_with_string():
    @cache_factory(times=2)
    def txt(text: str):
        return text * 2

    val_1 = txt("Bob")
    val_2 = txt("Bob")
    assert val_1 == val_2


@cache_factory(times=2)
def object_function(any_object):
    return any_object()


v1 = object_function(TestPlug)
v2 = object_function(TestPlug)
v3 = object_function(TestPlug)
v4 = object_function(TestPlug)
v5 = object_function(TestPlug)
v6 = object_function(TestPlug)
v7 = object_function(TestPlug)
v8 = object_function(TestPlug)
v9 = object_function(TestPlug)


def test_class_same_object():
    assert v1 is v2 is v3, "Their ID is equal, same object from cache"


def test_class_outside_cache_size():
    assert v1 is not v4, "Their ID is not equal, other object"
    assert v2 is not v4, "Their ID is not equal, other object"
    assert v3 is not v4, "Their ID is not equal, other object"


def test_cache_called_8_times():
    assert v1 is v2 is v3, "Their ID is equal, same object from cache"
    assert v3 is not v4, "Their ID is not equal, other object"
    assert v4 is v5 is v6, "Their ID is equal, same object from cache"
    assert v6 is not v7, "Their ID is not equal, other object"
    assert v7 is v8 is v9, "Their ID is equal, same object from cache"
