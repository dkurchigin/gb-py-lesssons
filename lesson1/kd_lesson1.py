def programm_title():
    print("*******************")
    print("*GB/Python/Lesson1*")
    print("*******************")

def check_parameters(age,weight):
    if age < 30:
        if (weight >= 50) and (weight <= 120):
            return "хорошее состояние"
        else:
            return "следует заняться собой"
    elif (age >= 30) and (age < 40):
        if (weight >= 50) and (weight <= 120):
            return "хорошее состояние"
        else:
            return "следует заняться собой"
    else:
        if (weight >= 50) and (weight <= 120):
            return "хорошее состояние"
        else:
            return "следует обратится к врачу!ы"

first_name = ""
last_name = ""
age = ""
weight = ""

programm_title()
while True:
    if (not first_name):
        print("Введите вашу фамилию:")
        first_name = input()
        if (not first_name):
            continue
    if not last_name:
        print("Введите ваше имя:")
        last_name = input()
        if (not last_name):
            continue
    if not age:
        print("Введите ваш возраст:")
        age = input()
        if (not age):
            continue
        else:
            age = int(age)
            if (age <= 0):
                print("Ваш возраст должен быть положительным числом")
                age = ""
                continue
    if not weight:
        print("Введите ваш вес:")
        weight = input()
        if (not weight):
            continue
        else:
            weight = int(weight)
            if (weight <= 0):
                print("Ваш вес должен быть положительным числом")
                weight = ""
                continue
    final_result = check_parameters(age,weight)
    print(first_name + " " + last_name + ", возраст " + str(age) + ", вес " + str(weight) + " - " + final_result)
    break