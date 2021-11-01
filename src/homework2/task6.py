'''
Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины. Задача требует работать только с числами
(без конвертации числа в строку или что-нибудь еще)
'''


def main():
    n = int(input("Введите число: "))
    tmp = n
    reverse_num = 0
    while(n > 0):
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n //= 10
    if (tmp == reverse_num):
        print("Полиндром")
    else:
        print("Не полиндром")


if __name__ == "__main__":
    main()
