'''
6. Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
'''


def main():

    print('Введите произвольное число')
    num = int(input())
    old_num = num
    new_num = 0

    while old_num > 0:
        new_num = new_num * 10 + old_num % 10
        old_num = old_num // 10
    if num == new_num:
        print('It is polindrome')
    else:
        print('It is not polindrome')


main()
