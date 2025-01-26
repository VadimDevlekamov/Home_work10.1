import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функции и их результатов."""

    # Настройка логирования
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                # Логируем входные параметры функции
                logging.info(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}")

                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем результат
                logging.info(f"Функция {func.__name__} вернула результат: {result}")
                return result
            except Exception as e:
                # Логируем ошибку и входные параметры
                logging.error(
                    f"Ошибка в функции {func.__name__}: {type(e).__name__}. "
                    f"Входные параметры: args={args}, kwargs={kwargs}"
                )
                logging.exception("Произошла ошибка")
                raise

        return wrapper

    return decorator
