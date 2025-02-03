import sys
import os
import unittest
from unittest.mock import patch
from src.external_api import convert_transaction_to_rub

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


class TestCurrencyConverter(unittest.TestCase):
    @patch("external_api.requests.get")
    def test_convert_usd_to_rub(self, mock_get):
        """Тест конвертации USD в RUB."""
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"RUB": 7500}}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 750000.0)  # 100 USD * 7500 RUB

    @patch("external_api.requests.get")
    def test_convert_eur_to_rub(self, mock_get):
        """Тест конвертации EUR в RUB."""
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"rates": {"RUB": 8500}}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 850000.0)  # 100 EUR * 8500 RUB

    def test_convert_rub_to_rub(self):
        """Тест конвертации RUB в RUB."""
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}

        result = convert_transaction_to_rub(transaction)
        self.assertEqual(result, 100.0)

    @patch("external_api.requests.get")
    def test_api_failure(self, mock_get):
        """Тест на случай ошибки API."""
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
        mock_get.return_value.status_code = 404

        result = convert_transaction_to_rub(transaction)

        self.assertEqual(result, 0.0)

    def test_unsupported_currency(self):
        """Тест на неподдерживаемую валюту."""
        transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "JPY"}}}

        with self.assertRaises(ValueError):
            convert_transaction_to_rub(transaction)

    def test_invalid_amount(self):
        """Тест на некорректный формат суммы."""
        transaction = {"operationAmount": {"amount": "invalid_amount", "currency": {"code": "USD"}}}

        with self.assertRaises(ValueError):
            convert_transaction_to_rub(transaction)


if __name__ == "__main__":
    unittest.main()
