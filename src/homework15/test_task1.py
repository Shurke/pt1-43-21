from ddt import data
from ddt import ddt
from ddt import unpack

from task1 import Order
from task1 import Pizza
from task1 import Waiter

import unittest


@ddt
class TestPizza(unittest.TestCase):
    """Test cases for the Pizza Class."""

    @data(
        (
         "medium",
         "medium",
         ["Моцарелла", "базилик", "томатный соус", "помидоры"],
         ["Моцарелла", "базилик", "томатный соус", "помидоры"]
         ),
        ("big",
         "big",
         ["куриное филе", "ветчина", "Моцарелла"],
         ["куриное филе", "ветчина", "Моцарелла"]
         ),
    )
    @unpack
    def test_size_ingredients(self, size_input, size_output, ingredients_input, ingredients_output):
        pizza = Pizza(ingredients_input, size_input)
        """проверяет размер и ингредиенты пиццы"""
        self.assertEqual(pizza.size, size_output)
        self.assertEqual(pizza.ingredients, ingredients_output)

    @data(
        ("medium",
         ["Моцарелла", "базилик", "томатный соус", "помидоры"],
         "Сырная пицца"
         ),
        ("big",
         ["куриное филе", "ветчина", "Моцарелла"],
         "Мясная пицца"
         ),
    )
    @unpack
    def test_str(self, size_input, ingredients_input, expected_str):
        """проверяет строковое представление пиццы"""
        pizza = Pizza(ingredients_input, size_input)
        self.assertEqual(str(pizza), expected_str)

    @data(
        ("medium",
         ["Моцарелла", "базилик", "томатный соус", "помидоры"],
         15.6
         ),
        ("big",
         ["куриное филе", "ветчина", "Моцарелла"],
         19.5
         ),
    )
    @unpack
    def test_price(self, size_input, ingredients_input, expected_price):
        """проверяет расчет цены товара"""
        pizza = Pizza(ingredients_input, size_input)
        self.assertEqual(pizza.price(), expected_price)


class TestOrder(unittest.TestCase):
    """Test cases for the Order Class."""
    def setUp(self):
        ingredients = ["Моцарелла", "базилик", "томатный соус", "помидоры"]
        size = "medium"
        self.pizza1 = Pizza(ingredients, size)
        ingredients = ["Моцарелла", "базилик", "томатный соус", "помидоры", "ветчина"]
        size = "big"
        self.pizza2 = Pizza(ingredients, size)
        self.order = Order([self.pizza1, self.pizza2])

    def test_list_of_pizzas(self):
        """проверяет спискок пицц"""
        self.assertEqual(self.order.list_of_pizzas, [self.pizza1, self.pizza2])

    def test_count_total(self):
        """проверяет расчет суммы заказа"""
        self.assertEqual(self.order.count_total(), 36.6)


class TestWaiter(unittest.TestCase):
    """Test cases for the Order Class."""
    def setUp(self):
        self.waiter = Waiter("Masha")

    def test_name(self):
        """проверяет имя официанта"""
        self.assertEqual(self.waiter.name, "Masha")


if __name__ == "__main__":
    unittest.main()
