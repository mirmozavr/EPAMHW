from hw7.hw7_t01 import find_occurrences


def test_empty_dictionary():
    tree = {}
    assert find_occurrences(tree, "element") == 0


def test_nested_dicts_and_lists():
    tree = {
        "first": ["RED", "BLUE"],
        "second": {
            "simple_key": [
                "simple",
                "list",
                "of",
                "RED",
                "valued",
                ["nested_list", "RED", "BLUE", "RED", "RED"],
            ],
        },
        "third": {
            "abc": "BLUE",
            "jhl": "RED",
            "complex_key": {
                "key1": "value1",
                "key2": "RED",
                "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
            },
        },
        "fourth": "RED",
    }
    assert find_occurrences(tree, "RED") == 9
