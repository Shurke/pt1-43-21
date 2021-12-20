"""
Игра камень ножницы бумага
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д.
"""


import random


class Battle:
    all_actions = ["камень", "ножницы", "бумага"]


class Bot:
    def __init__(self):
        self.bot_choice = random.choice(Battle.all_actions)

    @staticmethod
    def bot_choice():
        bot_choice = random.choice(Battle.all_actions)
        return bot_choice


class User:
    def __init__(self):
        self.name = input("Как вас зовут? \n")
        self.botname = input("Придумайте имя вашему сопернику: \n")

    def get_choice(self):
        try:
            choice = int(input(f"\nПривет, {self.name}!\n"
                               f"Сегодня ты сразишься с {self.botname}\n\nВыбери жест:"
                               f"\n1-Камень\n2-Ножницы\n3-Бумага\nВаш выбор: "))
            user_choice = Battle.all_actions[choice - 1]
            bot_choice = Bot.bot_choice()
            print(f"{user_choice} VS {bot_choice}")
            if user_choice == bot_choice:
                print(f"Оба пользователя выбрали {user_choice}. Ничья!")
            elif user_choice == "камень":
                if bot_choice == "ножницы":
                    print(f"{self.name} победил!")
                else:
                    print(f"{self.botname} победил")
            elif user_choice == "бумага":
                if bot_choice == "камень":
                    print("f{self.name} победил!")
                else:
                    print(f"{self.botname} победил")
            elif user_choice == "ножницы":
                if bot_choice == "бумага":
                    print("f{self.name} победил!")
                else:
                    print(f"{self.botname} победил")
        except (TypeError, ValueError, SyntaxError, IndexError):
            print("Ошибка ввода!")


p1 = User()
p1.get_choice()
