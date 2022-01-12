"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
ведет учет различных продуктов и считает общую стоимость инвентаря"""


class Product:
    def __init__(self, p_id, name, price, quantity):
        """Инициализирует атрибуты"""
        self.price = price
        self.id = p_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.new_price = new_price

    @property
    def new_price(self):
        return self.new_price

    @new_price.setter
    def new_price(self, new_pricenew):
        if new_pricenew <= 0:
            self.new_price = new_pricenew
        else:
            print("Ошибка! Невозможно обновить цену до нуля или ниже")

    def update_quantity(self, new_quantity, is_increment):
        """Позволяет обновлять коли товара путем увел или умен кол зависимости от isIncrement."""
        if is_increment is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print("Ошибка, дальнейшее сокращение невозможно!")

    def get_quantity(self):
        """Возвращает текущее количество товара."""
        return self.quantity

    def view_product(self):
        """Отображает информацию о продукте посредством печати"""
        print('Product ID: ' + str(self.id) + ", Name: " + self.name + ", "
                                                                       "Price: " + str(
            self.price) + ', Quantity: ' + str(self.quantity))


class Inventory:
    def __init__(self):
        """Инициализирует атрибут"""
        self.list_prod = []

    def add_product(self, pId):
        """Добавить новый товар в список"""
        self.list_prod.append(pId)

    def remove_product(self, pId):
        """удаляет товар из списка"""
        if pId in self.list_prod:
            self.list_prod.remove(pId)
        else:
            print("Ошибка. Товара нет на складе.")

    def view_inventory(self):
        """Отображает список инвентаря через печать"""
        print(self.list_prod)


if __name__ == '__main__':
    prod1 = Product(1, "colgate", 2.20, 10)
    print(prod1.get_quantity(), prod1.update_quantity(2, True), prod1.view_product())

    invent1 = Inventory()
    invent1.add_product(3)
    invent1.remove_product(2)
    invent1.view_inventory()
