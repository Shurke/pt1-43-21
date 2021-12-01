def task1_2():
    m = int(input('цена рублей'))
    n = int(input('коппеек'))
    s = int(input('колл. товара'))

    print('Общая цена', (m * s + n * s // 100), 'рублей', (n * s % 100), 'копеек')


def task2_2():
    import string

    a = str(input(' введите предложение'))
    a1 = a

    for i in string.punctuation:
        a1 = a1.replace(i, " ")

    b = a1.split(' ')
    c = 0
    res = 0

    for i in b:
        if len(i) > c:
            c = len(i)
            res = i

    print(res)


def task3_2():
    a = input('введите предложение')
    b = a.replace(' ', '')
    n = ''

    for i in b:
        if i not in n:
            n = n + i

    print(n)


def task4_2():
    import string

    a = str(input('Введите предложение', ))
    am = 0
    ab = 0

    for i in a:
        if i in string.ascii_lowercase:
            am = am + 1
        elif i in string.ascii_uppercase:
            ab = ab + 1

    print('больших', ab)
    print('маленьких', am)


def task5_2():
    a = 1
    b = 1
    n = input("Номер элемента ряда Фибоначчи: ")
    n = int(n)
    i = 0

    while i < n - 2:
        c = a + b
        a = b
        b = c
        i = i + 1

    print("Значение этого элемента:", b)


def task6_2():
    a = int(input('введите число: '))
    a1 = a
    pol = 0

    while a1 > 0:
        b = a1 % 10
        a1 = a1 // 10
        pol = pol * 10
        pol = pol + b

    if a == pol:
        print('полиндром')
    else:
        print('не полиндром')


def task7_2():
    a = int(input())
    b = int(input())
    c = int(input())

    if a + b > c and b + c > a and a + c > b:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b)) * (p - c)
        s1 = s ** 0.5
        print('это треугольник площадь которого', s1)
    else:
        print('это не треугольник')


def task1_4():
    for int_elem in range(1, 101):
        if int_elem % 3 == 0 and int_elem % 5 == 0:
            print("FizzBuzz")
        elif int_elem % 3 == 0:
            print("Fizz")
        elif int_elem % 5 == 0:
            print("Buzz")
        else:
            print(int_elem)


def task2_4():
    import copy

    lst1 = [a + b for a in 'ab' for b in 'bcd']

    print(lst1)
    lst2 = lst1[::2]

    print(lst2)
    lst3 = [str(i) + 'a' for i in range(1, 5)]

    print(lst3)
    print(lst3.pop(1))

    lst4 = copy.deepcopy(lst3)
    lst5 = ['2a']

    print(lst4 + lst5)


def task3_4():
    tuple1 = ([1, 2, 3],)

    print(tuple1[0], len(tuple1))


def task4_4():
    list_int = input('Введите числа через пробел').split()
    all_repeat = 0

    for n in list_int:
        all_repeat = all_repeat + list_int.count(n) - 1

    couples_elem = all_repeat / 2

    print('Колл.пар элементов равных друг другу', int(couples_elem))


def task5_4():
    list1 = ['a', 'b', 'b', 'c', 'd', 'e', 'a']

    for elem_list1 in list1:
        if list1.count(elem_list1) == 1:
            print(elem_list1)


def task6_4():
    list_int = [1, 2, 0, 3, 0, 4, 6]

    for elem_list in range(len(list_int)):
        if list_int[elem_list] == 0:
            list_int.append(list_int.pop(elem_list))

    print(list_int)


def task1_5():
    dict1 = {i: i ** 3 for i in range(1, 21)}

    print(dict1)


def task2_5():
    states = {}

    for _ in range(int(input('введите колличество стран', ))):
        state, *cities = input('вветите название страны затем названия городов', ).split()
        for city in cities:
            states[city] = state

    print(*(states[input()] for _ in range(int(input("колл. стран и их название", )))), sep="\n")


def task3_5():
    lst1 = [1, 2, 3, 4]
    lst2 = [2, 3, 4, 5]

    print('колличество разных чисел списков: ', len(set(lst1) | set(lst2)))


def task4_5():
    lst1 = [2, 2, 3, 2]
    lst2 = [2, 3, 4, 5]
    lst3 = set(lst1) & set(lst2)
    lst4 = set(lst1) ^ set(lst1)

    print('колличество различных чисел одного списка:', len(set(lst3) | set(lst4)))


def task5_5():
    union = set()
    all = set()

    for i in range(int(input('введите колличество школьников:', ))):
        m = int(input('введите колличество языков школьников:', ))
        a = {input('введите название языков школьника:', ) for j in range(m)}
        all.update(a)
        if i != 1:
            union.update(a)
        else:
            union &= a

    print('колличество языков которые знают все школьники:', len(union))
    print('\n'.join(sorted(union)))
    print('колличество языков которое знает хотя бы один школьник:', len(all))
    print('\n'.join(sorted(all)))


def task6_5():
    str1 = str(input('введите текст'))
    str2 = str1.replace('\n', ' ').split(' ')
    str3 = ()

    print('колличество различных слов:', len(set(str2) | set(str3)))


def task7_5():
    int1 = 15
    int2 = 45

    while int1 != 0 and int2 != 0:
        if int1 > int2:
            int1 = int1 % int2
        else:
            int2 = int2 % int1

    print('наибольший общий делитель:', (int1 + int2))
