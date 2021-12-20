"""
Рассмотрим дробь n/d, где n и d являются натуральными числами.
Если n<d и НОД(n,d) = 1, то речь идет о сокращенной правильной дроби.
Если перечислить множество сокращенных правильных дробей для d ≤ 8
в порядке возрастания их значений, получим:
1/8, 1/7, 1/6, 1/5, 1/4, 1/3, 1/2, 2/7, 3/8, 2/5, 3/7, 4/7,
3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
Нетрудно заметить, что данное множество состоит из 21 элемента.
Из скольки элементов будет состоять множество
сокращенных правильных дробей для d ≤ 1 000 000?
"""


from math import gcd


def num_of_nat_fract(max_denominator):
    if max_denominator <= 0:
        raise ValueError("Знаменатель не может быть меньше или равен 0!")
    if type(max_denominator) is not int:
        raise TypeError("Знаменатель может быть только целым числом!")
    counter = 0
    numerator = 1
    while numerator < max_denominator:
        denominator = max_denominator
        while denominator > 1:
            if numerator < denominator and gcd(numerator, denominator) == 1:
                counter += 1
            denominator -= 1
        numerator += 1
    return counter


num = int(input("Максимальный знаменатель: "))
print(f"Правильных дробей: {num_of_nat_fract(num)}")
