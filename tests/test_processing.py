import unittest

from src.processing import filter_by_state, get_date, mask_account_card, sort_by_date


class TestProcessingFunctions(unittest.TestCase):

    def test_mask_account_card(self):
        """Тест для корректных данных"""
        self.assertEqual(mask_account_card("Счет 12345678901234567890"), "Счет 1234************890")
        self.assertEqual(mask_account_card("Карта 1234567812345678"), "Карта ************5678")

        # Тест для некорректного формата ввода
        with self.assertRaises(ValueError) as context:
            mask_account_card("Некорректные данные")
        self.assertEqual(str(context.exception), "Некорректный формат ввода. Ожидался тип и номер.")

        # Тест для неверного номера карты
        with self.assertRaises(ValueError) as context:
            mask_account_card("Карта 123")
        self.assertEqual(str(context.exception), "Неверный номер карты. Номер карты должен состоять из 16 цифр.")

    def test_get_date(self):
        """Тест для корректного преобразования даты"""
        self.assertEqual(get_date("2023-10-10T14:30:00"), "10.10.2023")

        # Тест для некорректного формата даты
        with self.assertRaises(ValueError):
            get_date("Некорректная дата")

    def test_filter_by_state(self):
        """Тест фильтрации по состоянию"""
        data = [{"state": "EXECUTED"}, {"state": "PENDING"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]
        filtered_data = filter_by_state(data)
        self.assertEqual(len(filtered_data), 2)
        self.assertTrue(all(item["state"] == "EXECUTED" for item in filtered_data))

    def test_sort_by_date(self):
        # Тест сортировки по дате
        data = [{"date": "2023-10-10T14:30:00"}, {"date": "2023-09-10T14:30:00"}, {"date": "2023-11-10T14:30:00"}]
        sorted_data = sort_by_date(data)
        self.assertEqual(sorted_data[0]["date"], "2023-11-10T14:30:00")
        self.assertEqual(sorted_data[-1]["date"], "2023-09-10T14:30:00")

        # Тест сортировки по дате в обратном порядке
        sorted_data_desc = sort_by_date(data, decrease=False)
        self.assertEqual(sorted_data_desc[0]["date"], "2023-09-10T14:30:00")
        self.assertEqual(sorted_data_desc[-1]["date"], "2023-11-10T14:30:00")


if __name__ == "__main__":
    unittest.main()
