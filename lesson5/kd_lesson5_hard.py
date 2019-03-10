# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import re

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp - создает копию указаного файла")
    print("rm - удалить указаный файл")
    print("cd - сменить текущую директорию на указаную")
    print("ls - посмотреть путь, где вы находитесь")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def show_path():
    print("Вы находитесь здесь:")
    print(os.getcwd())


def remove_file():
    file = dir_name
    if not file:
        print("Необходимо указать имя файла вторым параметром")
        return
    try:
        if check_user_answer(file):
            os.remove(file)
            print("Удалил файл", file)
    except IsADirectoryError:
        print("{} не является файлом".format(file))
    except FileNotFoundError:
        print("Файл {} не существует".format(file))


def check_user_answer(file):
    print("Вы собираетесь удалить {}, вы согласны?".format(file))
    print("(Y)es | (N)o?")
    answer = input()

    pattern_for_yes = '(^[yY]$|^[yY][eE][sS]$)'
    if re.match(pattern_for_yes, answer):
        return True
    else:
        return False


def get_dir_for_change():
    dir_for_change = dir_name
    current_dir = os.getcwd()

    pattern_for_full_path = '^\/.*'
    try:
        if not re.match(pattern_for_full_path, dir_for_change):
            os.chdir("{}/{}".format(current_dir, dir_for_change))
        else:
            os.chdir(dir_for_change)
        show_path()
    except (NotADirectoryError, FileNotFoundError):
        print("Не могу перейти в директорию {}, её либо не существует, либо это файл, "
              "а не директория".format(dir_for_change))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": show_path,
    "rm": remove_file,
    "cd": get_dir_for_change
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
print("Укажите ключ help для получения справки")