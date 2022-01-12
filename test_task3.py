from task3 import list1
from task3 import n
import unittest


class t_test(unittest.TestCase):

    def test_1(self):
        if list1 == ['a', 'b', 'b', 'c', 'd', 'e', 'a']:
            self.assertEqual(n == ['c', 'd', 'e'])


if __name__ == "__main__":
    unittest.main()
