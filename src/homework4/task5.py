"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def main():

    lst = [1, 1, 4, 4, 12, 5, 6, 0, 6, 3]
    lst2 = []
    for element in lst:
        if element not in lst2:
            count_el = lst.count(element)
            lst2.append(element)
            if count_el == 1:
                print(element, end=' ')


if __name__ == "__main__":
    main()
