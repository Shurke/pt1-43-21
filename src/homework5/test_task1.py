"""Tests for task1.py."""

import unittest

from task1 import main


class TestMain(unittest.TestCase):
    """Test case for the main() function."""

    def test_output(self):
        """Test values of the of the dictionary returned by main()."""
        self.assertEqual(
            main(),
            {
                1: 1, 2: 8, 3: 27, 4: 64, 5: 125,
                6: 216, 7: 343, 8: 512, 9: 729, 10: 1000,
                11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375,
                16: 4096, 17: 4913, 18: 5832, 19: 6859, 20: 8000
            }
        )


if __name__ == '__main__':
    unittest.main()
