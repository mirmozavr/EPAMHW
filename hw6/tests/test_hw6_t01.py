from hw6.hw6_t01 import User


def test_instances_counter():
    a, b, c = User(), User(), User()  # noqa: F841
    assert a.get_created_instances() == 3
    d = User()
    assert d.get_created_instances() == 4


def test_reset_instances_counter():
    User.count = 0
    a, b, c = User(), User(), User()  # noqa: F841
    a.reset_instances_counter()
    assert a.get_created_instances() == 0
