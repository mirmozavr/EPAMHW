from hw3.hw3_t03 import make_filter


def test_polly():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert make_filter({"name": "polly", "type": "bird"}).apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_both_characters_by_diff_parameter():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert (
        make_filter(
            {
                "occupation": "was here",
                "type": "bird",
            }
        ).apply(sample_data)
        == []
    )


def test_with_non_existent_value():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert (
        make_filter(
            {
                "occupation": "here",
                "type": "bird",
            }
        ).apply(sample_data)
        == []
    )


def test_with_non_existent_key():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert (
        make_filter(
            {
                "name": "Bill",
                "age": 44,
            }
        ).apply(sample_data)
        == []
    )


def dont_test_both_characters_by_diff_parameter():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert (
        make_filter(
            {
                "name": "Bill",  # noqa: F601
                "name": "polly",  # noqa: F601
            }
        ).apply(sample_data)
        == []
    )
