import json
import logging
import os
from typing import Any, Dict, List

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(log_dir, "utils.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Чтение JSON-файла и возвращение списка словарей с данными о финансовых транзакциях."""
    logger.debug(f"Попытка загрузки транзакций из файла: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден: {file_path}")
        return []  # Если файл не найден

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            logger.warning(f"Файл пустой: {file_path}")
            return []  # Если файл пустой

        try:
            transactions = json.loads(content)
            if isinstance(transactions, list):
                logger.debug("Транзакции успешно загружены.")
                return transactions
            else:
                logger.error("Данные в файле не являются списком.")
                return []
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка чтения JSON: {e}")
            return []