import task1
import unittest


def test1():
    t = task1.prod1()
    t2 = task1.Product()
    assert t == t2


def test2():
    t3 = task1.invent1.addProduct()
    t4 = task1.invent1.removeProduct()
    assert t3 == 3 and t4 == 2


if __name__ == "__main__":
    unittest.main()
