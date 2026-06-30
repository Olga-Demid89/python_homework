import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("привет", "Привет"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("1 first", "1 first"),
    ("", ""),
    ("   ", "   "),
    ("%&#", "%&#")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" 123456", "123456"),
    (" Привет, мир!", "Привет, мир!"),
    ("   Hello", "Hello")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" ", ""),
    (" %$#$", "%$#$"),
    ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Строка", "т", True),
    ("String", "i", True),
    ("Teacher", "w", False),
    ("123456", "5", True),
    ("%$#", "$", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "", True),
    ("FiRst test", " ", True),
    (" . ", ".", True),
    (" ", "#", False),
    ("QA-engineer", "a", True)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Строка", "т", "Срока"),
    ("String", "i", "Strng"),
    ("Tea cher", " ", "Teacher"),
    ("123456", "5", "12346"),
    ("%$#", "$", "%#"),
    ("Telegram", "e", "Tlgram")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "", ""),
    (" ", " ", ""),
    ("Teacher", "w", "Teacher"),
    ("SKyPro", "k", "SyPro")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
