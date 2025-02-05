from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions import read_transactions_from_csv, read_transactions_from_excel


def test_read_transactions_from_csv():
    mock_csv_data = "date,amount,description\n2023-01-01,100,Test transaction"

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        transactions = read_transactions_from_csv("dummy_path.csv")
        assert len(transactions) == 1
        assert transactions[0]["amount"] == "100"


def test_read_transactions_from_excel():
    mock_df = pd.DataFrame({"date": ["2023-01-01"], "amount": [100], "description": ["Test transaction"]})
    with patch("pandas.read_excel", return_value=mock_df):
        transactions = read_transactions_from_excel("dummy_path.xlsx")
        assert len(transactions) == 1
        assert transactions[0]["amount"] == 100
