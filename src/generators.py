from typing import List, Dict, Any, Iterator


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]:
    """Генератор, который фильтрует транзакции по валюте."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, возвращающий описания транзакций."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, создающий номера банковских карт."""
    for num in range(start, end + 1):
        yield f"{num:04d} {num:04d} {num:04d} {num:04d}"