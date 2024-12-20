from .masks import get_mask_card_number, get_mask_account
import re


def mask_account_card(account_info: str) -> str:
    '''Функция определяющая тип и номер'''

    match = re.match(r"(.+?)\s+(\d+)", account_info)

    account_type = match.group(1).strip()  # Удаляем лишние пробелы
    account_number = match.group(2).strip()

    if account_type == "Счет":
        return f"{account_type} {get_mask_account(account_number)}"

    if len(account_number) == 16:
        return f"{account_type} {get_mask_card_number(account_number)}"
    else:
        raise ValueError("Неверный номер карты. Номер карты должен состоять из 16 цифр.")



