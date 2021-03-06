import os
import re
import sys
import shutil

def programm_title():
    print("************************")
    print("*GB/Python/Lesson5/EASY*")
    print("************************")


def print_files_on_dir(directory="."):
    files = os.listdir(directory)
    print ('===Список файлов===')
    for file in files:
        if os.path.isdir(file):
            print(file, "<-- директория")
        else:
            print(file)
    print ('===================')
    print ('')


def make_dir(path="."):
    try:
        os.mkdir(path)
        print("Создал директорию", path)
    except FileExistsError:
        print("Не могу создать директорию \"{}\", т.к. такая директория уже существует".format(path))


def remove_dirs(pattern, path="."):
    files = os.listdir(path)
    for file in files:
        if re.match(pattern, file):
            remove_one_dir("{}/{}".format(path, file))


def remove_one_dir(path="."):
    try:
        os.rmdir(path)
        print("Удалил директорию", path)
    except NotADirectoryError:
        print("{} не является директорией".format(path))
    except FileNotFoundError:
        print("Директория {} не существует".format(path))


if __name__ == "__main__":
    programm_title()
    for count in range(1, 10):
        make_dir("dir_" + str(count))
    print_files_on_dir()

    pattern_for_rm = "^dir_[0-9]+$"
    remove_dirs(pattern_for_rm)

    shutil.copyfile(sys.argv[0], sys.argv[0] + ".copy")
    print_files_on_dir()