from python_project_scripts import generate_diff


def test_1():
    file1 = {'name': "John", 'age': 35}
    file2 = {'name': "John", 'age': 37}

    expected = """{
  - age: 35
  + age: 37
    name: John
}"""

    assert generate_diff(file1, file2) == expected


def test_2():
    file1 = {'a': 1}
    file2 = {'a': 1, 'b': 2}

    expected = """{
    a: 1
  + b: 2
}"""

    assert generate_diff(file1, file2) == expected


def test_3():
    file1 = {}
    file2 = {}

    expected = """{

}"""

    assert generate_diff(file1, file2) == expected


def test_4():
    file1 = {'a': 1, 'b': 2}
    file2 = {'a': 1}

    expected = """{
    a: 1
  - b: 2
}"""

    assert generate_diff(file1, file2) == expected


def test_5():
    file1 = {'a': 1, 'b': 2}
    file2 = {'c': 3, 'd': 4}

    expected = """{
  - a: 1
  - b: 2
  + c: 3
  + d: 4
}"""

    assert generate_diff(file1, file2) == expected