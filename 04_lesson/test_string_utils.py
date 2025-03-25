import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# проверка для capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
# проверки для trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),         # Один пробел
    ("skypro", "skypro"),          # Строка без пробелов
    (" ", ""),                 # Только пробелы
    ("", "")                       # Пустая строка
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected_exception", [
    (123, AttributeError),
    (None, AttributeError),
])
def test_trim_negative(input_str, expected_exception):
    with pytest.raises(expected_exception):
        string_utils.trim(input_str)

# проверки для contains

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),                # Буква присутствует
    ("SkyPro", "y", True),                # Маленькая буква присутствует
    ("SkyPro", "z", False),               # Буквы нет
    ("SkyPro", "P", True),                # Прописная буква
    ("SkyPro", " ", False),               # Пробельный символ отсутствует
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_exception", [
    (123, "a", AttributeError),                # Нестроковое значение
    (None, "a", AttributeError),          # Значение None
])
def test_contains_negative(input_str, symbol, expected_exception):
    with pytest.raises(expected_exception):
        string_utils.contains(input_str, symbol)

 # проверки для  delete_symbol

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),  # Однократное удаление символа
    ("SkyPro", "P", "Skyro"),  # Многократное удаление символа
    ("SkyPro", "x", "SkyPro"),  # Символ отсутствует
    ("SkyPro", "", "SkyPro"),  # Пустой символ
    ("SkyPro", " ", "SkyPro"),  # Пробельный символ отсутствует
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected_exception", [
    (123, "a", AttributeError),  # Нестроковое значение
    (None, "a", AttributeError ),  # Значение None
])
def test_delete_symbol_negative(input_str, symbol, expected_exception):
    with pytest.raises(expected_exception):
        string_utils.delete_symbol(input_str, symbol)




