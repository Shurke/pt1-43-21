''' Задачи из Homework3, преобразованные в функции.
'''


def task1():
    for i in range(1, 101):
        if not i % 15:
            print('FizzBuzz')
        elif not i % 3:
            print('Fizz')
        elif not i % 5:
            print('Buzz')
        else:
            print(i)


def task2():
    lst = [lst1 + lst2 for lst1 in 'ab' for lst2 in 'bcd']
    print('1: ', lst)

    lst3 = slice(0, 6, 2)
    print('2: ', lst[lst3])

    lst4 = [lst5 + lst6 for lst5 in '1234' for lst6 in 'a']
    print('3: ', lst4)

    print('4: ', lst4.pop(1))

    lst4.insert(1, '2a')
    print('5: ', lst4)


def task3():
    lst1 = ['a', 'b', 'c']
    tpl1 = tuple(lst1)
    print(tpl1)

    tpl2 = ('a', 'b', 'c')
    lst2 = list(tpl2)
    print(lst2)

    lst2[0:3] = ['a', 2, 'python']
    print(lst2)

    tpl4 = ((1, 2, 3), )
    for elem in tpl4[0]:
        print(elem, end=', ')
    print('len(tpl) = ', len(tpl4))


def task4():
    lst = [1, 1, 1, 1]
    pairs = 0
    dct = {element: lst.count(element) for element in lst}
    keyslist = dct.keys()
    for i in keyslist:
        Sn = dct[i] * (dct[i] - 1) // 2
        pairs += Sn
    print('В списке:', lst, 'количество пар:', pairs)


def task5():
    lst = [1, 5, 2, 56, 3, 1, 3, 1, 7, 1]
    lst_ = [element for element in lst if lst.count(element) == 1]
    print('Элементы, встречающиеся только один раз:', lst_)


def task6():
    lst = [1, 0, 5, 2, 56, 0, 3, 1, 3, 1, 0, 7, 1]
    for element in lst:
        if element == 0:
            lst.remove(0)
            lst.append(0)
    print(lst)
