"""Проект Эйлера
Задача 71
Упорядоченные дроби
https://euler.jakumo.org/problems/view/71.html

Перечислив множество сокращенных правильных дробей для d ≤ count
в порядке возрастания их значений,
найдите числитель дроби, расположенной непосредственно слева от дроби search_fraction.

дробь представляется кортежом-парой (числитель, знаменатель)
"""

 
class StringWithoutSlash(Exception):
    def __init__(self, message):
        self.txt = message


def gcd(a: int, b: int) -> int:   # Наибольший общий делитель (алгоритм Евклида)
    while b > 0:
        a, b = b, a % b
    return a


def simplify(fraction: tuple) -> tuple:  # сокращение дроби
    g = gcd(fraction[0], fraction[1])
    return fraction[0] // g, fraction[1] // g


def search_left_numerator(count: int, search_fraction: str) -> str:
    if search_fraction.find("/") == -1:
        raise StringWithoutSlash("Второй аргумент вызова функции search_left_numerator "
                                 "должен быть дробью.")
    search_fraction_list = search_fraction.split('/')
    search_fraction_numerator = int(search_fraction_list[0])
    search_fraction_denominator = int(search_fraction_list[1])
    t = []
    prev_numerator = None
    result = None
    for num in range(1, count+1):          # цикл по всем числителям
        for den in range(num+1, count+1):  # цикл по всем знаменателям
            pair = simplify((num, den))    # очередная дробь
            t.append(pair)                 # добавим к списку
    s = list(set(t))  # устраняем дубликаты - превращаем список во множество
    for q in sorted(s, key=lambda x: x[0] / x[1]):  # сортируем по величине частного (в виде float)
        print(str(q[0]) + "/" + str(q[1]))
        if str(q[0]) == str(search_fraction_numerator) \
                and str(q[1]) == str(search_fraction_denominator):
            print("Числитель дроби, расположенной непосредственно слева от дроби",
                  str(search_fraction), "-", prev_numerator)
            result = prev_numerator
            break
        prev_numerator = str(q[0])
    return result


search_left_numerator(100, "3/7")
