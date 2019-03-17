import random
import collections
import re

"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""


class Card:
    def __init__(self, type="player"):
        self.type = type
        self.first_string = []
        self.second_string = []
        self.third_string = []
        self.summury_strings = []
        self.init_card()
        self._scratched_count = 0

    def init_card(self):
        self.first_string, self.second_string, self.third_string = self._init_card_strings()

    def _init_card_strings(self):
        positions_for_card = []

        for line in range(0, 3):
            positions_for_line = [(lambda element: 1)(element) for element in range(1, 6)]
            empty_positions = [(lambda element: ' ')(element) for element in range(1, 5)]

            positions_for_line += empty_positions
            random.shuffle(positions_for_line)
            positions_for_card += positions_for_line

        random_numbers = [(lambda element: random.randint(1, 90))(element) for element in range(1, 16)]
        self._check_repeat(random_numbers)
        self._group_by_five()


        card = [(lambda element: self.summury_strings.pop(0) if element == 1 else ' ')(element) for element in positions_for_card]
        return card[:9], card[9:18], card[18:]

    def _group_by_five(self):
        first, second, third = self.summury_strings[:5], self.summury_strings[5:10], self.summury_strings[10:]
        first.sort()
        second.sort()
        third.sort()
        self.summury_strings = first + second + third
        return self.summury_strings

    def _check_repeat(self, elements):
        not_unique_random_numbers = [item for item, count in collections.Counter(elements).items() if count > 1]

        if not_unique_random_numbers:
            for repeated_elements in not_unique_random_numbers:
                new_random_number = random.randint(1, 90)
                elements[elements.index(repeated_elements)] = new_random_number
            self._check_repeat(elements)
        else:
            self.summury_strings = elements

    def __str__(self):
        if self.type == "player":
            player_type = "---------- Ваша карточка ----------"
        else:
            player_type = "------- Карточка компьютера -------"
        first_str = "{0[0]}\t {0[1]}\t {0[2]}\t {0[3]}\t {0[4]}\t {0[5]}\t {0[6]}\t {0[7]}\t {0[8]}".format(self.first_string)
        second_str = "{0[0]}\t {0[1]}\t {0[2]}\t {0[3]}\t {0[4]}\t {0[5]}\t {0[6]}\t {0[7]}\t {0[8]}".format(self.second_string)
        third_str = "{0[0]}\t {0[1]}\t {0[2]}\t {0[3]}\t {0[4]}\t {0[5]}\t {0[6]}\t {0[7]}\t {0[8]}".format(self.third_string)
        final = "-----------------------------------"
        return "{}\n{}\n{}\n{}\n{}".format(player_type, first_str, second_str, third_str, final)

    def try_scratch_out(self, number):
        if self.type == "player":
            print("Зачеркнуть цифру? (y / n)")
            while True:
                answer = input()
                pattern_for_y = '(^[yY]$|^[yY][eE][sS]$)'
                pattern_for_n = '(^[nN]$|^[nN][oO]$)'
                if not (re.match(pattern_for_y, answer) or re.match(pattern_for_n, answer)):
                    print("Неизвестная команда, попробуйте ещё раз!")
                    continue
                elif (re.match(pattern_for_y, answer) and not self._scratch_out(number)) or \
                        (re.match(pattern_for_n, answer) and self._scratch_out(number)):
                    print("Вы ошиблись и проиграли!")
                    exit(0)
                else:
                    break
        else:
            print("Компьютер пытается найти и вычеркнуть число...")
            self._scratch_out(number)

    def _scratch_out(self, number):
        if number in self.first_string:
            self.first_string[self.first_string.index(number)] = 'X'
            self._scratched_count += 1
        elif number in self.second_string:
            self.second_string[self.second_string.index(number)] = 'X'
            self._scratched_count += 1
        elif number in self.third_string:
            self.third_string[self.third_string.index(number)] = 'X'
            self._scratched_count += 1
        else:
            return False

        return True

    def is_win(self):
        if self._scratched_count == 15:
            return True


class Loto:
    def __init__(self):
        self.last_number = ''
        self._generate_numbers()
        self.new_game()

    def _generate_numbers(self):
        self._numbers_in_bag = [element for element in range(1, 91)]

    def get_number(self):
        random.shuffle(self._numbers_in_bag)
        remove_one = self._numbers_in_bag.pop()
        print("Новый бочонок: {} (осталось {})".format(remove_one, len(self._numbers_in_bag)))
        return remove_one

    def new_game(self):
        print("Добро пожаловать в игру ЛОТО!")
        print("Создаю карточку игрока и компьютера...")
        player_card = Card()
        pc_card = Card('pc')
        self._turn_by_turn(player_card, pc_card)

    def check_winner(self, user, pc):
        if user.is_win() and pc.is_win():
            print("Поздравляем! Победила дружба!")
            exit(1)
        elif user.is_win():
            print("Вы победили!")
            exit(2)
        elif pc.is_win():
            print("Слава Тьюрингу! Компьютерам Слава!")
            exit(0)

    def _turn_by_turn(self, user, pc):
        while True:
            print(user)
            print(pc)
            self.last_number = self.get_number()
            pc.try_scratch_out(self.last_number)
            user.try_scratch_out(self.last_number)
            self.check_winner(user, pc)


newgame = Loto()
