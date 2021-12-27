"""
Создайте  модель из жизни. Это может быть бронирование комнаты в
отеле, покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для
симуляции различных действий. Программа должна инстанцировать
объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""


import random
import sys
# import time


"""
Подготовка к встрече Нового Года

Поставить ёлку и купить подарки
"""


class NewYearTreePlace:
    """Место для новогодней елки."""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def dimensions_tree(self):
        out_str = f'Так, в высоту елка должна быть {self.height} метра, в ширину - {self.width}'
        return print(out_str)


class Car:
    """Средство передвижения."""
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def move(self):
        out_str = f'А добраться туда можно на {self.vehicle}.'
        print(out_str)
        return self.vehicle


class Gifts:
    """Подарки на Новый год."""
    def __init__(self, desires):
        self.desires = desires

    @staticmethod
    def move_gifts():
        """Поездка за подарками."""
        print('За подарками поедем в торговый центр. ', end='')
        random_choose_car = RandomChoose(['такси', 'своей машине', 'общественном транспорте'], 1)
        my_vehicle = Car(random_choose_car.get_choice())
        out_vehicle = my_vehicle.move()
        return out_vehicle

    def choose_gifts(self):
        """Выбор подарков."""
        random_choose_gifts = RandomChoose(self.desires, 4)
        out_gifts = random_choose_gifts.get_choice()
        print('Куплены отличные подарки: ', end='')
        print(', '.join(out_gifts))
        return out_gifts


class NewYearTree(NewYearTreePlace):
    """Новогодняя ёлка."""
    type_tree = ''
    get_tree_place = ''

    def __init__(self, height, width):
        NewYearTreePlace.__init__(self, height, width)

    def choose_type_tree(self):
        """Выбор между живой и искусственной елкой."""
        type_tree_list = ['Живую, конечно!', 'Искусственную, в гараже дожидается!']
        random_choose_tree = RandomChoose(type_tree_list, 1)
        self.type_tree = random_choose_tree.get_choice()
        out_type = f'Какую ель выбрать?..{self.type_tree}'
        return print(out_type)

    def get_tree(self):
        """Покупка ёлки на базаре."""
        print('Даа... Выбор здесь большой.')
        view_tree_list = ['облезлая', 'редкая', 'пышная']
        while True:
            rand_height = round(random.triangular(self.height * 0.7,
                                                  self.height * 1.3, self.height), 1)
            rand_width = round(random.triangular(self.width * 0.7,
                                                 self.width * 1.3, self.width), 1)
            random_choose_view = RandomChoose(view_tree_list, 1)
            view_tree = random_choose_view.get_choice()
            print(f'Посмотрим на эту. Высота {rand_height}, ширина {rand_width}, {view_tree}')
            if view_tree == 'пышная':
                height_ratio = rand_height / self.height
                width_ratio = rand_width / self.width
                if height_ratio == 1.0 and width_ratio == 1.0:
                    print('Это она. Красавица! Поехали домой.')
                    break
                elif 0.8 <= height_ratio <= 1.1 and 0.8 <= width_ratio <= 1.1:
                    print('Красивая! Правда, размер немного другой. ', end='')
                    my_choice = ''
                    while my_choice != 'да' and my_choice != 'нет':
                        my_choice = input('Брать?..(да/нет): ')
                    if my_choice == 'нет':
                        print('Похожу еще')
                    elif my_choice == 'да':
                        print('Все, выбрали. Поехали домой.')
                        break
        return view_tree

    def move_tree(self):
        """Поездка за ёлкой."""
        if self.type_tree.find('Жив') != -1:
            self.get_tree_place = 'Базар'
        elif self.type_tree.find('Искус') != -1:
            self.get_tree_place = 'Гараж'
        else:
            print('Мы еще не выбрали тип ёлки...')
        print(f'{self.get_tree_place}. Привезем ель оттуда. ', end='')
        random_choose_car = RandomChoose(['такси', 'своей машине'], 1)
        my_vehicle = Car(random_choose_car.get_choice())
        my_vehicle.move()
        return my_vehicle

    @staticmethod
    def put_gifts():
        """Положить подарки."""
        desires_list = ['наушники', 'краски с кистью', 'плюшевый мишка', 'часы', 'кукла', 'духи', 'коньки']
        print('Ёлку поставили и украсили. Надо еще положить подарки.')
        gifts = Gifts(desires_list)
        out_vehicle = gifts.move_gifts()
        out_gifts = gifts.choose_gifts()
        return [out_vehicle, out_gifts]


class RandomChoose:
    """Случайный выбор одного или нескольких элементов из списка."""
    def __init__(self, choice_list, choice_type):
        self.choice_list = choice_list
        self.choice_type = choice_type

    def get_choice(self):
        if self.choice_type == 1:
            return random.choice(self.choice_list)
        elif self.choice_type > 1:
            return random.sample(self.choice_list, self.choice_type)


def tree_quest():
    """Квест по установке новогдней елки."""
    print('Новый Год скоро. пора устанавливать елку!')

    height_place = 2.5
    width_place = 1.5
    tree_place = NewYearTreePlace(height_place, width_place)
    tree_place.dimensions_tree()

    newyear_tree = NewYearTree(tree_place.height, tree_place.width)
    newyear_tree.choose_type_tree()
    newyear_tree.move_tree()
    if newyear_tree.get_tree_place == 'Базар':
        newyear_tree.get_tree()
    newyear_tree.put_gifts()
    print('Ёлка поставлена, подарки положены, до Нового года можно отдохнуть.')
    print('Нееееет! Еще закупать продукты и готовить к столу! Но это уже другая история.')
    print('Конец')


if __name__ == '__main__':
    sys.exit(tree_quest())
