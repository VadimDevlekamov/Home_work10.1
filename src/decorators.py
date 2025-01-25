import functools
import logging
import sys

def log(filename=None):
    # Создаем и настраиваем логгер
    logger = logging.getLogger('FunctionLogger')
    logger.setLevel(logging.DEBUG)

    # Создаем обработчик
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логирование входных параметров
            logger.info(f'Вызов функции: {func.__name__}, аргументы: {args}, {kwargs}')
            try:
                result = func(*args, **kwargs)
                # Логирование результата
                logger.info(f'Функция: {func.__name__} завершилась успешно, результат: {result}')
                return result
            except Exception as e:
                # Логирование ошибки без трассировки стека
                logger.error(f'Ошибка в функции: {func.__name__}, аргументы: {args}, {kwargs}, ошибка: {str(e)}')
                raise  # Перекинем исключение дальше

        return wrapper

    return decorator


