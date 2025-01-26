import logging

import pytest
from _pytest.logging import LogCaptureFixture

from src.decorators import log  # Замените на реальный путь к вашему декоратору


# Настройка логирования для тестирования
@pytest.fixture(autouse=True)
def caplog(caplog: LogCaptureFixture) -> LogCaptureFixture:
    # Обнуляем ловушку лога перед каждым тестом
    caplog.set_level(logging.INFO)
    yield caplog
    caplog.clear()


# Пример функций для тестирования
@log()
def successful_function(a: int, b: int) -> int:
    return a + b


@log()
def function_with_error(a: float, b: float) -> float:
    return a / b  # Деление на ноль вызовет ошибку


# Тесты
def test_log_success(caplog: LogCaptureFixture) -> None:
    successful_function(5, 2)  # Успешный вызов функции

    # Проверяем, что вывод в логе содержит информацию об успешном выполнении
    assert "Вызов функции successful_function с аргументами: args=(5, 2), kwargs={}" in caplog.text
    assert "Функция successful_function вернула результат: 7" in caplog.text


def test_log_exception(caplog: LogCaptureFixture) -> None:
    with pytest.raises(ZeroDivisionError):
        function_with_error(10, 0)  # Дивидение на ноль вызовет ошибку

    # Проверяем, что вывод в логе содержит сообщение об ошибке
    assert "Ошибка в функции function_with_error: ZeroDivisionError" in caplog.text
    assert "Вызов функции function_with_error с аргументами: args=(10, 0), kwargs={}" in caplog.text


def test_log_another_exception(caplog: LogCaptureFixture) -> None:
    with pytest.raises(TypeError):
        successful_function(5, "a")  # Этот вызов приведет к ошибке типа

    # Проверяем, что вывод в логе содержит сообщение об ошибке
    assert "Ошибка в функции successful_function: TypeError" in caplog.text
    assert "Вызов функции successful_function с аргументами: args=(5, 'a'), kwargs={}" in caplog.text
