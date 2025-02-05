import logging
from typing import Generator

import pytest
from _pytest.logging import LogCaptureFixture

from src.decorators import log


@pytest.fixture(autouse=True)
def caplog(caplog: LogCaptureFixture) -> Generator[LogCaptureFixture, None, None]:
    """Фикстура для настройки логирования перед каждым тестом."""
    caplog.set_level(logging.INFO)
    yield caplog
    caplog.clear()


@log()
def successful_function(a: int, b: int) -> int:
    """Функция, возвращающая сумму двух чисел."""
    return a + b


@log()
def function_with_error(a: float, b: float) -> float:
    """Функция, выполняющая деление, может вызвать ошибку деления на ноль."""
    return a / b


# Тесты
def test_log_success(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование успешного вызова функции."""
    successful_function(5, 2)

    assert "Вызов функции successful_function с аргументами: args=(5, 2), kwargs={}" in caplog.text
    assert "Функция successful_function вернула результат: 7" in caplog.text


def test_log_exception(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование исключения при вызове функции."""
    with pytest.raises(ZeroDivisionError):
        function_with_error(10, 0)

    assert "Ошибка в функции function_with_error: ZeroDivisionError" in caplog.text
    assert "Вызов функции function_with_error с аргументами: args=(10, 0), kwargs={}" in caplog.text


def test_log_another_exception(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование другого исключения при вызове функции."""
    with pytest.raises(TypeError):
        successful_function(5, "a")

    assert "Ошибка в функции successful_function: TypeError" in caplog.text
    assert "Вызов функции successful_function с аргументами: args=(5, 'a'), kwargs={}" in caplog.text
