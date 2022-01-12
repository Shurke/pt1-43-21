'''
Tests for homework15 task4
'''

import task4
import unittest


class TestTask(unittest.TestCase):

    def test_type(self):
        """Test for function input type"""
        self.assertRaises(TypeError, task4.euler_task_69, 2132131)
        self.assertRaises(TypeError, task4.euler_task_69, 1.23)

    def test_result(self):
        """Test for result equality"""
        self.assertEqual(task4.euler_task_69(1000000), 510510)
        self.assertEqual(task4.euler_task_69(1000000), 1)
        self.assertEqual(task4.euler_task_69(1000), 12312)


if __name__ == '__main__':
    unittest.main()
