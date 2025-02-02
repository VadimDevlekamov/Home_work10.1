import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"


def convert_transaction_to_rub(transaction: dict) -> float:
    currency = transaction.get("currency")
    amount = transaction.get("amount")

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError("Unsupported currency")

    response = requests.get(f"{BASE_URL}latest?base={currency}", headers={"apikey": API_KEY})

    if response.status_code != 200:
        return 0.0

    data = response.json()
    if currency == "USD":
        return amount * data["rates"]["RUB"]
    elif currency == "EUR":
        return amount * data["rates"]["RUB"]
