from unittest.mock import Mock

from hw3.hw3_task01 import cache_factory


def test_with_object_type_cache_size_2():
    @cache_factory(times=2)
    def foo(obj):
        return obj()

    a = foo(Mock)
    b = foo(Mock)
    c = foo(Mock)
    a2 = foo(Mock)
    b2 = foo(Mock)
    c2 = foo(Mock)
    a3 = foo(Mock)
    assert a is b, "original is first from cache"
    assert b is c, "1st from cache is 2nd from cache"
    assert c is not a2, "2nd from previous cache is not new original, cache cleared"
    assert a2 is b2, "new original is 1st from new cache"
    assert b2 is c2, "1st from new cache is 2nd from new cache"
    assert c2 is not a3, "2nd from previous cache is not new original, cache cleared"


def test_with_object_type_cache_size_3():
    @cache_factory(times=3)
    def foo(obj):
        return obj()

    a = foo(Mock)
    b = foo(Mock)
    c = foo(Mock)
    d = foo(Mock)
    a2 = foo(Mock)
    assert a is b is c is d, "original and three values from cache"
    assert d is not a2, "3rd from cache is not new original, cache cleared"
