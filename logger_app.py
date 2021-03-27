from datetime import datetime
import json
import hashlib

def log_decorator(foo):
    def new_foo(*args, **kwargs):
        time = datetime.now()
        start = time.strftime("%Y-%m-%d-%H.%M.%S")
        result = foo(*args, **kwargs)
        logs = f'Дата и время вызова функции: {start};\nИмя функции: {foo.__name__};\nАргументы: {args} и {kwargs};\nРезультат: {result}'
        with open('logs_file.txt', 'a', encoding='utf-8') as file:
            file.write(f"{logs}")
        return result
    return new_foo



class Iteration_json:
    def __init__(self, file):
        self.file = file
        self.start = -1
        self.len_f = len(self.file)
        f_j = open('countries.json', encoding='utf-8')
        self.file_json = json.load(f_j)

    def __iter__(self):
        return self

    @log_decorator
    def __next__(self):
        self.start += 1
        try:
            country = self.file_json[self.start]['name']['common']
        except IndexError:
            raise StopIteration

        country_dash = country.replace(' ', '_')
        unification = country + ' - ' + wikipedia_link + country_dash + '\n'
        return unification

    def download(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as new_file:
            for data in self:
                new_file.write(data)

def hashlib_md5 (file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for chunk in file:
            code_list= hashlib.md5(chunk.encode())
            yield code_list.hexdigest()

if __name__ == '__main__':
    wikipedia_link = 'https://en.wikipedia.org/wiki/'
    downloader = Iteration_json('contries.json')
    downloader.download('countries_links.txt')
    for result in hashlib_md5('countries_links.txt'):
        print(result)
