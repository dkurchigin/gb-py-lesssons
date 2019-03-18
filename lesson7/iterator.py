import os


class LogReader:

    def __init__(self):
        self.files = []

        for file in os.listdir():
            if os.path.isdir(file):
                continue
            if file.startswith('log'):
                file_descriptor = open(file, encoding='UTF-8')
                self.files.append(file_descriptor)

        self.i = 0

    def __del__(self):
        for file_descriptor in self.files:
            file_descriptor.close()
        print('Файлы закрыты')

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.files):
            print(type(self.files[self.i]), "this")
            for line in self.files[self.i]:
                return line
            self.i += 1
        raise StopIteration  # Выбрасываем исключение


log_reader = LogReader()

# For запрашивает объект итератор
# Задача итератора вернуть объект, у которого есть метод __next__

for i in log_reader:
    print(i.strip())
