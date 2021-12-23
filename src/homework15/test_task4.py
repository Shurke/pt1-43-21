""" test task3"""


from task4 import Problem
import pytest
import unittest


class TestProblem(unittest.TestCase):
    """Test cases for the Problem Class."""

    def setUp(self):
        self.p = Problem()

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_output(self):
        """Test for proper output."""
        self.p.solve()
        captured = self.capsys.readouterr()
        self.assertEqual(captured.out.strip(), "Fast => 2647787126797397063")
