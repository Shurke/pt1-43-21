"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают ситуацию.
Объекты должны содержать как атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
ведет учет различных продуктов и считает общую стоимость инвентаря"""


class Product:
    def __init__(self, pId, name, price, quantity):
        """Инициализирует атрибуты"""
        self.id = pId
        self.name = name
        self.price = price
        self.quantity = quantity

    def updatePrice(self, new_price):
        """Обновляет цену товара"""
        if new_price > 0:
            print("Ошибка! Невозможно обновить цену до нуля или ниже")
        else:
            self.price = new_price

    def updateQuantity(self, new_quantity, isIncrement):
        """Позволяет обновлять коли товара путем увел или умен кол зависимости от isIncrement."""
        if isIncrement is True:
            self.quantity += new_quantity
        elif (self.quantity - new_quantity) >= 0:
            self.quantity -= new_quantity
        else:
            print("Ошибка, дальнейшее сокращение невозможно!")

    def getQuantity(self):
        """Возвращает текущее количество товара."""
        return self.quantity

    def viewProduct(self):
        """Отображает информацию о продукте посредством печати"""
        print('Product ID: ' + str(self.id) + ", Name: " + self.name + ", "
              "Price: " + str(self.price) + ', Quantity: ' + str(self.quantity))


class Inventory:
    def __init__(self):
        """Инициализирует атрибут"""
        self.listProd = []

    def addProduct(self, pId):
        """Добавить новый товар в список"""
        self.listProd.append(pId)

    def removeProduct(self, pId):
        """удаляет товар из списка"""
        if pId in self.listProd:
            self.listProd.remove(pId)
        else:
            print("Ошибка. Товара нет на складе.")

    def viewInventory(self):
        """Отображает список инвентаря через печать"""
        print(self.listProd)


if __name__ == '__main__':
    prod1 = Product(1, "colgate", 2.20, 10)
    print(prod1.getQuantity(), prod1.updateQuantity(2, True), prod1.viewProduct())

    invent1 = Inventory()
    invent1.addProduct(3)
    invent1.removeProduct(2)
    invent1.viewInventory()
