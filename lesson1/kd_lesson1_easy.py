def programm_title():
    print("************************")
    print("*GB/Python/Lesson1/EASY*")
    print("************************")


programm_title()
first = "Это первая переменая"
second = "А это вторая переменая"


print("Смотри, я создал две переменные:")
print(first)
print(second)
print("А давай что-нибудь запишем во вторую переменную?")
second = input()
print("Молодец, теперь во второй переменной записано:", second)
programm_title()

print("Введите число, а я прибавлю к нему +2")
number = int(input())
number = number + 2
print("Результат равен =", number)
programm_title()

print("Введите ваш возраст")
age = int(input())
if (age >= 18):
    print("Доступ разрешён!")
else:
    print("Доступ запрещён!")