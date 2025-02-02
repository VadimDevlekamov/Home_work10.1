import unittest
from unittest.mock import mock_open, patch

from src.utils import load_transactions_from_json


class TestLoadTransactions(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100.0, "currency": "RUB"}]')
    @patch("os.path.exists", return_value=True)
    def test_valid_json_file(self, mock_exists, mock_file):
        result = load_transactions_from_json("data/operations.json")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 100.0)

    @patch("os.path.exists", return_value=False)
    def test_file_not_found(self, mock_exists):
        result = load_transactions_from_json("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("os.path.exists", return_value=True)
    def test_empty_file(self, mock_exists, mock_file):
        result = load_transactions_from_json("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="not a json")
    @patch("os.path.exists", return_value=True)
    def test_invalid_json(self, mock_exists, mock_file):
        result = load_transactions_from_json("data/operations.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    @patch("os.path.exists", return_value=True)
    def test_non_list_json(self, mock_exists, mock_file):
        result = load_transactions_from_json("data/operations.json")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
