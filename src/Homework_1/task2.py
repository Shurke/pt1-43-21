import string

str = input("Введите строку: ")
word, max_len = '', 0

for i in str.split():
    if len(i.strip(string.punctuation)) > max_len:
        max_len = len(i.strip(string.punctuation))
        word = i.strip(string.punctuation)

print(f"Самое длинное слово - '{word}'")
