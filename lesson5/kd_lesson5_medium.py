from kd_lesson5_easy import make_dir, remove_one_dir, print_files_on_dir
import os


def programm_title():
    print("**************************")
    print("*GB/Python/Lesson5/MEDIUM*")
    print("**************************")


def get_dir_for_change(current_dir):
    print("Введите название директории, в которую хотите перейти:")
    dir_for_change = input()
    try:
        os.chdir("{}/{}".format(current_dir, dir_for_change))
    except (NotADirectoryError, FileNotFoundError):
        print("Не могу перейти в директорию {}, её либо не существует, либо это файл, "
              "а не директория".format(dir_for_change))


def get_dir_for_remove(current_dir):
    print("Введите название директирии, которую хотите удалить:")
    dir_for_remove = input()
    remove_one_dir("{}/{}".format(current_dir, dir_for_remove))


def get_dir_for_create(current_dir):
    print("Введите название директирии, которую хотите создать:")
    dir_for_create = input()
    make_dir("{}/{}".format(current_dir, dir_for_create))


def commands():
    current_dir = os.getcwd()
    print("Эта программа умеет:")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")
    print("Выберите действие, например, введите 2")
    try:
        command = int(input())
        if command == 1:
            get_dir_for_change(current_dir)
        elif command == 2:
            print_files_on_dir()
        elif command == 3:
            get_dir_for_remove(current_dir)
        elif command == 4:
            get_dir_for_create(current_dir)
        else:
            print("Вы ошиблись, такой команды нет...")
    except ValueError:
        print("Вы ошиблись с вводом команды, а я помню предыдущий урок! =)\n")


programm_title()
while True:
    commands()
