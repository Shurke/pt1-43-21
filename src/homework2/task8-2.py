# Попробуйте выяснить какое количество нулей содержит данное число в конце.

# Входные данные: Положительное целое число (int).
# abc
# Выходные данные: Целое число (int).

a = int(input('a = '))
i = 0
while a > 0 and a % 10 == 0:
    i = i + 1
    a = a // 10
print('кол-во 0 в конце:', i)
