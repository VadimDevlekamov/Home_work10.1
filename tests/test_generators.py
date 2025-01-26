from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(transactions: List[Dict[str, Any]]) -> None:
    """Тест правильной фильтрации USD"""
    usd_transactions: List[Dict[str, Any]] = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 3
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in usd_transactions)

    # Тест фильтрации, когда валюты отсутствуют
    rub_transactions: List[Dict[str, Any]] = list(filter_by_currency(transactions, "RUB"))
    assert len(rub_transactions) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "RUB" for tx in rub_transactions)

    # Тест на пустой список
    empty_transactions: List[Dict[str, Any]] = []
    empty_result: List[Dict[str, Any]] = list(filter_by_currency(empty_transactions, "USD"))
    assert empty_result == []


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    """Тест возвращения описаний транзакций"""
    descriptions: List[str] = list(transaction_descriptions(transactions))
    assert len(descriptions) == 5
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    # Тест с пустым списком транзакций
    empty_descriptions: List[str] = list(transaction_descriptions([]))
    assert empty_descriptions == []


def test_card_number_generator() -> None:
    """Тест генерации номеров карт"""
    card_numbers: List[str] = list(card_number_generator(1, 5))
    assert len(card_numbers) == 5
    assert card_numbers == [
        "0001 0001 0001 0001",
        "0002 0002 0002 0002",
        "0003 0003 0003 0003",
        "0004 0004 0004 0004",
        "0005 0005 0005 0005",
    ]

    # Тест генератора с одним значением
    single_number: List[str] = list(card_number_generator(10, 10))
    assert single_number == ["0010 0010 0010 0010"]

    # Тест генератора с пустым диапазоном
    empty_range: List[str] = list(card_number_generator(5, 1))
    assert empty_range == []
