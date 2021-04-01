import os.path

from hw8.hw8_t02 import TableData

db_path = os.path.dirname(__file__) + "/example.sqlite"


def test_table_data_length():
    with TableData(db_path, "presidents") as presidents:
        assert len(presidents) == 3


def test_table_data_contains():
    with TableData(db_path, "presidents") as presidents:
        assert "Trump" in presidents
        assert "Lincoln" not in presidents


def test_table_data_get_item():
    with TableData(db_path, "presidents") as presidents:
        assert presidents["Trump"] == ("Trump", 1337, "US")
