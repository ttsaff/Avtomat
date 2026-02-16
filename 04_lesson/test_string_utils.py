import pytest
from string_utils import StringUtils


utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("skypro", "Skypro"),
        ("тест", "Тест"),
        ("hello world", "Hello world"),
        ("123", "123"),
    ]
)
def test_capitalize_positive(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", "   "),
    ]
)
def test_capitalize_negative(input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.negative
def test_capitalize_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)

@pytest.mark.positive
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("   skypro", "skypro"),
        (" skypro", "skypro"),
        ("skypro", "skypro"),
        ("   hello world", "hello world"),
    ]
)
def test_trim_positive(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),
        ("   ", ""),
    ]
)
def test_trim_negative(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.negative
def test_trim_none():
    with pytest.raises(AttributeError):
        utils.trim(None)

@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "S"),
        ("SkyPro", "y"),
        ("123", "2"),
    ]
)
def test_contains_positive(string, symbol):
    assert utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol",
    [
        ("SkyPro", "U"),
        ("", "a"),
    ]
)
def test_contains_negative(string, symbol):
    assert utils.contains(string, symbol) is False


@pytest.mark.negative
def test_contains_none_string():
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


@pytest.mark.negative
def test_contains_empty_symbol():
    assert utils.contains("SkyPro", "") is True

@pytest.mark.positive
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("123123", "1", "2323"),
    ]
)
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "U", "SkyPro"),
        ("", "a", ""),
    ]
)
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
def test_delete_symbol_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")