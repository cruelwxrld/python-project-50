from python_project_scripts import generate_diff


def test_with_values():
    file1 = {
        'a': 1,
        'b': 2,
    }
    file2 = {
        "a": 1,
        "b": 3,
    }

    expected = """{
    a: 1
  - b: 2
  + b: 3
}"""

    assert generate_diff(file1, file2) == expected


def test_with_values_add_from_first_file():
    file1 = {
        "a": 1,
    }
    file2 = {
        "a": 1,
        "b": 3,
    }

    expected = """{
    a: 1
  + b: 3
}"""

    assert generate_diff(file1, file2) == expected


def test_with_values_delete_from_first_file():
    file1 = {
        "a": 1,
        "b": 3,
    }
    file2 = {
        "a": 1,
    }

    expected = """{
    a: 1
  - b: 3
}"""

    assert generate_diff(file1, file2) == expected


def test_without_values():
    file1 = {}
    file2 = {}

    expected = """{

}"""

    assert generate_diff(file1, file2) == expected


def test_with_values_but_different():
    file1 = {
        "a": 1,
        "b": 2,
    }
    file2 = {
        "c": 3,
        "d": 4,
    }

    expected = """{
  - a: 1
  - b: 2
  + c: 3
  + d: 4
}"""

    assert generate_diff(file1, file2) == expected