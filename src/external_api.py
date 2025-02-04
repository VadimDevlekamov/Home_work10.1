import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"


def convert_transaction_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции в рубли (RUB)."""
    operation_amount = transaction.get("operationAmount", {})

    amount_str = operation_amount.get("amount", "0.0")
    currency_code = operation_amount.get("currency", {}).get("code", "")

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError("Invalid amount value")

    if currency_code == "RUB":
        return amount

    if currency_code not in ["USD", "EUR"]:
        raise ValueError("Unsupported currency")

    try:
        response = requests.get(f"{BASE_URL}latest?base={currency_code}", headers={"apikey": API_KEY})

        if response.status_code == 200:
            data = response.json()
            if "rates" in data and "RUB" in data["rates"]:
                return amount * data["rates"]["RUB"]

    except requests.RequestException:
        raise RuntimeError("Failed to get exchange rate")

    return 0.0
