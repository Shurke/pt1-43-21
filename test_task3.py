from task3 import n
import unittest


class t_test(unittest.TestCase):

    def test_1(self):
        self.assertTrue(n == ['c', 'd', 'e'])


if __name__ == "__main__":
    unittest.main()
