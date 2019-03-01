import re

equation = 'y = -12x + 11111140.2121'

def programm_title():
    print("************************")
    print("*GB/Python/Lesson2/HARD*")
    print("************************")

def parse_and_calc_equation(eduation, user_x):
    eduation_elements = eduation.split()
    if not (len(eduation_elements) == 5):
        print("Уравнение должно быть в формате y = kx + b и содержать пробелы между знаками и переменными")
    else:
        if not (eduation_elements[0] == "y"):
            print("Не могу найти переменную Y в строке!")
        if not (eduation_elements[1] == "="):
            print("Не могу найти знак равенства в строке!")
        if not ("x" in eduation_elements[2]):
            print("Не могу найти KX в строке!")
        else:
            eduation_elements[2] = re.sub(r'(x)', '', eduation_elements[2])
            return float(eduation_elements[2]) * user_x + float(eduation_elements[4])

def check_date(date):
    date_elements = date.split('.')
    if not (len(date_elements) == 3):
        print("Дата должна быть в формате dd.mm.yyyy")
    else:
        if ((1 <= int(date_elements[2]) <= 9999) and (len(date_elements[2]) == 4)):
            check_day_and_month(date_elements[0], date_elements[1])
        else:
            print("Год некорректен")
    
def check_day_and_month(day, month):
    if (1 <= int(month) <= 12) and (len(month) == 2):
        if ((1 <= int(day) <= 31) and (len(day) == 2)):
            if ((int(day) == 31) and not (((int(month) <= 7) and (int(month) % 2 == 1)) or ((int(month) >= 8) and (int(month) % 2 == 0)))):
                print("В месяце под номером", month, "нет 31 числа")
            else: 
                print("Вы ввели абсолютно верную дату!")
        else:
            print("День некорректен")
    else:
        print("Месяц некорректен")
    
programm_title()
print("Дано уравнение вида:", equation)
print("Введите значение x:")
x = float(input())
print("y = ", parse_and_calc_equation(equation, x))

programm_title()
print("Введите дату в формате dd.mm.yyyy :")
date = input()
check_date(date)
