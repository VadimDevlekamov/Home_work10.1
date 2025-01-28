# Модуль генераторов транзакций

Данный модуль содержит функции для фильтрации транзакций по валюте, извлечения описаний транзакций и генерации номеров банковских карт.

## Установка

Убедитесь, что у вас установлен `pytest` для запуска тестов:
bash pip install pytest

**Проект Виджет банковских операций клиента  - это проект для удобства 
пользования картами и счетами клиентом.**

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

# Декоратор логирования `log`

## Установка

Чтобы использовать этот декоратор, просто скопируйте файл с декоратором в ваш проект или установите его с помощью пакетного менеджера, если он доступен.

## Использование

### Импорт

Сначала импортируйте декоратор в вашем коде:
python from your_module import log # Замените your_module на имя вашего модуля

### Применение декоратора

Вы можете применить декоратор `log` к любой функции, чтобы автоматически журналировать ее вызовы и результаты.

#### Пример использования
python
@log() # Логирует информацию в стандартный вывод def add(a: int, b: int) -> int: return a + b

result = add(5, 3)

В логах будет:
"Вызов функции add с аргументами: args=(5, 3), kwargs={}"
"Функция add вернула результат: 8"

### Логирование в файл

Если вы хотите сохранять логи в файл, можно передать имя файла в декоратор:
python
@log(filename='app.log') def divide(a: float, b: float) -> float: return a / b

try: result = divide(10, 2) except ZeroDivisionError: pass # Лог ошибки будет записан в файл ```

Функциональность
Логирует:
Входные параметры функции.
Возвращаемый результат функции.
Исключения, если они возникают во время выполнения.
Формат логов
Логи записываются в следующем формате: YYYY-MM-DD HH:MM:SS - LEVEL - Сообщение

Обработка ошибок
Если функция вызывает исключение, декоратор фиксирует сообщение об ошибке и входные параметры, а затем повторно вызывает исключение. Это позволяет сохранить поведение функции при возникновении ошибок.
