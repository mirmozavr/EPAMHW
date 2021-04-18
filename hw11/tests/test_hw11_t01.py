import pytest

from hw11.hw11_t01 import SimplifiedEnum


def test_colorsenum_attributes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE != "BLACK"


def test_sizeenum_attributes():
    class SizesEnum(metaclass=SimplifiedEnum):
        __keys = ("XL", "L", "M", "S", "XS")

    assert SizesEnum.XL == "XL"
    assert SizesEnum.M != "S"


def test_absent_attributes():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    with pytest.raises(AttributeError):
        ColorsEnum.PINK
