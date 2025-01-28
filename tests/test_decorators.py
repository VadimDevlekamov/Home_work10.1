import logging
from typing import Generator  # Импортируем Generator
import pytest
from _pytest.logging import LogCaptureFixture
from src.decorators import log


# Настройка логирования для тестирования
@pytest.fixture(autouse=True)
def caplog(caplog: LogCaptureFixture) -> Generator[LogCaptureFixture, None, None]:
    """Фикстура для настройки логирования перед каждым тестом."""
    # Обнуляем ловушку лога перед каждым тестом
    caplog.set_level(logging.INFO)
    yield caplog
    caplog.clear()


# Пример функций для тестирования
@log()
def successful_function(a: int, b: int) -> int:
    """Функция, возвращающая сумму двух чисел."""
    return a + b


@log()
def function_with_error(a: float, b: float) -> float:
    """Функция, выполняющая деление, может вызвать ошибку деления на ноль."""
    return a / b  # Деление на ноль вызовет ошибку


# Тесты
def test_log_success(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование успешного вызова функции."""
    successful_function(5, 2)  # Успешный вызов функции

    # Проверяем, что вывод в логе содержит информацию об успешном выполнении
    assert "Вызов функции successful_function с аргументами: args=(5, 2), kwargs={}" in caplog.text
    assert "Функция successful_function вернула результат: 7" in caplog.text


def test_log_exception(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование исключения при вызове функции."""
    with pytest.raises(ZeroDivisionError):
        function_with_error(10, 0)  # Деление на ноль вызовет ошибку

    # Проверяем, что вывод в логе содержит сообщение об ошибке
    assert "Ошибка в функции function_with_error: ZeroDivisionError" in caplog.text
    assert "Вызов функции function_with_error с аргументами: args=(10, 0), kwargs={}" in caplog.text


def test_log_another_exception(caplog: LogCaptureFixture) -> None:
    """Тестируем логирование другого исключения при вызове функции."""
    with pytest.raises(TypeError):
        successful_function(5, "a")  # Этот вызов приведет к ошибке типа

    # Проверяем, что вывод в логе содержит сообщение об ошибке
    assert "Ошибка в функции successful_function: TypeError" in caplog.text
    assert "Вызов функции successful_function с аргументами: args=(5, 'a'), kwargs={}" in caplog.text
