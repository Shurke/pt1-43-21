"""
Создать модель из реальной жизни
    Реализация упрощенной модели Рецепшна, с различным функционалом
    1.Класс Client -> создание и удаление профиля клиента
        а)создание профиля клиента
        б)удадение профиля клиента
    2.Класс Reception -> обработка запросов клиентов
        a)запись соотвествий номер - постоялец в словарь (заселение)
        б)смена комнаты, с возможностью указания причины
        в)получение информации о клиенте через номер комнаты
        г)просьба об оказании услуги
        д)выселение
    3.Класс Entertainment -> реализация развлечений в отеле
        a)возможность поиграть в казино в отеле
        б)возможномть сходить в бассейн и аквазону
    4.Класс Restaurant -> реализация услуг ресторана клиентам отеля
        а)возможность купить алкоголь
        б)возможность заказать деликатест
        в)проверка клиента на наличие пакета "Все включено"
"""


import random
import time


class RoomNumberError(Exception):
    """Excepts not existing room number input"""


class Client:
    """creates and deletes clients' profile"""

    def __init__(self, name: str, surname: str, days: int, all_incl: int = 0):
        """initialization of client"""

        # checks if name is string
        if not isinstance(name, str):
            raise ValueError('Wrong input data')
        # checks if surname is string
        if not isinstance(surname, str):
            raise ValueError('Wrong input data')
        # checks if days is integer
        if not isinstance(days, int) or days < 1:
            raise ValueError('Wrong input data')
        # checks if all_inclusive is integer
        if not isinstance(all_incl, int):
            raise ValueError('Wrong input data')

        self.name = name
        self.surname = surname
        self.days = days
        self.all_inclusive = all_incl
        self.money_debt = 0
        self.curr_room = None

    def delete_client(self):
        """deletes client from class"""
        print('Thank you for choosing us!')
        del self


class Reception:
    """processes Reception Services and help"""

    def __init__(self, room_num: int = None):
        """initialization of room_number if client (not) exists """

        if room_num is not None:
            # If the client has a room, getting an request from him
            if room_num not in Reception.rooms.keys() or Reception.rooms[room_num] == 0:
                raise RoomNumberError('Wrong room number')
            self.room_number = room_num
            client = Reception.get_client_info(room_num)
            print(f'Hello, {client.name} {client.surname}!')
            print(Reception.offer_help_message)
        else:
            # If the client doesn't have a room, checking him in
            Reception.welcoming()
            x = Client(input(), input(), int(input()), int(input()))
            Reception.move_in(x)
            self.room_number = x.curr_room

    rooms = {
        101: 0, 102: 0, 103: 0, 104: 0, 105: 0,
        106: 0, 107: 0, 108: 0, 109: 0, 110: 0,
        201: 0, 202: 0, 203: 0, 204: 0, 205: 0,
        206: 0, 207: 0, 208: 0, 209: 0, 210: 0,
        301: 0, 302: 0, 303: 0, 304: 0, 305: 0,
        306: 0, 307: 0, 308: 0, 309: 0, 310: 0,
        401: 0, 402: 0, 403: 0, 404: 0, 405: 0,
        406: 0, 407: 0, 408: 0, 409: 0, 410: 0,
    }
    problems_with_room = []
    pending_service = {}
    welcome_words = 'Hello, we are glad to see you at our Hotel!'
    get_info = """please enter your name, surname, duration in days and
1 if you choose "all-inclusive" or 0 if you choose "standard" package:"""
    offer_help_message = 'How can we help you?'

    @staticmethod
    def welcoming():
        """prints out welcoming words"""
        print(Reception.welcome_words)
        print(Reception.get_info)

    @staticmethod
    def move_in(obj):
        """checks client in the room"""
        booked = False
        if obj.all_inclusive:
            obj.money_debt = obj.days * 150
        else:
            obj.money_debt = obj.days * 120
        for room in Reception.rooms.keys():
            if Reception.rooms[room] == 0:
                Reception.rooms[room] = obj
                obj.curr_room = room
                booked = True
                break
        if not booked:
            raise RoomNumberError('There are no free places at the hotel')
        print(f'Your room number is {obj.curr_room}')
        print(f'payments for the duration - {obj.money_debt}')

    def change_room(self, reason: str = None):
        """changes client's room and (optional) adds reason into list"""

        client = Reception.rooms[self.room_number]
        flag = False
        for room in Reception.rooms.keys():
            if Reception.rooms[room] == 0:
                Reception.rooms[client.curr_room] = 0
                client.curr_room = room
                Reception.rooms[room] = client
                self.room_number = room
                flag = True
                break
        if not flag:
            raise RoomNumberError('All other rooms are booked')
        print('Your room has been changed!')
        print(f'Now your room number is {client.curr_room}')
        if reason is not None:
            Reception.problems_with_room.append(reason)

    def ask_service(self, required_service):
        """asks for a service, by adding request in a pending dictionary"""
        print('We will help you as soon as possible!')
        Reception.pending_service[self.room_number] = required_service

    def moving_out(self):
        """realizes the process of checking out"""
        client = Reception.rooms[self.room_number]
        print(f'You have to pay {client.money_debt}$ for the duration')
        Reception.rooms[self.room_number] = 0
        print('Good Bye! Hope to see you next time at our Hotel!')
        Client.delete_client(client)

    @staticmethod
    def get_client_info(room_num: int):
        if not isinstance(room_num, int) or room_num not in Reception.rooms.keys():
            raise RoomNumberError('Wrong room number')
        """returns all information about the client from the room"""
        return Reception.rooms[room_num]


