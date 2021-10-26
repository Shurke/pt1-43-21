#You are going to be given a word. Your job is to return the middle
# character of the word. If the word's length is odd, return the middle character.
# If the word's length is even, return the middle 2 characters.

def get_middle(s):
    s_len = len(s)
    number = s_len // 2
    if s_len % 2 == 0:
        number = number - 1
    return s[number:(s_len - number)]


print(get_middle(input("Введите строку: ")))
