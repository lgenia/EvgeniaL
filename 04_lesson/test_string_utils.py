import pytest
from string_utils import StringUtils


string_utils = StringUtils()


def test_capitalize_positive():
    assert string_utils.capitalize("евгения") == "Евгения"


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_trim_positive():
    assert string_utils.trim("    skypro") == "skypro"


def test_trim_negative():
    assert string_utils.trim("skypro   ") == "skypro   "


def test_contains_positive():
    assert string_utils.contains("Skypro", "y")
    assert string_utils.contains("Skypro", "d") is False


def test_contains_negative():
    assert string_utils.contains(" ", " ")
    assert string_utils.contains("", "")


def test_delete_symbol_positive():
    assert string_utils.delete_symbol("Skypro", "y") == "Skpro"
    assert string_utils.delete_symbol("Skypro", "pro") == "Sky"


def test_delete_symbol_negative():
    assert string_utils.delete_symbol("Skypro", "pa") == "Skypro"
    assert string_utils.delete_symbol("Sky", "") == "Sky"
