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


def test_search_a_list_in_a_tree():
    tree = {
        "hit": [10, 20],
        "nested list": ["element", 123, [10, 20]],
        "nested dict": {"nested key": [10, 20]},
        "look alike": [10, 20, 10, 20],
    }
    assert find_occurrences(tree, [10, 20]) == 3


def test_nested_sets_and_tuples():
    tree = {
        "tuple": ("RED", "BLUE"),
        "dictionary": {
            "nested set": {
                "simple",
                "set",
                "of",
                "RED",
                "values",
                ("nested_tuple", "RED", "BLUE", "RED", "RED"),
            },
        },
        "another dictionary": {
            "abc": "BLUE",
            "jhl": {"RED"},
            "complex": {
                "key1": "value1",
                "key2": "RED",
                "set": {"a", "lot", "of", "values"},
            },
        },
    }
    assert find_occurrences(tree, "RED") == 7
