import pytest

from hw11.hw11_t01 import SimplifiedEnum


def test_class_attributes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE != "RED"


def test_absent_attributes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    with pytest.raises(AttributeError):
        ColorsEnum.PINK
