"""
Homework4
"""


from copy import copy


def task1():
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


if __name__ == "__main__":
    print(task1())


def task2():
    lst = [i + j for i in 'ab' for j in 'bcd']
    lst_slice = lst[::2]
    lst_num = [str(i) + 'a' for i in range(1, 5)]
    lst_copy = (copy(lst_num))
    lst_copy.append('2a')
    return lst_slice, lst_num.pop(1)


if __name__ == "__main__":
    print(*task2(), sep='\n')


def task3():
    lst = [1, 2, 3]
    tup = (lst,)
    result = []
    for elem in tup:
        for char in elem:
            result.append(char)
    return *result, f"len(tup) = {len(tup)}"


if __name__ == "__main__":
    print(*task3())


def task4():
    list_of_num = '1 1 1 1'
    list_of_num = list_of_num.split()
    counter = 0

    for enum, num in enumerate(list_of_num):
        for num_next in list_of_num[:enum]:
            if num == num_next:
                counter += 1
    return f'Количесвто пар: {counter}'


if __name__ == "__main__":
    print(task4())


def task5():
    list_of_elements = [1, 8, 2, 3, 1, 1, 2, 2, 3, 4, 5, 15]
    result = []
    for elem in list_of_elements:
        if list_of_elements.count(elem) == 1:
            result.append(elem)
    return result


if __name__ == "__main__":
    print(*task5(), sep=',')


def task6():
    list_of_num = [1, 0, 0, 4, 0, 4, 0, 6]
    for num in list_of_num:
        if num == 0:
            list_of_num.remove(num)
            list_of_num.append(num)
    return list_of_num


if __name__ == "__main__":
    print(task6())
