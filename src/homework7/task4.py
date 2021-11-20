"""
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
- Перевести числа от m до n (включительно) в двоичные числа.
- Сложить полученные двоичные числа по основанию 10.
- Перевести результат сложения в двоичную число.
- Вернуть строку с результатом.
Пример:
func(1, 4)   -->  1111010
1  // 1 в двоичном виде 1
10  // 2 в двоичном виде 10
11  // 3 в двоичном виде 11
100  // 4 в двоичном виде 100
-----
122  // 122 в двоичном виде 1111010
"""


def func(first_num, second_num):
    print("Формат:\nЧисло - Число в двоичной си-ме")
    work_num = first_num
    bin_sum = 0
    while work_num <= second_num:
        num = work_num
        print(f"{num} - ", end="")
        bin_num = ""
        while num >= 1:
            bin_num = f"{num % 2}{bin_num}"
            num = num // 2
        print(bin_num)
        bin_sum += int(bin_num)
        work_num += 1
    print("-----")
    num = bin_sum
    bin_num = ""
    while num >= 1:
        bin_num = f"{num % 2}{bin_num}"
        num = num // 2
    print(f"{bin_sum} - {bin_num}")


num1 = int(input("Первое чило: "))
num2 = int(input("Второе чило: "))
func(num1, num2)
