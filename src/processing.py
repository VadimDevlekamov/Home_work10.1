from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Функция фильтрует список словарей по ключу 'state'.
    """


    return [item for item in data if item.get('state') == state]


