import unittest

from src.widget import get_date, mask_account_card


class TestMaskingFunctions(unittest.TestCase):

    def test_mask_account_card_valid_account(self) -> None:
        """Тестирование корректного ввода счета"""
        account_info: str = "Счет 12345678901234567890"
        expected_output: str = "Счет **7890"
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


if __name__ == "__main__":
    unittest.main()
