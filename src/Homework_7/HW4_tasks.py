"""
Homework4
"""


from copy import copy


def hw4_task1():
    """
    Func task1 from HW1
    """
    result = ''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result += 'FizzBuzz '
        elif i % 3 == 0:
            result += 'Fizz '
        elif i % 5 == 0:
            result += 'Buzz '
        else:
            result += str(i) + ' '
    return result


def hw4_task2():
    """
    Func task2 from HW1
    """
    lst = [i + j for i in 'ab' for j in 'bcd']
    lst_slice = lst[::2]
    lst_num = [str(i) + 'a' for i in range(1, 5)]
    lst_copy = (copy(lst_num))
    lst_copy.append('2a')
    return lst_slice, lst_num.pop(1)


def hw4_task3(lst=None):
    """
    Func task3 from HW1
    """
    if lst is None:
        lst = [1, 2, 3]
    tup = (lst,)
    result = []
    for elem in tup:
        for char in elem:
            result.append(char)
    return *result, f"len(tup) = {len(tup)}"


def hw4_task4(list_of_num=None):
    """
    Func task4 from HW1
    """
    if list_of_num is None:
        list_of_num = '1 1 1 1'
    list_of_num = list_of_num.split()
    counter = 0
    for enum, num in enumerate(list_of_num):
        for num_next in list_of_num[:enum]:
            if num == num_next:
                counter += 1
    return f'Количесвто пар: {counter}'


def hw4_task5():
    """
    Func task5 from HW1
    """
    list_of_elements = [1, 8, 2, 3, 1, 1, 2, 2, 3, 4, 5, 15]
    result = []
    for elem in list_of_elements:
        if list_of_elements.count(elem) == 1:
            result.append(elem)
    return result


def hw4_task6():
    """
    Func task6 from HW1
    """
    list_of_num = [1, 0, 0, 4, 0, 4, 0, 6]
    for num in list_of_num:
        if num == 0:
            list_of_num.remove(num)
            list_of_num.append(num)
    return list_of_num
