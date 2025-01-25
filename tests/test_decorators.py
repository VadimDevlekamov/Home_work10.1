import pytest
import logging
from io import StringIO
import sys

# Импортируйте ваш декоратор
from src.decorators import log  # Замените "your_module" на имя вашего модуля, где объявлен декоратор.

logger = logging.getLogger('FunctionLogger')

@log()
def successful_function(arg1, arg2):
    return arg1 + arg2

@log()
def function_with_error(arg1, arg2):
    return arg1 / arg2

@pytest.fixture
def capsys_fixture(capsys):
    # Удаляем обработчики, чтобы избежать дублирования вывода
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)
    yield stream  # Возвращаем поток для проверки

def test_successful_function(capsys_fixture):
    result = successful_function(2, 3)
    assert result == 5

    # Проверка логов
    logs = capsys_fixture.getvalue().strip().split('\n')
    assert len(logs) == 2
    assert 'Вызов функции: successful_function' in logs[0]
    assert 'successful_function ok. Результат: 5' in logs[1]

def test_function_with_error(capsys_fixture):
    with pytest.raises(ZeroDivisionError):
        function_with_error(1, 0)

    # Проверка логов
    logs = capsys_fixture.getvalue().strip().split('\n')
    assert len(logs) == 2
    assert 'Вызов функции: function_with_error' in logs[0]
    assert 'function_with_error error: ZeroDivisionError' in logs[1]