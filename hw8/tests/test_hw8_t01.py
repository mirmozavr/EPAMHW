import os

from hw8.hw8_t01 import KeyValueStorage

home_dir = os.path.dirname(__file__)


def test_access_as_collection_item():
    storage = KeyValueStorage(home_dir + "/data.txt")
    assert storage["name"] == "kek"
    assert storage["last_name"] == "top"
    assert storage["power"] == 9001
    assert storage["song"] == "shadilay"


def test_access_as_attributes():
    storage = KeyValueStorage(home_dir + "/data.txt")
    assert storage.name == "kek"
    assert storage.last_name == "top"
    assert storage.power == 9001
    assert storage.song == "shadilay"


def test_built_in_attributes_not_changed():
    storage = KeyValueStorage(home_dir + "/data.txt")
    assert storage.__getitem__ != "shall_not_pass"
