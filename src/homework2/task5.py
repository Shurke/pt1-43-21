def main():
    n = input("Введите номер числа Фибоначчи: ")
    try:
        n = int(n)
    except ValueError:
        return print("Это не число!")
    if n < 0:
        return print("Число не должно быть отрицательным")
    elif n == 0:
        return print("Нумерация начнается с 1")
    elif n == 1:
        return print("0")
    elif n == 2:
        return print("1")
    else:
        i = 3
        fib = 1
        prefib = 0
        while i <= n:
            fib_old = fib
            fib = fib + prefib
            prefib = fib_old
            i = i+1
        print(fib)

main()


