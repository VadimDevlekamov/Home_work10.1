import re
from datetime import datetime
from typing import Dict, List

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция определяющая тип и номер."""
    match = re.match(r"(.+?)\s+(\d+)", account_info)
    if not match:
        raise ValueError("Некорректный формат ввода. Ожидался тип и номер.")

    account_type: str = match.group(1).strip()
    account_number: str = match.group(2).strip()

    if account_type == "Счет":
        return f"{account_type} {get_mask_account(account_number)}"

    if len(account_number) == 16:
        return f"{account_type} {get_mask_card_number(account_number)}"
    else:
        raise ValueError("Неверный номер карты. Номер карты должен состоять из 16 цифр.")


def get_date(date_string: str) -> str:
    """Преобразуем дату из формата 'YYYY-MM-DDTHH:MM:SS.ffffff' в формат 'ДД.ММ.ГГГГ'."""
    dt: datetime = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")


def filter_by_state(data: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Функция фильтрует список словарей по ключу 'state'."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, str]], decrease: bool = True) -> List[Dict[str, str]]:
    """Функция сортирует список словарей по ключу 'date'."""
    return sorted(data, key=lambda operations: operations["date"], reverse=decrease)
