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


programm_title()
print("Дано уравнение вида:", equation)
print("Введите значение x:")
x = float(input())
print("y = ", parse_and_calc_equation(equation, x))