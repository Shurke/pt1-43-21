"""
This module is test module,
it tests task1 with unittests
-tests class Client
-tests class Reception
-tests class Entertainment
-tests class Restaurant

"""


import ddt
import io
import task2
import time
import unittest
from unittest.mock import patch


@ddt.ddt
class TestClient(unittest.TestCase):
    """Tests Client class

    tests '__init__' method
    tests 'delete' method

    """

    @ddt.data(('Sergey', 'Ivanov', 23, True), ('Polina', 'Smirnova', 10, 0))
    @ddt.unpack
    def test_valid_init(self, name, surname, days, all_incl):
        """valid tests of creating prototype of Client class"""
        prototype = task2.Client(name, surname, days, all_incl)
        self.assertEqual(name, prototype.name)
        self.assertEqual(surname, prototype.surname)
        self.assertEqual(days, prototype.days)
        self.assertEqual(all_incl, prototype.all_inclusive)
        self.assertEqual(0, prototype.money_debt)
        self.assertEqual(None, prototype.curr_room)

    @ddt.data(
        ((), 'Ivanov', 23, True),
        ([], 'Smirnova', 10, 0),
        ('Vita', ['Rowan'], 16, True),
        ('Vanya', {}, 10, False),
        ('Sasha', 'Rowan', {}, True),
        ('Jena', 'Howard', '34', False),
        ('Senya', "Got", 18, 'False'),
        ('Pavel', "Swan", 11, [0]),
        ('Anton', "Swanky", 0, False),
    )
    @ddt.unpack
    def test_negative_init(self, *args):
        """negative tests of creating prototype of Client class"""
        self.assertRaises(ValueError, task2.Client.__init__, *args)

    # def test_delete_client(self):
    #     """tests 'delete_client' method"""
    #     client = Client('Serge', 'Ivanov', 9, True)
    #     print(client)
    #     client.delete_client()
    #     print(client.name)


