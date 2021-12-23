from task1 import Order
from task1 import Pizza
from task1 import Waiter

import unittest


class TestPizza(unittest.TestCase):
    """Test cases for the Pizza Class."""
    def setUp(self):
        ingredients = ["Моцарелла", "базилик", "томатный соус", "помидоры"]
        size = "medium"
        self.pizza = Pizza(ingredients, size)

    def test_size(self):
        """проверяет размер пиццы"""
        self.assertEqual(self.pizza.size, "medium")

    def test_ingredients(self):
        """проверяет ингредиенты пиццы"""
        ingredients_expected = ["Моцарелла", "базилик", "томатный соус", "помидоры"]
        self.assertEqual(self.pizza.ingredients, ingredients_expected)

    def test_str(self):
        """проверяет строковое представление пиццы"""
        self.assertEqual(str(self.pizza), "Сырная пицца")

    def test_price(self):
        """проверяет расчет цены товара"""
        self.assertEqual(self.pizza.price(), 15.6)


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
