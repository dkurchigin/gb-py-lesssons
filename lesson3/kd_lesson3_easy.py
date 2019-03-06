def programm_title():
    print("************************")
    print("*GB/Python/Lesson3/EASY*")
    print("************************")


def info_about_person(name, age, city):
    return f"{name}, {age} год(а), проживает в городе {city}"


def get_max_number(first_number, second_number, third_number):
    return max(first_number, second_number, third_number)


def find_max_str(*strings):
    longest_str = ""
    for string in strings:
        if len(string) >= len(longest_str):
            longest_str = string
    return longest_str


name = "Василий"
age = 21
city = "Москва"

programm_title()
print(info_about_person(name, age, city))

first_number, second_number, third_number = 23, 88, 14

programm_title()
print("Максимальное число:", get_max_number(first_number, second_number, third_number))

programm_title()
print("Самая длинная строка:", find_max_str("мама", "очень долго", "мыла наши рамы", "тынц-тынц"))
