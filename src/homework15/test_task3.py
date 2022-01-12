'''
Tests for homework15 task3
'''

import task3
import unittest


class TestTask(unittest.TestCase):

    def test_type(self):
        """Test for function input type"""
        self.assertRaises(TypeError, task3.task_func, 2132131)
        self.assertRaises(TypeError, task3.task_func, 99.9293123)
        self.assertRaises(TypeError, task3.task_func, False)
        self.assertRaises(TypeError, task3.task_func, (123, 3213, 1231231))

    def test_result(self):
        """Test for result equality"""
        self.assertEqual(task3.task_func("1 1 1"), 2)
        self.assertEqual(task3.task_func("1 1 1 1"), 6)


if __name__ == '__main__':
    unittest.main()
