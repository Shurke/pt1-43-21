"""
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
"""


str = "Why do? You\ncry, Willy. Why ^$# do  you\ncry 11 $ 19 $#$%^ валера"

str = str.lower()
words = str.split()

for num, word in enumerate(words):
    for char in word:
        if not char.isalpha():
            word = word.replace(char, "")
            words[num] = word

set_of_words = set([word for word in words if word])
print(len(set_of_words))
