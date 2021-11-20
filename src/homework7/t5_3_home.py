"""
3.	Даны два списка чисел. Посчитайте, сколько различных чисел содержится одновременно как
в первом списке, так и во втором.
"""


def func():
    list1 = [1, 1, 5]
    list2 = [7, 5, 1]
    s1 = len(set(list1)) + len(set(list2))
    print(s1)
    s2 = len(set(list1 + list2))
    print(s2)
    s1 = set(list1) - set(list2)
    print(len(s1))


if __name__ == "__main__":
    func()
