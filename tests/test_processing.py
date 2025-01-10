import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-03-11'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-03-09'},
        {'id': 4, 'state': 'PENDING', 'date': '2023-03-10'},
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-03-12'}
    ]

@pytest.fixture
def mixed_date_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 2, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 3, 'state': 'CANCELLED', 'date': '2023-03-11'},
        {'id': 4, 'state': 'CANCELLED', 'date': '2023-03-12'}
    ]

# Тесты для filter_by_state
def test_filter_by_state_executed(test_data):
    result = filter_by_state(test_data, 'EXECUTED')
    expected = [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-03-09'}
    ]
    assert result == expected

def test_filter_by_state_cancelled(test_data):
    result = filter_by_state(test_data, 'CANCELLED')
    expected = [
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-03-11'},
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-03-12'}
    ]
    assert result == expected

def test_filter_by_state_no_results(test_data):
    result = filter_by_state(test_data, 'COMPLETED')
    assert result == []

@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', [{'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
                   {'id': 3, 'state': 'EXECUTED', 'date': '2023-03-09'}]),
    ('CANCELLED', [{'id': 2, 'state': 'CANCELLED', 'date': '2023-03-11'},
                     {'id': 5, 'state': 'CANCELLED', 'date': '2023-03-12'}]),
    ('PENDING', [{'id': 4, 'state': 'PENDING', 'date': '2023-03-10'}]),  # Изменяем ожидаемое значение
    ('COMPLETED', [])
])
def test_filter_by_state_parametrized(test_data, state, expected):
    result = filter_by_state(test_data, state)
    assert result == expected

# Тесты для sort_by_date
def test_sort_by_date_ascending(test_data):
    result = sort_by_date(test_data, decrease=False)
    expected = [
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-03-09'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 4, 'state': 'PENDING', 'date': '2023-03-10'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-03-11'},
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-03-12'}
    ]
    assert result == expected

def test_sort_by_date_descending(test_data):
    result = sort_by_date(test_data, decrease=True)
    expected = [
        {'id': 5, 'state': 'CANCELLED', 'date': '2023-03-12'},
        {'id': 2, 'state': 'CANCELLED', 'date': '2023-03-11'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-03-10'},
        {'id': 4, 'state': 'PENDING', 'date': '2023-03-10'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-03-09'}
    ]
    assert result == expected

def test_sort_by_date_identical_dates(mixed_date_data):
    result = sort_by_date(mixed_date_data, decrease=False)
    expected = sorted(mixed_date_data, key=lambda x: x['date'])
    assert result == expected

def test_sort_by_date_empty_list():
    result = sort_by_date([])
    assert result == []