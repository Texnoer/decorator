
from datetime import datetime


# Написать декоратор - логгер. Он записывает в файл дату и время
# вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
def log_decorator(foo):
    def new_foo(*args, **kwargs):
        time = datetime.now()
        start = time.strftime("%Y-%m-%d-%H.%M.%S")
        result = foo(*args, **kwargs)
        logs = f'Дата и время вызова функции: {start};\nИмя функции: {foo.__name__};\nАргументы: {args} и {kwargs};\nРезультат: {result}.'
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"{logs}")
        return result
    return new_foo


@log_decorator
def foo(a, b):
    return a * b


if __name__ == '__main__':
    foo(3, 3)