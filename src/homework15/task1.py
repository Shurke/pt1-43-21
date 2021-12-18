""" Задача 1. Реализована модель заказа пиццы в ресторане

Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.

"""
import random


class Order:
    """осдержит список пицц, умеет посчитывать стоимость заказа"""
    def __init__(self, list_of_pizzas):
        self.list_of_pizzas = list_of_pizzas

    def count_total(self):
        total = 0
        for pizza in self.list_of_pizzas:
            total = total + pizza.price()
        return total


class Pizza:
    """"""

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
        "базилик": 1,
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

    def __init__(self, name):
        self.name = name

    def take_oder(self):
        list_of_pizzas = []
        print("Добрый день, меня зовут " + self.name,
              "Я готов принят ваш заказ, Давайте выберем пиццы.")
        one_more_pizza = True
        while one_more_pizza:
            ingredients = []
            print("Выберите размер пиццы: ", ", ".join(Pizza.sizes))
            size = "big"
            print("Вы выбрали пиццу размера " + size)
            print("Вы можете выбрать следующие ингредиенты: ")
            for ingredient in Pizza.available_ingredients:
                print("\033[1;34;47m", ingredient, "\033[0;0m")
            ingredients.append("Пармезан")
            ingredients.append("бекон")

            if len(ingredients) == 0:
                print("К сожалению, вы не выбрали ингредиенты для пиццы")
                one_more_pizza = False
            else:
                print("Вы выбрали следующте ингредиенты: ", ", ".join(ingredients))
                new_pizza = Pizza(ingredients, size)
                list_of_pizzas.append(new_pizza)
            print("Готовы заказать еще одну пиццу?")
            one_more_pizza = False
            print("ок")

        if len(list_of_pizzas) == 0:
            print("Ваш заказ не принят")
            return None
        else:
            print("Ваш заказ принят")
            return Order(list_of_pizzas)

    def sent_oder_to_cook(self, customer_order):
        print("Ваш заказ будет готов чере 15 минут")
        return True

    def take_payment(self, customer_order):
        print("Сумма вашего заказа составляет: ", customer_order.count_total())
        print("Карта или наличные?")
        print("Оплата прошла успешно")
        return True


waiter_Mark = Waiter("Mark")
customer_order_Mark = waiter_Mark.take_oder()
if customer_order_Mark:
    payment_succeed = waiter_Mark.take_payment(customer_order_Mark)
    if payment_succeed:
        waiter_Mark.sent_oder_to_cook(customer_order_Mark)
