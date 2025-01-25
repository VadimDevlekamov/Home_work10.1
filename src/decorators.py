import functools
import logging
import sys
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    logger = logging.getLogger('FunctionLogger')
    logger.setLevel(logging.DEBUG)

    # Убедитесь, что обработчики очищены
    if not logger.hasHandlers():
        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info(f'Вызов функции: {func.__name__} с аргументами: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)
                logger.info(f'{func.__name__} ok. Результат: {result}')
                return result
            except Exception as e:
                logger.error(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}')
                raise

        return wrapper

    return decorator