@ddt.ddt
class TestReception(unittest.TestCase):
    """Tests Reception class

    tests '__init__' method
    tests 'welcoming' method
    tests 'move_in' method
    tests 'change_room' method
    tests 'ask services' method
    tests 'moving_out' method
    tests 'get_client_info' method

    """

    @classmethod
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=[
        'Yana', 'Ivanova', 10, True, 'Ola', 'Downy', 12, False
    ])
    def setUpClass(cls, _, mock_stdout):
        """creates 2 samples of a class for future testing"""

        cls.person1 = task2.Reception()
        cls.person2 = task2.Reception()

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_welcoming(self, mock_stdout):
        """Tests 'welcoming' function"""

        task2.Reception.welcoming()
        expected = task2.Reception.welcome_words + '\n' + task2.Reception.get_info + '\n'
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['Vova', 'Sergeev', 18, False])
    def test_valid_init(self, _, mock_stdout):
        """tests valid cases of '__init__' method"""
        expected_room = 0
        for room in task2.Reception.rooms.keys():
            if task2.Reception.rooms[room] == 0:
                expected_room = room
                break
        visitor = task2.Reception()
        obj = task2.Reception.rooms[visitor.room_number]
        if obj.all_inclusive:
            money_debt_expected = obj.days * 150
        else:
            money_debt_expected = obj.days * 120
        phrase1 = 'Hello, we are glad to see you at our Hotel!\n'
        phrase2 = 'please enter your name, surname, duration in days and\n'
        phrase3 = '1 if you choose "all-inclusive" or 0 if you choose "standard" package:\n'
        phrase4 = f'Your room number is {expected_room}\n'
        phrase5 = f'payments for the duration - {money_debt_expected}\n'
        expected_phrase = phrase1 + phrase2 + phrase3 + phrase4 + phrase5
        self.assertFalse(obj == 0)
        self.assertEqual(money_debt_expected, obj.money_debt)
        self.assertEqual(mock_stdout.getvalue(), expected_phrase)
        self.assertEqual(expected_room, obj.curr_room)
        self.assertEqual(obj.curr_room, visitor.room_number)
        request_1 = task2.Reception(visitor.room_number)
        expect = f'Hello, {obj.name} {obj.surname}!\n' + task2.Reception.offer_help_message + '\n'
        self.assertEqual(expected_phrase + expect, mock_stdout.getvalue())
        self.assertEqual(request_1.room_number, visitor.room_number)

    @ddt.data(100, 401, 9, -101)
    def test_negative_init(self, room):
        """tests negative cases of '__init__' method"""
        self.assertRaises(task2.RoomNumberError, task2.Reception, room)

    def test_valid_get_client_info(self):
        """tests valid case of 'get_client_info' function"""
        visitor = task2.Reception.get_client_info(101)
        self.assertEqual(task2.Reception.rooms[101], visitor)

    @ddt.data('s', [103], (201,), 99)
    def test_negative_get_client_info(self, room):
        """tests negative case of 'get_client_info' function"""
        self.assertRaises(task2.RoomNumberError, task2.Reception.get_client_info, room)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_ask_service(self, mock_stdout):
        """tests valid cases of 'ask_service' function"""
        request = TestReception.person1
        request.ask_service('cleaning')
        self.assertEqual(mock_stdout.getvalue(), 'We will help you as soon as possible!\n')
        self.assertEqual('cleaning', task2.Reception.pending_service[request.room_number])

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_change_room(self, mock_stdout):
        """tests valid 'change room' cases"""
        client = TestReception.person1
        first_room = client.room_number
        expected_room = 0
        for room in task2.Reception.rooms.keys():
            if task2.Reception.rooms[room] == 0:
                expected_room = room
                break
        client.change_room('Sun side')
        phrase1 = 'Your room has been changed!\n'
        phrase2 = f'Now your room number is {expected_room}\n'
        expected_phrase = phrase1 + phrase2
        self.assertFalse(first_room == client.room_number)
        self.assertIn('Sun side', task2.Reception.problems_with_room)
        self.assertEqual(expected_phrase, mock_stdout.getvalue())

    def test_negative_change_room(self):
        """tests negative 'change room' cases"""
        client = TestReception.person1
        for room in task2.Reception.rooms:
            if task2.Reception.rooms[room] == 0:
                task2.Reception.rooms[room] = 1
        self.assertRaises(task2.RoomNumberError, client.change_room)
        for room in task2.Reception.rooms:
            if task2.Reception.rooms[room] == 1:
                task2.Reception.rooms[room] = 0

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_move_in(self, mock_stdout):
        """tests valid case of 'move_in' function"""
        person = task2.Client('Victor', 'Shem', 24, False)
        expected_room = 0
        for room in task2.Reception.rooms.keys():
            if task2.Reception.rooms[room] == 0:
                expected_room = room
                break
        task2.Reception.move_in(person)
        if person.all_inclusive:
            money_debt_expected = person.days * 150
        else:
            money_debt_expected = person.days * 120
        phrase1 = f'Your room number is {expected_room}\n'
        phrase2 = f'payments for the duration - {money_debt_expected}\n'
        self.assertEqual(money_debt_expected, person.money_debt)
        self.assertEqual(expected_room, person.curr_room)
        self.assertEqual(phrase1 + phrase2, mock_stdout.getvalue())

    def test_negative_move_in(self):
        """tests negative 'move in' cases"""
        person = task2.Client('Victoria', 'Shel', 20, True)
        for room in task2.Reception.rooms:
            if task2.Reception.rooms[room] == 0:
                task2.Reception.rooms[room] = 1
        self.assertRaises(task2.RoomNumberError, task2.Reception.move_in, person)
        for room in task2.Reception.rooms:
            if task2.Reception.rooms[room] == 1:
                task2.Reception.rooms[room] = 0

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_zmoving_out(self, mock_stdout):
        """tests 'moving_out' function"""
        client = TestReception.person1
        client_room_number = client.room_number
        debt = task2.Reception.rooms[client_room_number].money_debt
        client.moving_out()
        self.assertTrue(task2.Reception.rooms[client_room_number] == 0)
        phr1 = f'You have to pay {debt}$ for the duration\n'
        phr2 = 'Good Bye! Hope to see you next time at our Hotel!\nThank you for choosing us!\n'
        self.assertEqual(phr1 + phr2, mock_stdout.getvalue())


