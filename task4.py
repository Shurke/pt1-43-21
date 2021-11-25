"""    4. Двоичная пирамида.
На вход функции передаются два целых числа m и n, такие что 0 ≤ m ≤ n.
Функция выполняет следующие действия:
        a. Перевести числа от m до n (включительно) в двоичные числа.
        b. Сложить полученные двоичные числа по основанию 10.
        c. Перевести результат сложения в двоичную число.
        d. Вернуть строку с результатом."""


def func(int1):
    int2 = ''
    while int1 >= 1:
        int2 = int2 + (str(int1 % 2))
        int1 = int1 // 2
    return int2[::-1]


m = int(input('введите число m:', ))
n = int(input('введите число n больше чтсла m:', ))
m1 = m
n1 = n
while m <= n:
    print(m, 'в двоичном виде: ', func(m))
    m += 1
sum1 = 0
while m1 <= n1:
    sum1 = sum1 + m1
    m1 += 1
print('сумма чисел от m до n =', sum1, 'в двоичном виде: ', func(sum1))
