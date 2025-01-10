import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    ''' Тесты с правильными данными'''
    assert mask_account_card("Счет 1234567890") == "Счет **7890"
    assert mask_account_card("Карта 1234567890123456") == "Карта 1234 56** **** 3456"

    # Параметризованные тесты
    test_cases = [
        ("Счет 123456", "Счет **3456"),
        ("Карта 8765432187654321", "Карта 8765 43** **** 4321"),
    ]

    for account_info, expected in test_cases:
        assert mask_account_card(account_info) == expected

    # Тесты с некорректными данными
    with pytest.raises(ValueError):
        mask_account_card("Некорректный Ввод")  # Неверный ввод

    with pytest.raises(ValueError):
        mask_account_card("Карта 1234567890")  # Неправильный номер карты


# Тесты для get_date
def test_get_date():
    assert get_date("2023-03-10T14:30:00") == "10.03.2023"
    assert get_date("2021-01-01T00:00:00") == "01.01.2021"

    with pytest.raises(ValueError):
        get_date("Некорректная Строка")  # Некорректный формат даты

    with pytest.raises(ValueError):
        get_date("")  # Пустая строка


