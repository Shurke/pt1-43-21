"""
Homework1
"""


import string


def task1():
    m, n, s = 5, 15, 3
    total = (m * 100 + n) * s
    return f'Общая цена {total // 100} рублей {total % 100} коп'


if __name__ == "__main__":
    print(task1())


def task2():
    sentence = 'Найти самое длинное слово'
    sentence = sentence.split()
    word, max_len = '', 0

    for i in sentence:
        value = i.strip(string.punctuation)
        if len(value) > max_len:
            max_len = len(value)
            word = value

    return f"Самое длинное слово - '{word}'"


if __name__ == "__main__":
    print(task2())


def task3():
    str_ = 'abc cde def'
    result = ''
    for i in str_.replace(' ', ''):
        if i not in result:
            result += i
    return result


if __name__ == "__main__":
    print(task3())


def task4():
    text = 'The latest news and headlines from Yahoo! News.'
    low_letter = 0
    cap_letter = 0
    for i in text:
        if i in string.ascii_uppercase:
            cap_letter += 1
        elif i in string.ascii_lowercase:
            low_letter += 1

    return f"Lowercase letter: {low_letter}\nCapitalize letter: {cap_letter}"


if __name__ == "__main__":
    print(task4())


def task5():
    num = 6
    fib = 0
    fib_next = 1
    for i in range(num - 1):
        fib, fib_next = fib_next, fib_next + fib
    return fib


if __name__ == "__main__":
    print(task5())


def task6():
    num = 123432
    num_1 = num
    num_result = 0

    while num_1 // 10:
        num_result += num_1 % 10
        num_result *= 10
        num_1 = num_1 // 10
    num_result += num_1

    return num == num_result


if __name__ == "__main__":
    print(task6())


def task7():
    a, b, c = 1, 2, 3
    if (a + b > c) and (b + c > a) and (a + c > b):
        p = (a + b + c) / 2
        return f'Area of the triangle is: {round(((p * (p - a) * (p - b) * (p - c)) ** 0.5), 2)}'
    else:
        return 'Triangle doesn\'t exist!'


if __name__ == "__main__":
    print(task7())


def task8_1():
    recipe = {'flour': 0, 'sugar': 200, 'eggs': 1}
    available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
    result = []
    try:
        for ingrid in recipe:
            result.append(available[ingrid] // recipe[ingrid])
    except ZeroDivisionError:
        result.append(0)
    return min(result)


if __name__ == "__main__":
    print(task8_1())


def task8_2():
    arr = [';D', ':-(', ':-)', ';~)']
    count = 0
    for i in arr:
        if i[0] not in ':;':
            continue
        elif i[-1] not in ')D':
            continue
        elif len(i) == 3 and i[1] not in '-~':
            continue
        else:
            count += 1
    return count


if __name__ == "__main__":
    print(task8_2())


def task8_3():
    arr = [1, 1, 1, 2, 1, 1]
    set_num = set(arr)
    num = 0
    for num in set_num:
        if arr.count(num) == 1:
            break
    return num


if __name__ == "__main__":
    print(task8_3())


def task8_4():
    n = 1234
    return bin(n).count('1')


if __name__ == "__main__":
    print(task8_4())


def task8_5():
    value = 153
    total = 0
    for i in str(value):
        total += int(i) ** len(str(value))
    return total == value


if __name__ == "__main__":
    print(task8_5())
