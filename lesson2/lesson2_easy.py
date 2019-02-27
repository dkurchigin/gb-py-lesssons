import random

fruits = ["яблоко", "банан", "киви", "арбуз"]

first_list = ["это", "мой", "первый", "список", "список"]
second_list = ["да", "это", "же", "второй", "список"]

def programm_title():
    print("************************")
    print("*GB/Python/Lesson2/EASY*")
    print("************************")

def random_list_with_number(capacity):
    list = []
    for element in range(capacity):
        random_number = random.randint(0,99)
        list.append(random_number)
    return list

def div_and_inc(list):
    for element in list:
        if (element % 2 == 0):
            list[list.index(element)] = element / 4
        else:
            list[list.index(element)] = element * 2
    return list
    
def delete_list_from_list(first_list, second_list):
    for element_list_2 in second_list:
        if element_list_2 in first_list:
            first_list.pop(first_list.index(element_list_2))
            #yes, i have recurse =)
            delete_list_from_list(first_list, second_list)


programm_title()
print("Задача про фрукты:")
i = 0
for fruit in fruits:
    i += 1
    print('{}. \t{}'.format(i, fruit))

programm_title()
print("А это задача про два списка:")
print("Вот, что будет, если удалить из первого списка элементы, присутствующие во втором списке:")
delete_list_from_list(first_list, second_list)
print(first_list)

programm_title()
print("А вот задача с листом и цифрами:")
generated_list = random_list_with_number(10)
print("Исходный лист:", generated_list)
print("Результат:", div_and_inc(generated_list))