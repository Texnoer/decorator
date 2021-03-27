from datetime import datetime


# Написать декоратор из п.1, но с параметром – путь к логам.
def way_decorator(files):
    def log_decorator(foo):
        def new_foo(*args, **kwargs):
            time = datetime.now()
            start = time.strftime("%Y-%m-%d-%H.%M.%S")
            result = foo(*args, **kwargs)
            logs = f'Дата и время вызова функции: {start};\nИмя функции: {foo.__name__};\nАргументы: {args} и {kwargs};\nРезультат: {result}.'
            with open(files, 'a', encoding='utf-8') as file:
                file.write(f"{logs}")
            return result
        return new_foo
    return log_decorator

@way_decorator('logs')
def foo(a, b):
    return a * b


if __name__ == '__main__':
    foo(10, 3)