# Модуль генераторов транзакций

Данный модуль содержит функции для фильтрации транзакций по валюте, извлечения описаний транзакций и генерации номеров банковских карт.

## Установка

Убедитесь, что у вас установлен `pytest` для запуска тестов:
bash pip install pytest

## Функции

### `filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]`

Фильтрует транзакции по заданной валюте.

**Пример использования:**
python transactions = [...] # список транзакций usd_transactions = list(filter_by_currency(transactions, "USD"))

### `transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]`

Возвращает описания всех транзакций.

**Пример использования:**
python descriptions = list(transaction_descriptions(transactions))

### `card_number_generator(start: int, end: int) -> Iterator[str]`

Генерирует номера банковских карт в заданном диапазоне.

**Пример использования:**
python card_numbers = list(card_number_generator(1, 5))   
