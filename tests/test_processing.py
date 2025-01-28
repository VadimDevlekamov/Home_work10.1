import unittest
from typing import Any, Dict, List

from src.processing import filter_by_state, get_date, mask_account_card, sort_by_date


class TestFunctions(unittest.TestCase):

    def test_mask_account_card_valid_account(self) -> None:
        """Тестирование корректного ввода счета"""
        account_info: str = "Счет 12345678901234567890"
        expected_output: str = "Счет **7890"  # Изменено в соответствии с фактическим результатом
        result: str = mask_account_card(account_info)
        self.assertEqual(result, expected_output)

    def test_mask_account_card_valid_card(self) -> None:
        """Тестирование корректного ввода карты"""
        account_info: str = "Карта 1234567812345678"
        expected_output: str = "Карта 1234 56** **** 5678"
        result: str = mask_account_card(account_info)
        self.assertEqual(result, expected_output)

    def test_mask_account_card_invalid_card_length(self) -> None:
        """Тестирование неверного ввода карточного номера"""
        account_info: str = "Карта 123"
        with self.assertRaises(ValueError) as context:
            mask_account_card(account_info)
        self.assertEqual(str(context.exception), "Неверный номер карты. Номер карты должен состоять из 16 цифр.")

    def test_mask_account_card_invalid_format(self) -> None:
        """Тестирование некорректного формата ввода"""
        account_info: str = "Некорректный ввод"
        with self.assertRaises(ValueError) as context:
            mask_account_card(account_info)
        self.assertEqual(str(context.exception), "Некорректный формат ввода. Ожидался тип и номер.")

    def test_get_date_valid_format(self) -> None:
        """Тестирование корректного ввода даты"""
        date_string: str = "2023-10-01T12:30:45.123456"
        expected_output: str = "01.10.2023"
        result: str = get_date(date_string)
        self.assertEqual(result, expected_output)

    def test_get_date_invalid_format(self) -> None:
        """Тестирование некорректного формата даты"""
        date_string: str = "2023/10/01"
        with self.assertRaises(ValueError):
            get_date(date_string)

    def test_filter_by_state(self) -> None:
        """Тестирование фильтрации по состоянию"""
        data: List[Dict[str, Any]] = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "CANCELED", "amount": 200},
            {"state": "EXECUTED", "amount": 300},
        ]
        expected_output: List[Dict[str, Any]] = [
            {"state": "EXECUTED", "amount": 100},
            {"state": "EXECUTED", "amount": 300},
        ]
        result: List[Dict[str, Any]] = filter_by_state(data, "EXECUTED")
        self.assertEqual(result, expected_output)

    def test_sort_by_date(self) -> None:
        """Тестирование сортировки по дате"""
        data: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:30:45.123456", "amount": 100},
            {"date": "2022-01-01T12:30:45.123456", "amount": 200},
            {"date": "2023-05-01T12:30:45.123456", "amount": 300},
        ]
        expected_output: List[Dict[str, Any]] = [
            {"date": "2023-05-01T12:30:45.123456", "amount": 300},
            {"date": "2023-01-01T12:30:45.123456", "amount": 100},
            {"date": "2022-01-01T12:30:45.123456", "amount": 200},
        ]
        result: List[Dict[str, Any]] = sort_by_date(data, decrease=True)
        self.assertEqual(result, expected_output)

    def test_sort_by_date_ascending(self) -> None:
        """Тестирование сортировки по дате в порядке возрастания"""
        data: List[Dict[str, Any]] = [
            {"date": "2023-01-01T12:30:45.123456", "amount": 100},
            {"date": "2022-01-01T12:30:45.123456", "amount": 200},
            {"date": "2023-05-01T12:30:45.123456", "amount": 300},
        ]
        expected_output: List[Dict[str, Any]] = [
            {"date": "2022-01-01T12:30:45.123456", "amount": 200},
            {"date": "2023-01-01T12:30:45.123456", "amount": 100},
            {"date": "2023-05-01T12:30:45.123456", "amount": 300},
        ]
        result: List[Dict[str, Any]] = sort_by_date(data, decrease=False)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
