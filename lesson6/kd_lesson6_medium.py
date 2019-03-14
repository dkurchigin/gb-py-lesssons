import random


def programm_title():
    print("**************************")
    print("*GB/Python/Lesson6/MEDIUM*")
    print("**************************")


class Person:
    def __init__(self, name="Person"):
        self.name = name
        self.health = 100
        self.damage = 25
        self.armor = 10
        self.greetings()

    def attack(self, player2):
        player2.health = player2.health - self._calculate_attack_power(player2)
        print("{} наносит удар... У игрока {} осталось {} единиц жизни!".format(self.name, player2.name, player2.health))

    def _calculate_attack_power(self, player2):
        return round(self.damage / player2.armor)

    def greetings(self):
        print("Игрок {} готов к бою!".format(self.name))


class Player(Person):
    def __init__(self, name="Player"):
        super().__init__(name)


class Enemy(Person):
    def __init__(self, name="Enemy"):
        super().__init__(name)


class GamePlay:
    def __init__(self, player1, player2):
        self.first_turn, self.second_turn = self._check_first_turn(player1, player2)
        print("Первым ходит игрок {}".format(self.first_turn.name))
        self.main_block(self.first_turn, self.second_turn)

    def _check_first_turn(self, player1, player2):
        if random.randint(0, 1) == 0:
            return player1, player2
        else:
            return player2, player1

    def main_block(self, player1, player2):
        current_turn = player1.name
        while True:
            if player1.health <= 0:
                print("\nВы храбро погибли от рук {}! А ведь у него осталось всего лишь {} единиц жизни...".format(player2.name, player2.health))
                break
            if player2.health <= 0:
                print("\n{}, Вы выиграли! У вас осталось {} единиц жизни".format(player1.name, player1.health))
                break

            if current_turn == player1.name:
                player1.attack(player2)
                current_turn = player2.name
            else:
                player2.attack(player1)
                current_turn = player1.name


programm_title()
player = Player("Рыцарь-88")
enemy = Enemy("Гоблин-69")

player.damage = 300
print("{} нашёл крутой мечь! Теперь его урон равен {} единиц".format(player.name, player.damage))
enemy.armor = 50
print("{} одевает шлем варваров! Защита персонажа увелечина до {} единиц".format(enemy.name, enemy.armor))

new_game = GamePlay(player, enemy)
