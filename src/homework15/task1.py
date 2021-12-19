""" Задача 1. Реализована модель заказа пиццы из различных ингредиентов

Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции
различных действий. Программа должна инстанцировать объекты и эмулировать
какую-либо ситуацию - вызывать методы, взаимодействие объектов и т.д.
"""
import random


class Order:
    """Класс преднозначен для работы с заказом
    Для создания экземпляра класса необходимо передать список пицц: list_of_pizzas
    Умеет подсчитывать стоимость заказа: count_total"""
    def __init__(self, list_of_pizzas):
        self.list_of_pizzas = list_of_pizzas

    def __str__(self):
        list_of_pizza_names = map(str, self.list_of_pizzas)
        return ", ".join(list_of_pizza_names)

    def count_total(self):
        total = 0
        for pizza in self.list_of_pizzas:
            total = total + pizza.price()
        return total


class Pizza:
    """Класс предназначен для создания пиццы
    Для создания экземпляра небходимо передать инредиенты: ingredients, и размер пиццы: size.
    Хранит список возможных ингридитентов: available_ingredients, а так же их цены: ingredients_prices.
    Хранит стоимость приготовления пиццы: cost_to_cook.
    Хранит виды размеров пицы: sizes и коэффициенты изменения цены от размера: price_correction.
    Умее расчитать цену пиццы: price"""

    cost_to_cook = 7
    sizes = (
        "small",
        "medium",
        "big",
    )
    price_correction = {
        "small": 1,
        "medium": 1.3,
        "big": 1.5,
    }
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

    def __str__(self):
        meat = {
            "бекон",
            "куриное филе",
            "ветчина",
        }
        sea = {
            "морской коктейль из мидий",
            "мини-осьминоги",
            "кальмары",
            "креветки",
        }
        cheese = {
            "Моцарелла",
            "Пармезан",
            "Эмменталь",
            "сыр Дорблю",
        }
        vegetarian = {
           "каперсы",
           "маслины",
           "петрушка",
           "орегано",
           "базилик",
           "сельдерей",
           "томатный соус",
           "помидоры",
        }
        names_for_pizza = {
            "Морская пицца": sea,       
            "Мясная пицца": meat,
            "Сырная пицца": cheese,
            "Вегетарианская пицца": vegetarian,
        }
        set_ingredients = set(self.ingredients)
        for name_of_pizza, main_ingredients in names_for_pizza.items():
            if main_ingredients & set_ingredients:
                return name_of_pizza
        return "Оригинальная пицца"

    def price(self):
        """Считаем в зависимости от размера и ингридиентов и стоимости услуги приготовления"""
        total = self.cost_to_cook
        for ingredient in self.ingredients:
            total = total + self.ingredients_prices[ingredient]
        total = total * self.price_correction[self.size]
        return round(total, 2)


class Waiter:
    """Класс приеднозначени для работы с клиентом
    При создании класса необходимо передать имя официанта: name
    Умеет принимать заказ: take_oder
    Умет отправлять заказ на кухню: sent_oder_to_cook
    Умет принимать оплату take_payment"""
    def __init__(self, name):
        self.name = name

    def take_oder(self):
        list_of_pizzas = []
        print("Добрый день, меня зовут " + self.name + ".",
              "Я готов принять ваш заказ, Давайте выберем пиццы.")
        one_more_pizza = True
        while one_more_pizza:
            ingredients = []
            print("Выберите размер пиццы: ", ", ".join(Pizza.sizes))
            size = self.random_choose(Pizza.sizes)
            print("Вы выбрали пиццу размера " + size)
            print("Вы можете выбрать следующие ингредиенты: ")
            for ingredient in Pizza.available_ingredients:
                print("\033[1;34;47m", ingredient, "\033[0;0m")

            ingredients_to_choose = list(Pizza.available_ingredients)
            random_number_of_ingredients = random.randint(0, len(ingredients_to_choose) - 1)
            for i in range(random_number_of_ingredients):
                ingredient = self.random_choose(ingredients_to_choose)
                ingredients.append(ingredient)
                ingredients_to_choose.remove(ingredient)

            if len(ingredients) == 0:
                print("К сожалению, вы не выбрали ингредиенты для пиццы")
                one_more_pizza = False
            else:
                print("Вы выбрали следующте ингредиенты: ", ", ".join(ingredients), ". Хороший выбор.")
                new_pizza = Pizza(ingredients, size)
                list_of_pizzas.append(new_pizza)
            print("Готовы заказать еще одну пиццу?")
            one_more_pizza = self.random_choose((True, False))
            print("ок")

        if len(list_of_pizzas) == 0:
            print("Ваш заказ не принят")
            return None
        else:
            print("Ваш заказ принят")
            return Order(list_of_pizzas)

    def sent_oder_to_cook(self, customer_order):
        print("Кухня приняла заказ официанта " + self.name)
        print("Ваш заказ ", customer_order, " будет готов чере 15 минут")
        return True

    def take_payment(self, customer_order):
        print("Сумма вашего заказа составляет: ", customer_order.count_total())
        print("Офииант " + self.name + " принял оплату от клиента.")
        return True

    @staticmethod
    def random_choose(list_of_elements):
        return list_of_elements[random.randint(0, len(list_of_elements) - 1)]


waiter_Mark = Waiter("Mark")
customer_order_Mark = waiter_Mark.take_oder()
if customer_order_Mark:
    payment_succeed = waiter_Mark.take_payment(customer_order_Mark)
    if payment_succeed:
        waiter_Mark.sent_oder_to_cook(customer_order_Mark)
