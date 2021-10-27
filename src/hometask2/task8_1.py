# acmp.ru problem № 43
# Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.
def main():
    s = input("Введите строку из 0 и 1")
    max_null = 0
    current_null = 0
    for i in s:
        if i == '0':
            current_null += 1
        else:
            max_null = max(max_null, current_null)
            current_null = 0
    max_null = max(max_null, current_null)
    print(max_null)


main()
