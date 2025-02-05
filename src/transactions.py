import csv
import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """Читает финансовые операции из CSV файла и возвращает список словарей с транзакциями."""
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            transactions.append(row)
    return transactions

def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """Читает финансовые операции из Excel файла и возвращает список словарей с транзакциями."""
    transactions = []
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        transactions.append(row.to_dict())
    return transactions


