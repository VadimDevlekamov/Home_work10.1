import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "masks.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Убираем все пробелы из номера карты и возвращаем замаскированный номер."""
    card_number = card_number.replace(" ", "")

    try:
        if len(card_number) != 16 or not card_number.isdigit():
            raise ValueError("Номер карты должен состоять из 16 цифр")

        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.debug(f"Замаскированный номер карты: {masked_number}")
        return masked_number

    except ValueError as e:
        logger.error(f"Ошибка в get_mask_card_number: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Убираем все пробелы из номера счета и возвращаем замаскированный номер."""
    account_number = account_number.replace(" ", "")

    try:
        if len(account_number) < 4 or not account_number.isdigit():
            raise ValueError("Номер счета должен состоять только из цифр и содержать как минимум 4 цифры")

        masked_account = f"**{account_number[-4:]}"
        logger.debug(f"Замаскированный номер счета: {masked_account}")
        return masked_account

    except ValueError as e:
        logger.error(f"Ошибка в get_mask_account: {e}")
        raise