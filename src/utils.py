import json
import os
from typing import Any, Dict, List


def load_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """Чтение JSON-файла и возвращение списка словарей с данными о финансовых транзакциях."""
    if not os.path.exists(file_path):
        return []  # Если файл не найден

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if not content:
            return []  # Если файл пустой

        try:
            transactions = json.loads(content)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
        except json.JSONDecodeError:
            return []
