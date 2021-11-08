"""
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
"""


# O(N^3)
string = input('Enter text: ')
string = string.lower()
words = string.split()

for num, word in enumerate(words):
    for char in word:
        if not char.isalpha():
            word = word.replace(char, "")
            words[num] = word

set_of_words = set([word for word in words if word])
print(f'The text contains {len(set_of_words)} different words')
