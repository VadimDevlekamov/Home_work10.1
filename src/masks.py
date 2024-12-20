from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """Убираем все пробелы из номера карты и возвращаем замаскированный номер"""
    card_number = card_number.replace(" ", "")

    # Проверяем, что номер карты состоит из 16 цифр
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    # Формируем маску
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    return masked_number


def get_mask_account(account_number: str) -> str:
    """Убираем все пробелы из номера счета и возвращаем замаскированный номер"""
    account_number = account_number.replace(" ", "")

    # Проверяем, что номер счета состоит из достаточного количества цифр
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр и содержать как минимум 4 цифры")

    # Формируем маску
    masked_account = f"**{account_number[-4:]}"

    return masked_account
