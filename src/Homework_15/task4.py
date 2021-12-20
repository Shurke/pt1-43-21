"""
Домашняя 5. Задача 4.
Задача 69. Функция эйлера рассчитывается по формуле, есть в интернетах и
учебнике Бухштаба, там просто.

Задача 69.

Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества
чисел, меньших n, которые взаимно просты с n. К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти
и взаимно просты с девятью, φ(9)=6.

n 	Взаимно простые числа 	φ(n) 	n/φ(n)
2 	1 	                    1 	    2
3 	1,2 	                2 	    1.5
4 	1,3 	                2 	    2
5 	1,2,3,4 	            4 	    1.25
6 	1,5 	                2 	    3
7 	1,2,3,4,5,6 	        6 	    1.1666...
8 	1,3,5,7 	            4 	    2
9 	1,2,4,5,7,8 	        6 	    1.5
10 	1,3,7,9 	            4 	    2.5

Нетрудно заметить, что максимум n/φ(n) наблюдается при n=6, для n ≤ 10.

Найдите значение n ≤ 1 000 000, при котором значение n/φ(n) максимально.
"""


class Iterable:
    """
    Iterable class.
    The default argument can take a number or an iterable object (list, tuple).
    If nothing is transmitted - it prompts the user to enter the number 'n' and
    generate a sequence from 0 to 'n'
    """
    def __init__(self, collection=None):
        if collection is None:
            n = int(input('Enter max "n": '))
            if n <= 1:
                raise ValueError('Enter a natural number greater than 1!')
            self._collection = [_ for _ in range(1, n + 1)]
        else:
            if type(collection).__name__ not in ('list', 'tuple'):
                raise TypeError("The type of the iterable must be 'list' or 'tuple'")
            self._collection = collection

    def __iter__(self):
        return Iterator(self._collection)


class Iterator:
    """
    Iterator combined with the Euler function and returning the ratio of the number 'n'
    to the value of the Euler function.
    """
    max_num = 0, 0

    def __init__(self, collection):
        self.collection = collection
        self.cursor = 0

    def __iter__(self):
        return self

    @staticmethod
    def euler(num):
        """
        Euler's function takes a natural number as input and outputs the number of coprime numbers
        :param num: natural number
        :return: the coprime numbers
        """
        prime_number = 2
        result = 1
        count = 0
        while True:
            if num % prime_number == 0:
                count += 1
                num /= prime_number
                if count == 1:
                    result *= prime_number - 1
                elif count > 1:
                    result *= prime_number
            else:
                prime_number += 1
                count = 0
            if prime_number > num:
                break
        return result

    def __next__(self):
        if self.cursor >= len(self.collection):
            raise StopIteration
        elem = self.collection[self.cursor]
        self.cursor += 1
        num = elem / self.euler(elem)
        if num > self.max_num[1]:
            self.max_num = elem, num
        return self.max_num


def task4(collection=None):
    """
    Function for iteration start.
    :param collection: iterable object must be 'list' or 'tuple', or one number 'int' type
    :return: the maximum ratio of 'n' to the Euler(n) function
    """
    if type(collection).__name__ == 'int':
        element = collection, collection / Iterator.euler(collection)
    elif collection is None:
        for element in Iterable():
            pass
    else:
        for element in Iterable(collection):
            pass
    return f'n = {element[0]}; max n/Euler(n) = {element[1]}'
