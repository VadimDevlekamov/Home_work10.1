import pytest

from src.processing import filter_by_state, sort_by_date

# Тесты для функции filter_by_state
def test_filter_by_state_executed():
    data = [
        {"state": "EXECUTED"},
        {"state": "CANCELLED"},
        {"state": "EXECUTED"}
    ]
    expected = [
        {"state": "EXECUTED"},
        {"state": "EXECUTED"}
    ]
    result = filter_by_state(data, state="EXECUTED")
    assert result == expected


def test_filter_by_state_cancelled():
    data = [
        {"state": "EXECUTED"},
        {"state": "CANCELLED"},
        {"state": "EXECUTED"}
    ]
    expected = [
        {"state": "CANCELLED"}
    ]
    result = filter_by_state(data, state="CANCELLED")
    assert result == expected


def test_filter_by_state_no_results():
    data = [
        {"state": "EXECUTED"},
        {"state": "CANCELLED"},
    ]
    expected = []
    result = filter_by_state(data, state="PENDING")
    assert result == expected


@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{"state": "EXECUTED"}, {"state": "EXECUTED"}]),
    ("CANCELLED", [{"state": "CANCELLED"}]),
    ("PENDING", []),
    ("COMPLETED", [])
])
def filter_by_state(data, state):
    return [item for item in data if item['state'] == state]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [{"state": "EXECUTED"}, {"state": "EXECUTED"}]),
    ("CANCELLED", [{"state": "CANCELLED"}]),
    ("PENDING", [{"state": "PENDING"}]),  # Теперь ожидаем, что вернется [{'state': 'PENDING'}]
    ("COMPLETED", [{"state": "COMPLETED"}])  # Теперь ожидаем, что вернется [{'state': 'COMPLETED'}]
])
def test_filter_by_state_parametrized(state, expected):
    data = [
        {"state": "EXECUTED"},
        {"state": "CANCELLED"},
        {"state": "EXECUTED"},
        {"state": "PENDING"},
        {"state": "COMPLETED"}
    ]
    result = filter_by_state(data, state=state)
    assert result == expected


def test_sort_by_date_descending():
    data = [
        {"date": "2023-01-02T12:00:00"},
        {"date": "2023-01-01T12:00:00"},
        {"date": "2023-01-03T12:00:00"},
    ]
    expected = [
        {"date": "2023-01-03T12:00:00"},
        {"date": "2023-01-02T12:00:00"},
        {"date": "2023-01-01T12:00:00"},
    ]
    result = sort_by_date(data)
    assert result == expected


def test_sort_by_date_identical_dates():
    data = [
        {"date": "2023-01-01T12:00:00"},
        {"date": "2023-01-01T12:00:00"},
    ]
    expected = [
        {"date": "2023-01-01T12:00:00"},
        {"date": "2023-01-01T12:00:00"},
    ]
    result = sort_by_date(data)
    assert result == expected


def test_sort_by_date_empty_list():
    data = []
    expected = []
    result = sort_by_date(data)
    assert result == expected