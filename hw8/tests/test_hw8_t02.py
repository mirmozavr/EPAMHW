import os.path

from hw8.hw8_t02 import TableData

db_path = os.path.dirname(__file__) + "/example.sqlite"


def test_table_data_length():
    presidents = TableData(db_path, "presidents")
    assert len(presidents) == 3


def test_table_data_contains():
    presidents = TableData(db_path, "presidents")
    assert "Trump" in presidents
    assert "Lincoln" not in presidents


def test_table_data_get_item():
    presidents = TableData(db_path, "presidents")
    assert presidents["Trump"] == ("Trump", 1337, "US")
