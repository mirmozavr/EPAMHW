from hw6.hw6_t01 import instances_counter


@instances_counter
class User:
    """Pass."""


@instances_counter
class Counterator:
    count = "abc"

    def abc(self):
        return self.count


def test_instances_counter():
    a, b, c = User(), User(), User()  # noqa: F841
    assert a.get_created_instances() == 3
    d = User()
    assert d.get_created_instances() == 4


def test_reset_instances_counter():
    a, b, c = User(), User(), User()  # noqa: F841
    a.reset_instances_counter()
    assert a.get_created_instances() == 0


def test_instances_counter_with_tricky_class():
    a, b, c = Counterator(), Counterator(), Counterator()  # noqa: F841
    assert a.get_created_instances() == 3
    d = Counterator()
    assert d.get_created_instances() == 4


def test_reset_instances_counter_with_tricky_class():
    a, b, c = Counterator(), Counterator(), Counterator()  # noqa: F841
    a.reset_instances_counter()
    assert a.get_created_instances() == 0


def test_tricky_class_keeps_its_behaviour():
    a = Counterator()  # noqa: F841
    assert a.count == "abc"
    assert a.abc() == "abc"
