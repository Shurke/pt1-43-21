"""Homework 5, Task6:
Во входной строке записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""


def word_count(search_string: str) -> int:
    total_words = []
    strings = search_string.splitlines()
    for string_ in strings:
        string_words = string_.split()
        for word in string_words:
            total_words.append(word)
    total_words = set(total_words)
    count_total_words = len(total_words)
    print("Количество различных слов в тексте: ", count_total_words)
    return count_total_words


word_count("Это тестовая строка для подсчета \n в ней количества слов.")
