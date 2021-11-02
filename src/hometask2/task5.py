""" Выведите n-ое число Фибоначчи """


def main():
    num = int(input("Введите n-ое число Фибоначчи "))
    if num == 0:
        print('0')
        exit()
    prev1 = 0
    prev2 = 1
    ans = 1
    num -= 2
    while num:
        num -= 1
        ans = prev1 + prev2
        prev1 = prev2
        prev2 = ans
    print(ans)


main()
