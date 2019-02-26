def programm_title():
    print("**************************")
    print("*GB/Python/Lesson1/MEDIUM*")
    print("**************************")

programm_title()
while True:
    print("Введите число:")
    number = int(input())
    if (number < 0) or (number > 10):
        print("Ваше число должно быть в диапазоне 0..10")
    else:
        print("Теперь я возведу в степень ваше число:", number ** 2)
        break

programm_title()

first = "Это первая переменая"
second = "А это вторая переменая"


print("Смотри, я создал две переменные:")
print("first", first)
print("second", second)

print("Давай что-нибудь запишем в первую переменную:")
first = input()
print("Давай что-нибудь запишем и во вторую переменную:")
second = input()

print("Сейчас я поменяю их в одно действие:")
first, second = second, first
print("first", first)
print("second", second)
