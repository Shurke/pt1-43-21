# You are given a string. Split the string on a " "
# delimiter and join using a - hyphen.
print("Введите строку состоящую из нескольких слов через пробел")
string = input("Строка: ")
new_string = ""
for i in string.split():
    new_string = new_string + '-' + i
new_string = new_string.strip("-")
print(new_string)