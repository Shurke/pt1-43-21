# Выведите n-ое число Фибоначчи
def main():
    n = int(input("Введите n-ое число Фибоначчи "))
    if n == 0:
        print('0')
        exit()
    x = 0
    y = 1
    ans = 1
    n -= 1
    while n:
        n -= 1
        ans = x + y
        x = y
        y = ans
    print(ans)


main()
