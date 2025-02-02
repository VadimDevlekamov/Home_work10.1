import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функции и их результатов."""

    encoding = "utf-8"  # Указываем кодировку

    if filename:
        logging.basicConfig(
            filename=filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            encoding=encoding,
        )
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding=encoding)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logging.info(f"Вызов функции {func.__name__} с аргументами: args={args}, kwargs={kwargs}")

                result = func(*args, **kwargs)

                logging.info(f"Функция {func.__name__} вернула результат: {result}")
                return result
            except Exception as e:
                logging.error(
                    f"Ошибка в функции {func.__name__}: {type(e).__name__}. "
                    f"Входные параметры: args={args}, kwargs={kwargs}"
                )
                logging.exception("Произошла ошибка")
                raise

        return wrapper

    return decorator
