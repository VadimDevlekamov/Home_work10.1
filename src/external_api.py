import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/"


def convert_transaction_to_rub(transaction: dict) -> float:
    '''Доступ к вложенному словарю'''
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

    response = requests.get(f"{BASE_URL}latest?base={currency_code}", headers={"apikey": API_KEY})

    if response.status_code != 200:
        return 0.0

    data = response.json()

    return amount * data["rates"]["RUB"]