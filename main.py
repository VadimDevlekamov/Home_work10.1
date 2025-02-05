from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

"""Импортируем функции из пакета src.widget"""
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

"""Импортируем функции из пакета src.processing"""
# Пример входных данных
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции фильтрации
executed_transactions = filter_by_state(transactions)
print("Executed transactions:")
print(executed_transactions)

# Сортировка отфильтрованных транзакций по дате в порядке убывания
sorted_executed_transactions = sort_by_date(executed_transactions)
print("\nExecuted transactions sorted by date (decrease):")
print(sorted_executed_transactions)

# Вызов функции фильтрации для 'CANCELED'
canceled_transactions = filter_by_state(transactions, state="CANCELED")
print("\nCanceled transactions:")
print(canceled_transactions)

# Сортировка отфильтрованных транзакций по дате в порядке убывания
sorted_canceled_transactions = sort_by_date(canceled_transactions)
print("\nCanceled transactions sorted by date (decrease):")
print(sorted_canceled_transactions)

# Сортировка всех транзакций по дате
sorted_all_transactions = sort_by_date(transactions)
print("\nAll transactions sorted by date (decrease):")
print(sorted_all_transactions)

