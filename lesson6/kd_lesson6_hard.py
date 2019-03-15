def programm_title():
    print("************************")
    print("*GB/Python/Lesson6/HARD*")
    print("************************")


def try_create(title, color, type_of_toy):
    try:
        new_toy = CreateToy(title, color, type_of_toy)
    except TypeError:
        print("Для создания игрушки необходимо название, цвет и тип игрушки(животное или персонаж мультфильма)")


class Toy:
    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.print_info()

    def print_info(self):
        print("\nМы создали игрушку с названием {} и цветом {}".format(self.title, self.color))


class AnimalToy(Toy):
    def __init__(self, title, color):
        super().__init__(title, color)
        print("Замечательный зверёк!\n")


class CartoonToy(Toy):
    def __init__(self, title, color):
        super().__init__(title, color)
        print("Замечательный персонаж!\n")


class CreateToy:
    def __init__(self, title, color, type_of_toy):
        self.title = title
        self.color = color
        self.type_of_toy = type_of_toy
        self.buy_materials()
        self.sewing()
        self.paint()

        if self.type_of_toy == 0:
            return AnimalToy(self.title, self.color)
        else:
            return CartoonToy(self.title, self.color)

    def buy_materials(self):
        print("Покупаем сырьё для {}".format(self.title))

    def sewing(self):
        print("Начинаем шить {}!".format(self.title))

    def paint(self):
        print("Красим {} в вот такой цвет {}".format(self.title, self.color))


programm_title()
while True:
    print("Чтобы приступить к созданию игрушки нужно придумать ей название:")
    name = input()
    print("Далее введите её цвет:")
    color = input()
    if name == '' or color == '':
        print("Имя или цвет не должны быть пустыми, попробуйте ещё раз")
        continue
    print("И её тип. Если это животное введите 0, если персонаж мультфильма 1:")
    try:
        type_of_toy = int(input())
        if not (type_of_toy == 0 or type_of_toy == 1):
            print("Неизвестная команда, попробуйте заново")
            continue
        try_create(name, color, type_of_toy)
    except ValueError:
        print("Вы должны были ввести 0 или 1")
        continue
