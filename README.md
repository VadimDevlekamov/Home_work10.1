# Маскирование Номеров и Логирование

Этот проект предоставляет функциональность для маскирования номеров банковских карт и счетов, а также включает функции для работы с транзакциями и декоратор логирования для отслеживания вызовов функции.

## Установка

Скопируйте файл в вашу рабочую директорию или добавьте его в ваш проект. Убедитесь, что у вас установлены все необходимые библиотеки.

## Функции

### 1. Маскирование Номеров

#### `get_mask_card_number(card_number: str) -> str`

Убирает все пробелы из номера карты и возвращает замаскированный номер. Номер карты должен состоять из 16 цифр.

**Параметры:**
- `card_number` (str): Номер карты в строковом формате.

**Возвращает:**
- Замаскированный номер карты в формате `XXXX XX** **** XXXX`.

#### `get_mask_account(account_number: str) -> str`

Убирает все пробелы из номера счета и возвращает замаскированный номер. Номер счета должен содержать как минимум 4 цифры.

**Параметры:**
- `account_number` (str): Номер счета в строковом формате.

**Возвращает:**
- Замаскированный номер счета в формате `**XXXX`.

### 2. Преобразование Дат

#### `get_date(date_string: str) -> str`

Преобразует дату из формата `'YYYY-MM-DDTHH:MM:SS.ffffff'` в формат `'ДД.ММ.ГГГГ'`.

**Параметры:**
- `date_string` (str): Дата в строковом формате.

**Возвращает:**
- Дата в формате `'ДД.ММ.ГГГГ'`.

### 3. Фильтрация и Сортировка Транзакций

#### `filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]`

Фильтрует список транзакций по ключу `'state'`.

**Параметры:**
- `data` (List[Dict]): Список транзакций.
- `state` (str): Состояние для фильтрации (по умолчанию - "EXECUTED").

**Возвращает:**
- Отфильтрованный список транзакций.

#### `sort_by_date(data: List[Dict[str, str]], decrease: bool = True) -> List[Dict[str, str]]`

Сортирует список транзакций по ключу `'date'`.

**Параметры:**
- `data` (List[Dict]): Список транзакций.
- `decrease` (bool): Если True, сортирует по убыванию, иначе - по возрастанию.

**Возвращает:**
- Отсортированный список транзакций.

### 4. Генерация Номеров Транзакций

#### `filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Iterator[Dict[str, Any]]`

Генератор, который фильтрует транзакции по указанной валюте.

**Параметры:**
- `transactions` (List[Dict]): Список транзакций.
- `currency` (str): Код валюты для фильтрации.

#### `transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]`

Генератор, возвращающий описания транзакций.

**Параметры:**
- `transactions` (List[Dict]): Список транзакций.

### 5. Логирование

#### `log(filename: Optional[str] = None) -> Callable`

Декоратор для логирования вызовов функции и их результатов. Можно указать имя файла для логов.

**Параметры:**
- `filename` (Optional[str]): Имя файла для хранения логов. Если None, использует стандартный вывод.

**Пример использования:**
python
@log('app.log') def my_function():

# Ваша функция

## Пример Использования
python if __name__ == "__main__": card_number = "1234 5678 1234 5678" print(get_mask_card_number(card_number)) # "1234 56** **** 5678"
account_number = "123456789012"
print(get_mask_account(account_number))  # "**0012"

date_string = "2023-10-01T12:30:45.123456"
print(get_date(date_string))  # "01.10.2023"
