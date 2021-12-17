""" Задача 1. Реализована модель заказа пиццы в ресторане

Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.

"""


class Order:
    """осдержит список пицц, умеет посчитывать стоимость заказа"""
    def __init__(self, list_of_pizzas):
        self.list_of_pizzas = list_of_pizzas

    def count_total(self):
        total = 0
        for pizza in self.list_of_pizzas:
            total = total + pizza.price()
        return  total



class Pizza:

    """стандарт"""
    """цена за пиццу в зависмости от размера это у дочерних классов"""

    price_to_cook = 7
    sizes = ("small", "medium", "big")
    price_correction = dict()
    price_correction["small"] = 1
    price_correction["medium"] = 1.3
    price_correction["big"] = 1.5
    available_ingredients = (
        "морской коктейль из мидий",
        "мини-осьминоги",
        "кальмары",
        "креветки",
        "бекон",
        "куриное филе",
        "ветчина",
        "Моцарелла",
        "Пармезан",
        "Эмменталь",
        "сыр Дорблю",
        "каперсы",
        "маслины",
        "петрушка",
        "орегано",
        "базилик",
        "сельдерей",
        "томатный соус",
        "соус бешамель",
        "помидоры",
    )
    ingredients_prices = {
        "морской коктейль из мидий": 3,
        "мини-осьминоги": 3,
        "кальмары": 3,
        "креветки": 3,
        "бекон": 2,
        "куриное филе": 2,
        "ветчина": 2,
        "Моцарелла": 2,
        "Пармезан": 2,
        "Эмменталь": 2,
        "сыр Дорблю": 2,
        "каперсы": 1,
        "маслины": 1,
        "петрушка": 1,
        "орегано": 1,
        "базилик": 1 ,
        "сельдерей": 1,
        "томатный соус": 1,
        "соус бешамель": 1,
        "помидоры": 1,
    }


    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size

    def price(self):
        """счиатем в зависимости от размера и ингридиентов и стоимости услуги приготовления"""
        total = self.price_to_cook
        for ingredient in self.ingredients:
            total = total + self.ingredients_prices[ingredient]
        total = total * self.price_correction[self.size]
        return total


class Waiter:

    def take_oder():

        """предложить стандвртные пиццы"""
        """предложить пиццы из набора ингридиенов"""




    def sent_oder_to_cook():
        pass

    def print_the_bill():
        pass

    def take_payment():
        pass


waiter_Mark = Waiter()
Pizza1 = Pizza(("Моцарелла",
        "Пармезан",
        "Эмменталь",
        "сыр Дорблю",
        "каперсы",
        "маслины"), "big")
print(Pizza1.price())
Pizza2= Pizza(("Моцарелла",
        "орегано",
        "базилик",
        "томатный соус",
        "помидоры",), "big")
print(Pizza2.price())

order1 = Order([Pizza1, Pizza2])
print(order1.count_total())

#waiter_Mark.take_oder()
#if take

print("\033[1;34;47m цфшеук\033[0;0m")