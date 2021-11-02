""" Определите, является ли число палиндромом """


def main():
    num = int(input("Введите ваше число "))
    reverse_num = 0
    num1 = num
    while num1 > 0:
        reverse_num = reverse_num * 10 + num1 % 10
        num1 = num1 // 10
    if reverse_num == num:
        print("YES")
    else:
        print("NO")


main()
