'''Заказ пиццы в интернет-магазине с возможностью пополнения счета и накопления бонусных баллов.

Реализовано: создание аккаунта покупателя, пополнение счета,
создание корзины, выбор товаров с ценой зависимой от размера порции, удаление товаров из корзины,
оплата заказа(включая списание средств со счета и начисление бонусных баллов с каждого заказа)

-реализовать возможность оплаты части заказа бонусными баллами?
-пользовательский интерфейс?
-бд с кол-вом товара доступным к заказу("на складе")?
-история заказов?
'''


class Item:

    def __init__(self, name, quantity, type_of, price):
        self.name = name
        self.quantity = quantity
        self.type_of = type_of
        self.price = price

    def __str__(self):
        'Информация о товаре'

        print(self.name)
        print(self.quantity)
        print(self.type_of)
        print(self.size)


class Pizza(Item):

    def __init__(self, quantity, type_of, size):
        self.name = self.__class__.__name__
        self.type_of = type_of
        self.quantity = quantity
        self.size = size
        match size:
            case 'M':
                self.price = 20
            case 'L':
                self.price = 25
            case 'XL':
                self.price = 30
        

class Potatoes(Item):

    pass


class Drink(Item):

    def __init__(self, quantity, type_of, size):
        self.name = self.__class__.__name__
        self.type_of = type_of
        self.quantity = quantity
        self.size = size
        match size:
            case '0.25':
                self.price = 2
            case '0.5':
                self.price = 3
            case '1':
                self.price = 4


class Salad(Item):

    def __init__(self, quantity, type_of, size):
        self.name = self.__class__.__name__
        self.type_of = type_of
        self.quantity = quantity
        self.size = size
        match size:
            case 'M':
                self.price = 6
            case 'L':
                self.price = 8


class Souce(Item):

    def __init__(self, quantity, type_of):
        self.name = self.__class__.__name__
        self.type_of = type_of
        self.quantity = quantity
        self.price = 1


class Customer:

    def __init__(self, name='Unknown'):
        self.__current_account = 0
        self.name = name
        self.loyalty = 0

    def top_up_current_account(self, top_up_summ):
        '''Пополнение текущего баланса на сумму top_up_summ'''

        self.__current_account = self.__current_account + top_up_summ

    def top_down_current_account(self, top_down_summ):
        '''Списание с текущего баланса на сумму top_down_summ'''

        if self.__current_account < top_down_summ:
            print('Пополните баланс')
            raise ValueError('Недостаточно средств')
        self.__current_account = self.__current_account - top_down_summ

    def top_up_loyalty(self, bonus_loyalty):
        '''Начисление бонусных баллов'''

        self.loyalty = self.loyalty + bonus_loyalty

    def __str__(self):
        '''Информация о счете клиента'''

        name = str(self.name)
        current_account = 'Сумма на счете - ' + str(round(self.__current_account, 2))
        loyalty_summ = 'Сумма бонусных баллов - ' + str(self.loyalty)
        return '{}, {}, {}'.format(self.name, current_account, loyalty_summ)


class Cart:

    def __init__(self):
        self.items_in_cart = {}
        self.quantity_in_cart = 0
        self.cart_value = 0
        self.current_quantity = 0

    def add_to_cart(self, item):
        '''Добавление товара в корзину'''

        if not self.items_in_cart.get((item.name, item.type_of)):
            self.items_in_cart[(item.name, item.type_of)] = item.quantity
        else:
            self.current_quantity = self.items_in_cart[(item.name, item.type_of)]
            self.items_in_cart.update(
                {(item.name, item.type_of): self.current_quantity + item.quantity})
        self.quantity_in_cart += item.quantity
        self.cart_value += item.price * item.quantity

    def remove_from_cart(self, item):
        '''Удаление товара из корзины'''

        del self.items_in_cart[item.type_of]
        self.quantity_in_cart -= item.quantity
        self.cart_value -= item.price * item.quantity

    def __str__(self):
        '''Отображение информации о заказе'''

        a = ""
        for item in self.items_in_cart:
            a += f'{item[0]}  {item[1]} - {self.items_in_cart[item]} шт\n'

        return (f'Ваш заказ составил:\n\
            \r{{}}\
            \rКол-во товаров в корзине - {{}}\n\
            \rСумма к оплате - {{}}'.format(a,
                                            self.quantity_in_cart,
                                            self.cart_value)
                )


class Payment:

    def __init__(self, payer, cart_to_pay):
        self.payer = payer
        self.cart_to_pay = cart_to_pay

    def payment(self):
        '''Операция оплаты'''

        print(f'С вашего счета будет снято {self.cart_to_pay.cart_value}')
        self.payer.top_down_current_account(self.cart_to_pay.cart_value)

    def bonus_loyalty_from_order(self):
        '''Начисление бонусных балло в случае успешной оплаты'''

        bonus_loyalty = self.cart_to_pay.cart_value * 0.05
        self.payer.top_up_loyalty(bonus_loyalty)
        print(f'На ваш бонусный счет зачислено {bonus_loyalty} бонусных баллов!')


customer = Customer('Andrei Barysevich')
customer.top_up_current_account(555.55)


pizza_1 = Pizza(1, 'pepperoni', 'L')
pizza_2 = Pizza(2, 'meat', 'XL')
drink_1 = Drink(1, 'Coca-cola', '0.5')
cart_1 = Cart()

cart_1.add_to_cart(pizza_1)
cart_1.add_to_cart(pizza_2)
cart_1.add_to_cart(pizza_2)
cart_1.add_to_cart(drink_1)


print(cart_1)

payment_1 = Payment(customer, cart_1)

payment_1.payment()
payment_1.bonus_loyalty_from_order()

print(customer)
