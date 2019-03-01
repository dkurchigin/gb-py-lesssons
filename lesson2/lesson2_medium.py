import random
import math
import datetime

my_date = datetime.date(2013,11,2)
n = 10

days_to_words = {
    1: "первое", 2: "второе", 3: "третье", 4: "четвёртое", 5: "пятое",
    6: "шестое", 7: "седьмое", 8: "восьмое", 9: "девятое", 10: "десятое",
    11: "одиннадцатое", 12: "двенадцатое", 13: "тринадцатое", 14: "четырнадцатое", 15: "пятнадцатое",
    16: "шестнадцатое", 17: "семнадцатое", 18: "восемнадцатое", 19: "девятнадцатое", 20: "двадцатое",
    21: "двадцать первое", 22: "двадцать второе", 23: "двадцать третье", 24: "двадцать четвёртое", 25: "двадцать пятое",
    26: "двадцать шестое", 27: "двадцать седьмое", 28: "двадцать восьмое", 29: "двадцать девятое", 30: "тридцатое",
    31: "тридцать первое"
}

month_to_words = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня",
    7: "июля", 8: "августа", 9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}

def programm_title():
    print("**************************")
    print("*GB/Python/Lesson2/MEDIUM*")
    print("**************************")

def random_list_with_number(n, lower_range, top_range):
    list = []
    for element in range(n):
        random_number = random.randint(lower_range,top_range)
        list.append(random_number)
    return list

def get_sqrt_from_list(list):
    list_with_sqrts = []
    for elements in list:
        root = math.sqrt(abs(elements))
        if (root % 1 == 0):
            list_with_sqrts.append(int(root))
    return list_with_sqrts

def get_unique_elements(list, mode):
    unique_elements_dict = {}
    not_repeated = []
    unique_elements_list = []

    for element in list:
        if not (element in unique_elements_dict):
            unique_elements_dict[element] = "Not Repeated"
        else:
            unique_elements_dict[element] = "Repeated"

    for key in unique_elements_dict:
        unique_elements_list.append(key)
        if (unique_elements_dict[key] == "Not Repeated"):
            not_repeated.append(key)

    if (mode == "unique"):
        return unique_elements_list
    else:
        return not_repeated

programm_title()
print("Если возможно получить корень без десятичной части, то делаем это:")
generated_list = random_list_with_number(n,-100,100)
print("Исходный лист:", generated_list)
print("Результат:", get_sqrt_from_list(generated_list))

programm_title()
print("Дана дата в формате dd.mm.yyyy, например:", my_date.strftime("%d.%m.%Y"))
print(days_to_words[my_date.day], month_to_words[my_date.month], my_date.year, "года")

programm_title()
print("Функция, которую я создал ещё в easy, на её вход посылаем n:")
print(random_list_with_number(n,-100,100))

programm_title()
print("Создаю список:")
generated_list = random_list_with_number(n,0,10)
unique_elements = get_unique_elements(generated_list, "unique")
not_repeated_elements = get_unique_elements(generated_list, "repeated")
print("Исходный лист:", generated_list)
print("Лист с неповторяющимися элементами:", unique_elements)
print("Лист с элеметами, которые не имеют повторений:", not_repeated_elements)