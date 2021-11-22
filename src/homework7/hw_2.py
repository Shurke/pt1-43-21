'''
Homework 2 tasks
'''

import math
import string


def task_2_1():
    print('Введите цену одного товара, руб')
    rub = int(input())
    print('Введите цену одного товара, коп')
    cop = int(input())
    print('Введите количество товаров, шт')
    amount = int(input())
    tot_cop = (rub * amount * 100 + cop * amount)
    print('Цена товара', rub, 'рублей', cop, 'копеек за штуку')
    print('Общая цена', (tot_cop // 100), 'рублей', (tot_cop % ((tot_cop // 100) * 100)), 'копеек')


def task_2_2():
    print('Введите произвольное предложение')
    msg = input()
    words = ''
    max_word = ''
    words_lst = []

    for i in msg:
        if i not in string.punctuation:
            words = words + i
        else:
            words = words + ' '
    words_lst = words.split()
    max_word = max(words_lst, key=len)

    print("Самое длинное слово:", max_word, ", его длина составляет", len(max_word), "символов")


def task_2_3():
    print('Введите произвольную строку')
    msg = (input().replace(' ', ''))
    result = ''
    for i in msg:
        if i not in result:
            result = result + i

    print('Результат:', result)


def task_2_4():
    print('Введите произвольную строку')
    msg = input()
    eng_lower = 0
    eng_upper = 0

    for i in msg:
        if i in string.ascii_lowercase:
            eng_lower = eng_lower + 1
        elif i in string.ascii_uppercase:
            eng_upper = eng_upper + 1
        else:
            pass

    print('Всего строчных английских букв:', eng_lower)
    print('Всего прописных английских букв:', eng_upper)


def task_2_5():
    print('Введите n-ое число Фибоначчи')
    n = int(input())
    x = 1
    y = 1
    result = 0
    i = 3

    if n < 3:
        result = 1
    else:
        while i <= n:
            result = x + y
            x = y
            y = result
            i = i + 1

    print('n-ое число Фибоначчи =', result)


def task_2_6():
    print('Введите произвольное число')
    num = int(input())
    old_num = num
    new_num = 0

    while old_num > 0:
        new_num = new_num * 10 + old_num % 10
        old_num = old_num // 10
    if num == new_num:
        print('It is polindrome')
    else:
        print('It is not polindrome')


def task_2_7():
    print('Введите первую длину одной из сторон треугольника:')
    a = float(input())
    print('Введите вторую длину одной из сторон треугольника:')
    b = float(input())
    print('Введите третью длину одной из сторон треугольника:')
    c = float(input())

    if a + b > c and a + c > b and c + b > a:
        print('Такой треугольник существует')
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Его площадь составляет:', s)
    else:
        print('Такого треугольника не существует')


def task_2_8():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    res_str = '('
    for i in range(10):
        if i <= 2 or (i > 3 and i <= 5) or i > 6:
            res_str = res_str + str(n[i])
        elif i == 3:
            res_str = res_str + ') ' + str(n[i])
        elif i == 6:
            res_str = res_str + '-' + str(n[i])
    return res_str


def task_2_9():
    s = 'The quick, brown fox jumps over the lazy dog!'
    letters = ''
    s = s.lower()

    for i in s:
        if i in string.ascii_letters:
            if i not in letters:
                letters = letters + i
            else:
                pass
        else:
            pass
    if len(letters) == 26:
        return True
    else:
        return False


def task_2_10():
    n = 3
    if n >= 0:
        if n ** 0.5 % 1 == 0:
            return True
        else:
            return False
    else:
        return False