"""6. Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково). Число положительное целое, произвольной длины. Задача
требует работать только с числами (без конвертации числа в строку или что-нибудь
еще)
Задачу поместите в файл task6.py в папке src/homework2."""

num = num_1 = int(input("Enter the number: "))
num_result = 0

while num_1 // 10:
    num_result += num_1 % 10
    num_result *= 10
    num_1 = num_1 // 10
num_result += num_1

print(num == num_result)
