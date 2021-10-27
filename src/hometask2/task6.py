# Определите, является ли число палиндромом
def main():
    n = int(input("Введите ваше число"))
    a = 0
    h = n
    while h > 0:
        a = a * 10 + h % 10
        h = h // 10
    if a == n:
        print("YES")
    else:
        print("NO")


main()
