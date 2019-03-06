def programm_title():
    print("************************")
    print("*GB/Python/Lesson3/HARD*")
    print("************************")


def attack(player1, player2):
    player2["health"] = player2["health"] - calculate_attack_power(player1["damage"], player2["armor"])
    return player2


def calculate_attack_power(damage, armor):
    return round(damage / armor)


def change_turn(turn):
    if turn == "player":
        return "enemy"
    else:
        return "player"


def load_entities_from_file(file, dict_name):
    with open(file, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.replace("\n", "")
            key, value = line.split(': ')
            value = value.replace(",", "")
            if not value.isalpha():
                value = float(value)
                if value % 1 == 0:
                    value = int(value)
            dict_name.update({key: value})
        return dict_name

who_turn_now = "player"

player = {}
enemy = {}
#player = {"name": "player", "health": 100, "damage": 25, "armor": 1.2}
#enemy = {"name": "enemy", "health": 100, "damage": 23, "armor": 1.5}

programm_title()

player = load_entities_from_file("player.txt", player)
enemy = load_entities_from_file("enemy.txt", enemy)
print("Для начала игры введите имя вашего персонажа:")
player["name"] = input()
print("Добро пожаловать в игру, {}!".format(player["name"]))

while True:
    if player["health"] <= 0:
        print("\nВы храбро погибли от рук {}! А ведь у него осталось всего лишь {} единиц жизни...".format(enemy["name"], enemy["health"]))
        break
    if enemy["health"] <= 0:
        print("\n{}, Вы выиграли! У вас осталось {} единиц жизни".format(player["name"], player["health"]))
        break

    if who_turn_now == "player":
        enemy = attack(player, enemy)
        print("{} атаковал {}. Значение жизни вашего врага теперь равно {}".format(player["name"], enemy["name"], enemy["health"]))
    else:
        player = attack(enemy, player)
        print("Вас атаковал {}. Ваше значение жизни снизилась до {}".format( enemy["name"], player["health"]))

    who_turn_now = change_turn(who_turn_now)
