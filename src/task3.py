"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами. Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.
"""


def num_of_couple(list_of_nums):
    if type(list_of_nums) is not str:
        raise TypeError("Функция приниает в качестве аргумента только строку!")
    list_of_nums = list_of_nums.split()
    list_of_nums.sort()
    item1 = 0
    counter = 0
    while item1 < len(list_of_nums):
        item2 = item1 + 1
        while item2 < len(list_of_nums):
            if list_of_nums[item1] == list_of_nums[item2]:
                counter += 1
            item2 += 1
        item1 += 1
    return counter


my_string = input("Введите список чисел через пробел для подсчета "
               "количества пар элементов, равных друг другу:\n")
print(f"Количество пар равно {num_of_couple(my_string)}")
