'''
Создайте  модель из жизни.
Это может быть бронирование комнаты в отеле, покупка билета в транспортной компании,
или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
Камень, ножницы, бумага, #ящерица, #спок
'''

import random


class Actions:
    '''Класс. Список доступных действий игрока и npc

    '''
    actions = {1: "Камень", 2: "Ножницы", 3: "Бумага"}


class Npc:
    '''Класс Игровой бот. Рандомно получает действие и имя из списка

    '''
    names = {1: 'Шелдон', 2: 'Пенни', 3: 'Говард'}

    def __init__(self):
        self.choice = random.choice(list(Actions.actions.keys()))
        self.name = random.choice(list(Npc.names.keys()))

    @staticmethod
    def choice():
        choice = random.choice(list(Actions.actions.keys()))
        return choice

    @staticmethod
    def name():
        name = random.choice(list(Npc.names.values()))
        print("Ваш соперник:", name)
        return name


class Gamer:
    """Класс Игрок. Ввод имени. Выбор"""

    def __init__(self):
        self.name = input("Введите ваше имя: ")

    @staticmethod
    def choice():
        print(f"Введите цифру соответствующую действию {Actions.actions}:")
        try:
            choice = int(input("Ваше действие:"))
            if choice not in range(1, 3):
                print("Ошибка ввода")
            else:
                return choice
        except (TypeError, ValueError):
            print("Ошибка ввода")


class Session:
    """Класс сессия.Работает с текущим счетом и определяет победителя сессии

    """

    def __init__(self, win1=0, win2=0):
        self.win1 = win1
        self.win2 = win2

    @staticmethod
    def description():
        """Описание игры"""
        print("Привет! Я хочу сыграть с тобой в игру :) Камень, ножницы, бумага")
        print("Камень, ножницы, бумага")
        print("Правила просты. Камень тупит ножницы. Ножницы режут бумагу. Бумага накрывает камень.")
        print("Удачи!!!")

    def play_game(self, gamer, npc, npc_name, gamer_name):
        """Определение победителя раунда"""
        if npc == 1 and gamer == 3:
            print(f'Бумага накрывает камень, {gamer_name} выйграл раунд!')
            self.win1 += 1
        elif npc == 1 and gamer == 2:
            print(f'Камень тупит ножницы, {npc_name} выиграл раунд')
            self.win2 += 1
        elif npc == 3 and gamer == 1:
            print(f'Бумага накрывает камень, {npc_name} выиграл раунд')
            self.win2 += 1
        elif npc == 3 and gamer == 2:
            print(f'Ножницы режут бумагу, {gamer_name} выйграл раунд!')
            self.win1 += 1
        elif npc == 2 and gamer == 1:
            print(f'Камень тупит ножницы, {gamer_name} выйграл раунд!')
            self.win1 += 1
        elif npc == 2 and gamer == 3:
            print(f'Ножницы режут бумагу, {npc_name} выиграл раунд')
            self.win2 += 1

    def get_score(self):
        print(f'Текущий счет {self.win1} - {self.win2}')
        return self.win1, self.win2


def game():
    """Непосредственно игра"""

    Session().description()
    npc_name = Npc.name()
    gamer_name = Gamer().name
    gamer_choice = Gamer.choice()

    if gamer_choice is None:
        return
    npc_choice = Npc.choice()

    gamer_wins = 0
    npc_wins = 0
    # while gamer_wins < 3 or npc_wins < 3:
    gamer_wins, npc_wins = Session().get_score()
    print(f'{npc_name} выбирает {Actions.actions[npc_choice]}')
    Session().play_game(gamer_choice, npc_choice, npc_name, gamer_name)


if __name__ == '__main__':
    game()
