"""
Определим F(m,n) как количество кортежей положительных чисел длиной n,
произведение всех элементов которых не превышает m.

F(10, 10) = 571.

F(10**6, 10**6) mod 1 234 567 891 = 252903833.

Найдите F(10**9, 10**9) mod 1 234 567 891.

Переменные функции main:
module - делитель
in_number - граничное число и длина кортежей
segm_number - количество этапов (сегментов) при расчете


"""

import math
import sys


class Prime:
    @staticmethod
    def get(n):
        """Создание списка простых чисел в диапазоне n, начиная с двойки."""
        primes = []
        visited = [False] * (n + 1)

        for i in range(2, n + 1):
            if not visited[i]:
                primes.append(i)
                # Вычеркивание мест непростых чисел
                for j in range(i * i, n + 1, i):
                    visited[j] = True
        return primes


class BinomialCoefficient:
    """Создание словарей биномиальных коэффициентов С(n,m)."""
    def __init__(self, mod):
        """Делитель."""
        self.mod = mod
        self.cache = {}

    def get(self, n, m):

        # Создание значения ключа - пустого словаря
        if n not in self.cache:
            self.cache[n] = {}

        # Если m нет в словаре с ключом n
        if m not in self.cache[n]:
            result = 1

            # Расчет биномиальных коэффициентов
            for i in range(1, m + 1):
                result = result * (n - i + 1) // i
            self.cache[n][m] = result % self.mod
        return self.cache[n][m]


class SieveAlgorithm:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.binomial_coefficient = BinomialCoefficient(mod)

        # Из класса Prime - список простых чисел в диапазоне корня из n, округленном вниз
        self.basic_primes = Prime().get(math.floor(math.sqrt(n)))
        self.solution_count_cache = {}

    def get_range(self, begin, end):
        """Расчет списка биномиальных коэффициентов в заданном сегменте расчета."""
        if begin > end:
            return []
        number_list = [i for i in range(begin, end + 1)]
        result_list = [1 for i in range(begin, end + 1)]

        for p in self.basic_primes:
            p_begin_pos = 0
            if begin % p != 0:
                p_begin_pos = p - (begin % p)
            for i in range(p_begin_pos, end - begin + 1, p):
                e = 0
                while number_list[i] % p == 0:
                    number_list[i] //= p
                    e += 1
                result_list[i] = (result_list[i] * self.__get_solution_count(e)) % self.mod

        for i in range(end - begin + 1):
            if number_list[i] > 1:
                result_list[i] = (result_list[i] * self.n) % self.mod
        return result_list

    def __get_solution_count(self, e):
        """Извлечение биномиального коэффициента?"""
        if e not in self.solution_count_cache:
            self.solution_count_cache[e] = self.binomial_coefficient.get(self.n + e - 1, e)
        return self.solution_count_cache[e]


class Problem:
    def __init__(self, mod, input_number, segm):
        # Задание делителя нацело
        self.mod = mod
        self.input_number = input_number
        self.segm = segm

    def solve(self):
        """Лишняя функция."""
        out_number = self.get(self.input_number, self.segm)
        print(out_number)
        return out_number

    def get(self, n, segment_count):
        """Расчет количества кортежей по сегментам расчета и вывод общего количества кортежей."""
        # Проверка, что целевое число делится на количество сегментов нацело. Если нет - ошибка.
        assert n % segment_count == 0

        # Определение длины сегмента
        segment_len = n // segment_count

        sieve_algorithm = SieveAlgorithm(n, self.mod)
        total_count = 0

        for i in range(segment_count):
            solution_count_list = sieve_algorithm.get_range(i * segment_len + 1,
                                                            (i + 1) * segment_len)
            count = sum(solution_count_list) % self.mod
            total_count = (total_count + count) % self.mod
            print('current =>', i * segment_len + 1, (i + 1) * segment_len,
                  '=>', count, '=>', total_count)
        return total_count


def main():
    module = int(input('Введите делитель: '))
    in_number = int(input('Введите верхнюю границу произведений: '))
    segm_number = int(input('Введите количество блоков расчета: '))

    problem = Problem(module, in_number, segm_number)
    problem.solve()


if __name__ == '__main__':
    sys.exit(main())
