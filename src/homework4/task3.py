"""
Создайте кортеж из одного элемента,
чтобы при итерировании по этому элементу последовательно выводились значения 1, 2, 3.
Убедитесь что len() исходного кортежа возвращает 1.
"""


def main():
    tuple1 = ([1, 2, 3], )
    for i in tuple1:
        for q in i:
            print(q)
    print('Результат:', len(tuple1))


if __name__ == "__main__":
    main()