@ddt.ddt
class TestEntertainment(unittest.TestCase):
    """Tests Entertainment class

    tests '__init__' method
    tests 'play_casino' method
    tests 'swimming' method

    """

    @classmethod
    @patch('builtins.input', side_effect=['Vova', 'Bush', 14, True])
    @patch('sys.stdout', new_callable=io.StringIO)
    def setUpClass(cls, _, mock_stdout):
        visitor = task2.Reception()
        cls.entertainment_visitor = task2.Entertainment(visitor.room_number)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_swimming(self, mock_stdout):
        """tests valid case of 'swimming' function"""

        task2.Entertainment.swimming(4)
        s = time.strftime(time.ctime()).split()[3]
        if 7 < int(s[0]) * 10 + int(s[1]) < 22:
            self.assertEqual(
                mock_stdout.getvalue(),
                'We gave you 8 towels, you can swim until 22:00\n'
            )
        else:
            self.assertEqual(
                mock_stdout.getvalue(),
                'Unfortunately, swimming-pool is closed now,it opens at 7:00\n'
            )

    @ddt.data(0, -3, -99)
    def test_negative_case_swimming_value_error(self, persons):
        """tests negative cases of 'swimming' function with ValueError"""
        self.assertRaises(ValueError, task2.Entertainment.swimming, persons)

    @ddt.data('d', [4], (3,), {'person': 2})
    def test_negative_case_swimming_type_error(self, persons):
        """tests negative cases of 'swimming' function with TypeError"""
        self.assertRaises(TypeError, task2.Entertainment.swimming, persons)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_valid_play_casino(self, mock_stdout):
        """tests valid cases of 'play_casino' function"""

        player = TestEntertainment.entertainment_visitor
        first_debt = player.client.money_debt
        player.play_casino(100)
        ans = mock_stdout.getvalue().split('\n')
        if ans[1] == 'You have won 200 $':
            self.assertEqual(player.client.money_debt, first_debt - 100)
        else:
            self.assertEqual(player.client.money_debt, first_debt + 100)

    @ddt.data(0, -100, [2999], '100')
    def test_negative_play_casino(self, deposit):
        """tests negative cases of 'play_casino' function"""

        player = TestEntertainment.entertainment_visitor
        if isinstance(deposit, int):
            self.assertRaises(ValueError, player.play_casino, deposit)
        else:
            self.assertRaises(TypeError, player.play_casino, deposit)


@ddt.ddt
class TestRestaurant(unittest.TestCase):
    """Tests Restaurant class

    tests '__init__' method
    tests 'buy_alcohol' method
    tests 'order_delicacy' method

    """

    @classmethod
    @patch('builtins.input', side_effect=[
        'Vova', 'Bush', 15, True, 'Anna', 'Mil', 10, False
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def setUpClass(cls, _, mock_stdout):
        visitor1 = task2.Reception()
        cls.visitor2 = task2.Reception()
        cls.restaurant_visitor1 = task2.Restaurant(visitor1.room_number)

    @patch('builtins.input', side_effect=['y', 'N'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_init(self, _, mock_stdout):
        """tests '__init__ method'"""
        first_debt = task2.Reception.rooms[TestRestaurant.visitor2.room_number].money_debt
        guest_1 = task2.Restaurant(TestRestaurant.visitor2.room_number)
        self.assertEqual(first_debt + 15, guest_1.client.money_debt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_buy_alcohol(self, mock_stdout):
        """tests 'buy_alcohol' function"""
        guest = TestRestaurant.restaurant_visitor1
        first_debt = guest.client.money_debt
        guest.buy_alcohol('Red Wine')
        self.assertEqual(f'Red Wine costs 15$, {guest.client.name}\n', mock_stdout.getvalue())
        self.assertEqual(first_debt + 15, guest.client.money_debt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_order_delicacy(self, mock_stdout):
        """tests 'order_delicacy' function"""
        guest = TestRestaurant.restaurant_visitor1
        first_debt = guest.client.money_debt
        guest.order_delicacy('Crab')
        expected = f'You will pay 20$ for Crab, {guest.client.name}\n'
        self.assertEqual(expected, mock_stdout.getvalue())
        self.assertEqual(first_debt + 20, guest.client.money_debt)


if __name__ == '__main__':
    unittest.main()
