from kd_lesson5_easy import make_dir, remove_one_dir, print_files_on_dir
import os


def programm_title():
    print("**************************")
    print("*GB/Python/Lesson5/MEDIUM*")
    print("**************************")


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
            print("Введите название директории, в которую хотите перейти:")
            dir_for_change = input()
            if os.path.isdir(dir_for_change) and os.path.exists(dir_for_change):
                dir_for_change = current_dir + "/" + dir_for_change
                os.chdir(dir_for_change)
            else:
                print("Не могу удалить директорию {}, её либо не существует, либо это файл, "
                      "а не директория".format(dir_for_remove))
        elif command == 2:
            print_files_on_dir()
        elif command == 3:
            print("Введите название директирии, которую хотите удалить:")
            dir_for_remove = input()
            if os.path.isdir(dir_for_remove) and os.path.exists(dir_for_remove):
                dir_for_remove = current_dir + "/" + dir_for_remove
                remove_one_dir(dir_for_remove)
            else:
                print("Не могу удалить директорию {}, её либо не существует, либо это файл, "
                      "а не директория".format(dir_for_remove))
        elif command == 4:
            print("Введите название директирии, которую хотите создать:")
            dir_for_create = input()
            if not os.path.exists(dir_for_create):
                make_dir(current_dir + "/" + dir_for_create)
            else:
                print("Такая директория уже существует, придумайте другое название")
        else:
            print("Вы ошиблись, такой команды нет...")
    except ValueError:
        print("Вы ошиблись с вводом команды, а я помню предыдущий урок! =)\n")


programm_title()
while True:
    commands()
