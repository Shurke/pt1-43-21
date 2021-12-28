'''Проект Эйлера №451
Обратные по модулю числа

Рассмотрим число 15.
Существует восемь натуральных чисел меньше 15,
которые являются взаимно простыми с 15: 1, 2, 4, 7, 8, 11, 13, 14.
Числами, обратными этим восьми по модулю 15, являются: 1, 8, 4, 13, 2, 11, 7, 14
так как
1*1 mod 15=1
2*8=16 mod 15=1
4*4=16 mod 15=1
7*13=91 mod 15=1
11*11=121 mod 15=1
14*14=196 mod 15=1
Пусть I(n) будет наибольшим положительным числом m меньше n-1, таким что число,
обратное числу m по модулю n равно самому же m.
Таким образом, I(15)=11.
Также, I(100)=51 и I(7)=1.
Найдите ∑I(n) для 3≤n≤2*10**7
'''


def great_comm_divisor(a, b):
    '''Находит НОД 2х чисел'''

    if a < b:
        while b:
            (a, b) = (b, a % b)
        return a
    while a:
        (b, a) = (a, b % a)
    return b


def mutually_simple_list(n: int = 15) -> list:
    '''Создает список взаимно простых чисел от 1 до n'''

    lst_1 = [el for el in range(1, n) if great_comm_divisor(n, el) == 1]
    return lst_1


def modulo_inverse_list(lst: list, n: int) -> list:
    '''Создает урезанный список чисел обратных числам из lst по модулю n в диапазоне от 1 до n-1,

    состоящий только из элементов равных себе же обратным по модулю
    '''

    back_lst = [i for i in lst if (i * i) % n == 1 and i < n - 1]
    return back_lst


def max_m(n):
    '''Yаходит наибольшее положительное число m,

    такое, что число обратное m по модулю n равно самому m
    '''

    if n < 2:
        return 1
    b = modulo_inverse_list(mutually_simple_list(n), n)
    m = b[-1]
    return m
    pass


def sum_func(ranges):
    '''Находит ∑max_m(n) для диапазона ranges'''

    summ = 0
    for i in ranges:
        summ += max_m(i)
    return summ
    pass


# sum_func(range(3, 2 * 10**7))
sum_func([7, 15, 100])
