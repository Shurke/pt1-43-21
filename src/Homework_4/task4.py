"""
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами.
Выходные данные - количество пар.
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""


list_of_num = input('Enter numbers by  "Space" separated: ')
list_of_num = list_of_num.split()
counter = 0

for enum, num in enumerate(list_of_num):
    for num_next in list_of_num[:enum]:
        if num == num_next:
            counter += 1
print(f'Количесвто пар: {counter}')