class Entertainment(Reception):
    """Class realizes different entertainments"""

    def __init__(self, room_num: int):
        """initialization of room number for further operations"""
        super().__init__(room_num)
        self.client = Reception.get_client_info(room_num)
        print('What would you like to do?')

    def play_casino(self, deposit: int):
        """Simulates casino gameplay, based on random library"""

        # checks if deposit more than 0
        if deposit <= 0:
            raise ValueError('Deposit should be more than 0')
        # checks if int was given
        if not isinstance(deposit, int):
            raise TypeError('Deposit should be int')

        if random.randint(1, 10) % 2 == 0:
            # Winning case
            print(f'{self.client.name}, you\'ve won in casino')
            print(f'You have won {deposit * 2} $')
            # decreasing hotel debt
            self.client.money_debt -= deposit
            print('Your current hotel debt -', self.client.money_debt)
        else:
            # loosing case
            print(f"{self.client.name}, you've lost in casino")
            print(f'You have lost {deposit} $')
            # increasing hotel debt
            self.client.money_debt += deposit
            print('Your current hotel debt -', self.client.money_debt)

    @staticmethod
    def swimming(person_amount: int):
        """gives person * 2 towels if swimming-pool is opened"""

        # checks if the amount of people more than 0
        if person_amount <= 0:
            raise ValueError('Should be at least one person')
        # checks if int was given
        if not isinstance(person_amount, int):
            raise TypeError('Number of persons should be int')

        # s equals to time in hh:mm:ss format
        s = time.strftime(time.ctime()).split()[3]
        if 7 < int(s[0]) * 10 + int(s[1]) < 22:
            print(f'We gave you {person_amount * 2} towels, you can swim until 22:00')
        else:
            print('Unfortunately, swimming-pool is closed now,it opens at 7:00')


class Restaurant(Reception):
    """class realizes Hotel Restaurant services and functions"""

    def __init__(self, room_num: int):
        """initialization of room number for further operations"""
        super().__init__(room_num)
        self.client = Reception.get_client_info(room_num)

        if self.client.all_inclusive:
            # checks if client's package is 'all-inclusive'
            print(f'Have a nice meal, {self.client.name}!')
        else:
            # checks if client's package is 'standard' and makes an offer
            print('Meals are not included, you have to pay 15$ extra!')
            print('Would you like to pay: (y/n)')
            answer = input().lower()
            if answer == 'y':
                self.client.money_debt += 15
                print(f'Have a nice meal, {self.client.name}!')
            else:
                print(f'Have a nice day, {self.client.name}!')

    def buy_alcohol(self, alcohol: str):
        """sells alcohol to a client"""
        print(f'{alcohol} costs 15$, {self.client.name}')
        self.client.money_debt += 15

    def order_delicacy(self, delicacy: str):
        """sells delicacy to a client"""
        print(f'You will pay 20$ for {delicacy}, {self.client.name}')
        self.client.money_debt += 20


def main():
    """Examples of working with given classes"""

    print('-----Creating first client-----')
    Reception()                     # создаем профиль клиента1 и заселяем его
    print('\n-----Creating second client-----')
    Reception()                     # создаем профиль клиента2 и заселяем его
    print('\n-----Creating prototype for room 102-----')
    client1 = Reception(102)        # создаем экземпляр Reception, для работы с методами
    # print(Reception.rooms)        # для проверки заполненности комнат до смены
    client1.change_room()           # Меняем комнату клиента
    # print(Reception.rooms)        # для проверки заполненности комнат после смены
    print('\n-----Creating prototype for room 101-----')
    client2 = Reception(101)        # создаем экземпляр Reception, для работы с методами
    client2.ask_service('clean')    # используем метод объекта, для заказа услуги
    print('\n-----Creating prototype for room 101 in Entertainment-----')
    ent1 = Entertainment(101)       # создаем экземпляр класса развлечения
    ent1.play_casino(200)           # используем метод объекта, для игры в казино
    print('\n-----Creating prototype for room 103 in Entertainment-----')
    ent2 = Entertainment(103)       # создаем экземпляр класса развлечения
    ent2.play_casino(300)           # используем метод объекта, для игры в казино
    print('\n-----client1 goes to swimming-pool-----')
    ent1.swimming(2)                # используем метод объекта, для посещения аквазоны
    print('\n-----client2 goes to swimming-pool-----')
    ent2.swimming(3)                # используем метод объекта, для посещения аквазоны
    print('\n-----Creating prototype for room 101 in Entertainment-----')
    eating1 = Restaurant(101)       # создаем экземпляр класса ресторан
    eating1.buy_alcohol('wine')     # используем метод объекта, для покупки алкоголя
    print('\n-----Creating prototype for room 103 in Entertainment-----')
    eating2 = Restaurant(103)       # создаем экземпляр класса ресторан
    eating2.order_delicacy('Crab')  # используем метод объекта, для заказа деликатеса
    print('\n-----moving out from client1 room-----')
    client1.moving_out()            # используем метод объекта, для выселения постояльца


if __name__ == '__main__':
    main()
