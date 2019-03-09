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


def make_dirs(count):
    for dir in range(1, count+1):
        os.mkdir("dir_"+str(dir))
    print("Директории созданы")


def remove_dirs(pattern, directory="."):
    files = os.listdir(directory)
    for file in files:
        if re.match(pattern, file):
            os.rmdir(directory + "/" + file)
    print("Удалил все папки!")


programm_title()
make_dirs(9)
print_files_on_dir()

pattern_for_rm = "^dir_[0-9]+$"
remove_dirs(pattern_for_rm)

shutil.copyfile(sys.argv[0], sys.argv[0] + ".copy")
print_files_on_dir()