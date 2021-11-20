"""
5.	Уникальные элементы в списке
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
Задачу поместите в файл task5.py в папке src/homework3.
"""


def func():
    list1 = ['a', 'b', 2, 'c', 2, 'a', 'c']
    print(list1)
    list2 = []
    i = 0
    for item1 in list1:
        i = i + 1
        n = 0
        for item2 in list1:
            n = n + 1
            if item1 == item2 and n > i:
                list2.append(item1)
    print(list2)


if __name__ == "__main__":
    func()
