class TownCar:
    def __init__(self, name="Городское авто"):
        self.name = name
        self.color = "Серый"
        self._speed = 150
        self._is_police = False

    def go(self):
        print("{} начинает своё движение вперед".format(self.name))

    def stop(self):
        print("{} останавливается".format(self.name))

    def turn(self, direction=""):
        if direction == "right":
            print("{} повернула направо".format(self.name))
        elif direction == "left":
            print("{} повернула налево".format(self.name))
        else:
            print("{} никуда не повернула, водитель идиот =)".format(self.name))

    def is_it_police(self):
        if self._is_police:
            print("Да, {} является полицейской машиной".format(self.name))
        else:
            print("Автомобиль {} не является полицейской машиной".format(self.name))

        if self._speed >= 200 and not self._is_police:
                print("Но полицейской машине её будет сложно догнать...")


class SportCar(TownCar):
    def __init__(self, name="Спортивное авто"):
        super().__init__(name)
        self._speed = 250

    def go(self):
        print("{} быстро движется вперёд!".format(self.name))

    def stop(self):
        print("{} резко тормозит".format(self.name))


class PoliceCar(TownCar):
    def __init__(self, name="Полицейская машина"):
        super().__init__(name)
        self._speed = 190
        self._is_police = True


class WorkCar(TownCar):
    def __init__(self, name="Машина для работы"):
        super().__init__(name)
        self._speed = 120

    def go(self):
        print("{} медленно движется вперёд...".format(self.name))

    def stop(self):
        print("{} медленно тормозит...".format(self.name))


car = TownCar("Лада Калина")
car.go()
car.turn("left")
car.stop()
car.is_it_police()
print("=================")
car2 = SportCar("Феррари Турбо")
car2.go()
car2.turn("right")
car2.stop()
car2.is_it_police()
print("=================")
car3 = PoliceCar()
car3.go()
car3.turn("right")
car3.stop()
car3.is_it_police()
print("=================")
car4 = WorkCar()
car4.go()
car4.turn("hz")
car4.stop()
car4.is_it_police()