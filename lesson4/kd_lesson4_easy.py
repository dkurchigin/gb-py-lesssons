import random

def programm_title():
    print("************************")
    print("*GB/Python/Lesson4/EASY*")
    print("************************")

def random_list_with_number(list_lenght):
    return [(lambda element: random.randint(0, 19))(element) for element in range(list_lenght)]

def list_with_sqrt(list):
    return [element**2 for element in list]

def list_with_conditions(list):
    return [element for element in list if (element > 0 and element % 3 == 0 and element % 4 != 0)]

programm_title()
random_list = random_list_with_number(10)
print(random_list)
print(list_with_sqrt(random_list))

fruits_1 = ['банан', 'яблоко', 'груша']
fruits_2 = ['кокос', 'яблоко', 'банан', 'арбуз']

programm_title()
repeated_fruits = [element for element in fruits_1 if element in fruits_2]
print("Повторяющиеся фрукты:", repeated_fruits)

programm_title()
print(random_list)
print(list_with_conditions(random_list))


