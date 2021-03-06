import os.path

from hw8.hw8_t02 import TableData

db_path = os.path.dirname(__file__) + "/example.sqlite"


def test_context_manager_table_data_length():
    with TableData(db_path, "presidents") as presidents:
        assert len(presidents) == 3


def test_context_manager_table_data_contains():
    with TableData(db_path, "presidents") as presidents:
        assert "Trump" in presidents
        assert "Lincoln" not in presidents


def test_context_manager_table_data_get_item():
    with TableData(db_path, "presidents") as presidents:
        assert presidents["Trump"] == ("Trump", 1337, "US")


def test_context_manager_table_data_is_iterable_by_rows():
    with TableData(db_path, "presidents") as presidents:
        names, ages, countries = [], [], []
        for president in presidents:
            names.append(president["name"])
            ages.append(president["age"])
            countries.append(president["country"])
        assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
        assert ages == [999, 1337, 101]
        assert countries == ["Russia", "US", "Kekistan"]


def test_table_data_length():
    presidents = TableData(db_path, "presidents")
    assert len(presidents) == 3
    presidents.close()


def test_table_data_contains():
    presidents = TableData(db_path, "presidents")
    assert "Trump" in presidents
    assert "Lincoln" not in presidents
    presidents.close()


def test_table_data_get_item():
    presidents = TableData(db_path, "presidents")
    assert presidents["Trump"] == ("Trump", 1337, "US")
    presidents.close()


def test_table_data_is_iterable_by_rows():
    presidents = TableData(db_path, "presidents")
    names, ages, countries = [], [], []
    for president in presidents:
        names.append(president["name"])
        ages.append(president["age"])
        countries.append(president["country"])
    assert names == ["Yeltsin", "Trump", "Big Man Tyrone"]
    assert ages == [999, 1337, 101]
    assert countries == ["Russia", "US", "Kekistan"]
    presidents.close()
