"""Создайте декоратор,
который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа TooManyErrors
"""

from bs4 import BeautifulSoup
import requests
import time


class TooManyErrors(Exception):
    def __init__(self, message):
        self.txt = message


def functional_expander(n):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            result = ""
            total = 0
            i = 1
            try:
                while i <= n:
                    start = time.time()
                    result += func(*args, **kwargs)
                    end = time.time()
                    total += end - start
                    print("Фрагмент текста сайта получен", i, "раз(а), в среднем за",
                          total / i, "секунд.")
                    i += 1
                else:
                    raise TooManyErrors("Превышено количество попыток вызова функции.")
            except TooManyErrors:
                print("Превышено количество попыток вызова функции.")
            finally:
                return result
        return wrapper
    return real_decorator


@functional_expander(n=10)
def get_text(url):
    rs = requests.get(url)
    root = BeautifulSoup(rs.content, 'html.parser')
    article = root.select_one('.main-section-top__txt p')
    return article.text


text = get_text("https://www.it-academy.by/course/python-developer/")
print(text[:100])
