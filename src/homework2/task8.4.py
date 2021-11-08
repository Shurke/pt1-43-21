# You are given a string. Split the string on a " "
# delimiter and join using a - hyphen.
print("Введите строку состоящую из нескольких слов через пробел")
string = input("Строка: ")
new_string = string.replace(' ', '-')
print(new_string)
