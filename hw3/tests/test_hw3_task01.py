from hw3.hw3_task01 import TestPlug, cache_factory


@cache_factory(times=2)
def object_function(any_object):
    return any_object()


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


v1 = object_function(TestPlug)
v2 = object_function(TestPlug)
v3 = object_function(TestPlug)
v4 = object_function(TestPlug)


def test_class_same_object():
    assert v1 is v2 is v3, "Their ID is equal, same object from cache"


def test_class_outside_cache_size():
    assert v1 is not v4, "Their ID is not equal, other object"
    assert v2 is not v4, "Their ID is not equal, other object"
    assert v3 is not v4, "Their ID is not equal, other object"
