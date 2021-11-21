
import string as __string


def task1_2():
    """ 1. Напишите программу, которая считает общую цену.

     Вводится M рублей и N копеек цена, а также количество S товара
     Посчитайте общую цену в рублях и копейках за L товаров.
     Пример:
     Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
     Output: Общая цена 9 рублей 60 копеек

     """
    try:
        m = int(input("Введите Рубли: "))
        n = int(input("Введите копейки: "))
        k = int(input("Введите количество товара: "))
    except ValueError:
        print("Это не число!")
        return
    sum_rub = m * k + n * k // 100
    sum_k = n * k % 100
    print("стоимость товара: ", sum_rub, "р.", sum_k, "к.")


def task2_2():
    """ 2. Найти самое длинное слово в введенном предложении.

     Учтите что в предложении есть знаки препинания.
     Подсказки:
     - my_string.split([chars]) возвращает список строк.
     - len(list) - количество элементов в списке
    """
    our_string = input("Введите предложение: ")
    list_punct = __string.punctuation
    our_string_clean = ""
    for i in our_string:
        if i not in list_punct:
            our_string_clean = our_string_clean + i
    list_of_words = our_string_clean.split()
    len_of_list_of_words = len(list_of_words)
    if len_of_list_of_words == 0:
        print("В вашем предложении нет слов")
    elif len_of_list_of_words == 1:
        print(list_of_words[0])
    else:
        longest_word = ""
        len_of_longest_word = 0
        for i in list_of_words:
            if len_of_longest_word < len(i):
                len_of_longest_word = len(i)
                longest_word = i
        print(longest_word)


def task3_2():
    """3. Вводится строка. Требуется удалить из нее повторяющиеся
    символы и все пробелы. Например, если было введено
    "abc cde def", то должно быть выведено"""
    our_string = input("Введите строку: ")
    our_string = our_string.replace(" ", "")
    result_string = ""
    for i in our_string:
        if i not in result_string:
            result_string = result_string + i
    print(result_string)


def task4_2():
    """Посчитать количество строчных (маленьких) и прописных (больших) букв
    в введенной строке. Учитывать только английские буквы."""
    our_string = input("Введите строку: ")
    c_upper = 0
    c_lower = 0
    for i in our_string:
        if i.isalpha():
            if i.islower():
                c_lower = c_lower + 1
            else:
                c_upper = c_upper + 1
    print("Больших букв: ", c_upper, ", ", "Маленьких букв: ", c_lower)


def task5_2():
    """5. Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится
    n = номер числа Фибоначчи: """
    n = input("Введите номер числа Фибоначчи: ")
    try:
        n = int(n)
    except ValueError:
        return print("Это не число!")
    if n < 0:
        return print("Число не должно быть отрицательным")
    elif n == 0:
        return print("Нумерация начнается с 1")
    elif n == 1:
        return print("0")
    elif n == 2:
        return print("1")
    else:
        i = 3
        fib = 1
        prefib = 0
        while i <= n:
            fib_old = fib
            fib = fib + prefib
            prefib = fib_old
            i = i + 1
        print(fib)


def task6_2():
    """Определите, является ли число палиндромом
    (читается слева направо и справа налево одинаково).
    Число положительное целое, произвольной длины.
    Задача требует работать только с числами
    (без конвертации числа в строку или что-нибудь еще)"""

    n = input("Введите целое не отрицательное число: ")
    try:
        n = int(n)
    except ValueError:
        print("Это не число!")
        return
    m = n
    if m < 0:
        print("Это отрицательное число")
        return
    if m % 10 == 0:
        print("Не палиндром")
        return
    new_number = 0
    while m > 0:
        new_number = new_number * 10 + m % 10
        m = m // 10
    if new_number == n:
        print("Палиндром")
    else:
        print("Не палиндром")


def task7():
    """ Задача 7
    Даны: три стороны треугольника. Требуется: проверить,
    действительно ли это стороны треугольника. Если стороны
    определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.

"""
    try:
        a = float(input("введите строну a: "))
        b = float(input("введите строну b: "))
        c = float(input("введите строну c: "))
    except ValueError:
        print("Это не число!")
        return
    if a < 0 or b < 0 or c < 0:
        print("Стороны не должны быть отрицательными")
        return
    if a + b <= c or a + c <= b or c + b <= a:
        print("Это не треугольник")
    else:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
        print("площадь:", s)


def task8_1_2():
    """In this little assignment you are given a string of space
    separated numbers, and have to return the highest and lowest number.
    Example:
    high_and_low("1 2 3 4 5")  # return "5 1"
    high_and_low("1 2 -3 4 5") # return "5 -3"
    high_and_low("1 9 3 4 -5") # return "9 -5"
    Notes:
    All numbers are valid Int32, no need to validate them.
    There will always be at least one number in the input string.
    Output string must be two numbers separated by a single space, and highest number is first."""
    numbers = input("Введите строку из чисел: ")
    list_of_numbers = numbers.split()
    lowest = int(list_of_numbers[0])
    highest = int(list_of_numbers[0])
    for i in list_of_numbers:
        m = int(i)
        if m < lowest:
            lowest = m
        if m > highest:
            highest = m
    return print("" + str(highest) + " " + str(lowest))


def task8_2_2():
    """You are going to be given a word. Your job is to return the middle
    character of the word. If the word's length is odd, return the middle character.
    If the word's length is even, return the middle 2 characters."""
    s = input("Введите строку: ")
    s_len = len(s)
    number = s_len // 2
    if s_len % 2 == 0:
        number = number - 1
    return print(s[number:(s_len - number)])


def task8_3_3():
    """Given two integers a and b, which can be positive or negative,
    find the sum of all the integers between and including them and return it.
    If the two numbers are equal return a or b.
    Note: a and b are not ordered!
    Examples (a, b) --> output (explanation)
    (1, 0) --> 1 (1 + 0 = 1)
    (1, 2) --> 3 (1 + 2 = 3)
    (0, 1) --> 1 (0 + 1 = 1)
    (1, 1) --> 1 (1 since both are same)
    (-1, 0) --> -1 (-1 + 0 = -1)
    (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)"""
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    if a == b:
        return print(a)
        i = a
        s = 0
        while i <= b:
            s = s + i
            i = i + 1
        return print(s)
    else:
        i = b
        s = 0
        while i <= a:
            s = s + i
            i = i + 1
        return print(s)


def task8_4_3():
    """Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive.
    The string can contain any char.
    Examples input/output:
    XO("ooxx") => true
    XO("xooxx") => false
    XO("ooxXm") => true
    XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    XO("zzoo") => false"""
    s = input("ВВедите строку:")
    s = s.lower()
    return print(str(s.count("x") == s.count("o")))


def task8_5_5():
    """In this simple assignment you are given a number and
    have to make it negative. But maybe the number is already negative?
    Examples
    make_negative(1);  # return -1
    make_negative(-5); # return -5
    make_negative(0);  # return 0
    Notes
    The number can be negative already, in which case no change is required.
    Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense"""
    numb = int(input("Введите число: "))
    if numb <= 0:
        return print(str(numb))
    else:
        return print(str(-numb))








