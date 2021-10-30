"""
Выведите n-ое число Фибоначчи, используя только временные переменные,
циклические операторы и условные операторы. n - вводится
"""
def main():
    n = int(input("Введите N: "))
    if n == 0:
        print('0')
    elif n == 1:
        print('1')
    else:
        prev1 = 0
        prev2 = 1
        index = 3
        while index <= n:
            cur = prev1 + prev2
            index = index + 1
            prev1 = prev2
            prev2 = cur
    print(cur)
    
    if __name__ == "__main__":
    main()
