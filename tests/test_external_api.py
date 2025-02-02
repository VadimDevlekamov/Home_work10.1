import unittest
from unittest.mock import patch

from src.external_api import convert_transaction_to_rub


class TestCurrencyConverter(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_convert_usd_to_rub(self, mock_get):
        """Тест конвертации USD в RUB."""
        transaction = {"amount": 100.0, "currency": "USD"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 7500.0)

    @patch("src.external_api.requests.get")
    def test_convert_eur_to_rub(self, mock_get):
        """Тест конвертации EUR в RUB."""
        transaction = {"amount": 100.0, "currency": "EUR"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"RUB": 85.0}}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 8500.0)

    def test_convert_rub_to_rub(self):
        """Тест конвертации RUB в RUB."""
        transaction = {"amount": 100.0, "currency": "RUB"}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch("src.external_api.requests.get")
    def test_api_failure(self, mock_get):
        """Тест на случай ошибки API."""
        transaction = {"amount": 100.0, "currency": "USD"}
        mock_get.return_value.status_code = 404

        result = convert_transaction_to_rub(transaction)

        self.assertEqual(result, 0.0)

    def test_unsupported_currency(self):
        """Тест на неподдерживаемую валюту."""
        transaction = {"amount": 100.0, "currency": "JPY"}

        with self.assertRaises(ValueError):
            convert_transaction_to_rub(transaction)


if __name__ == "__main__":
    unittest.main()
