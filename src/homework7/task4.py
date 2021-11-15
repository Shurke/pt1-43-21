"""Задача 4. Двоичная пирамида.

На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
Перевести числа от m до n (включительно) в двоичные числа.
Сложить полученные двоичные числа по основанию 10.
Перевести результат сложения в двоичную число.
Вернуть строку с результатом.

Пример:
func(1, 4)   -->  1111010
    1  // 1 в двоичном виде 1
+  10  // 2 в двоичном виде 10
+  11  // 3 в двоичном виде 11
+ 100  // 4 в двоичном виде 100
-----
  122  // 122 в двоичном виде 1111010
Задачу поместите в файл task4.py в папке src/homework7.
"""


def decimal_to_binary(number):
<<<<<<< HEAD
    if number == 0:
        return 0
=======
>>>>>>> origin/homework7
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary


def binary_pyramid(m, n):
    sum_of_binary_numbers = 0
    for number in range(m, n + 1):
        sum_of_binary_numbers = sum_of_binary_numbers + int(decimal_to_binary(number))
    return decimal_to_binary(sum_of_binary_numbers)


try:
<<<<<<< HEAD
    m = int(input("Введите первое неотрицательное число: "))
    n = int(input("Введите второе неотрицательное число больше первого: "))
except ValueError:
    exit("Это не чило.")
if 0 <= m <= n:
    result = binary_pyramid(m, n)
    print("Итого: ", result)
else:
    print("Введенные числа не соответствуют условиям задачи.")
=======
    m = int(input("Введите первое число: "))
    n = int(input("Введите второе число: "))
except ValueError:
    exit("Это не чило.")
result = binary_pyramid(m, n)
print("Итого: ", result)
>>>>>>> origin/homework7
