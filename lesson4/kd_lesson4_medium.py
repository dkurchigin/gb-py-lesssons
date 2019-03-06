import re

def programm_title():
    print("**************************")
    print("*GB/Python/Lesson4/MEDIUM*")
    print("**************************")

programm_title()
print("Введите Вашу фамилию:")
last_name = input()
print("Введите Ваше имя:")
first_name = input()
print("Введите Ваш email:")
email = input()

pattern_for_names = '^[А-Я][а-я]+$'
pattern_for_email = '([a-z_0-9]+@[a-z0-9]+\.(com|ru|org))'

if not re.match(pattern_for_names, last_name):
    about_last_name = "- неверно указана фамилия"
else:
    about_last_name = ""
if not re.match(pattern_for_names, first_name):
    if about_last_name:
        about_first_name = ", а так же имя"
    else:
        about_first_name = "- неверно указано имя"
else:
    about_first_name = ""
if not re.match(pattern_for_email, email):
    about_email = "- неверно указан email"
else:
    about_email = "- указан верно"

print("{} {} {}{}, {} {}".format(last_name, first_name, about_last_name, about_first_name, email, about_email))

some_str_pattern = '\.{2}'
some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

programm_title()
if re.search(some_str_pattern, some_str):
    print("В тексте присутствует более двух точек подряд")
else:
    print("В тексте с точкам всё в порядке =)")