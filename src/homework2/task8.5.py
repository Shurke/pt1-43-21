# Read a given string, change the character at a given index and
# then print the modified string.
string = input("Введите вашу строку: ")
pos = int(input("Введите номер символа, который хотите заменить: "))
char = input(f"Введите символ, которым хотите заменить символ номер {pos}: ")
if 0 < pos <= len(string):
    string = string.replace(string[pos-1], char)
    print(string)
else:
    print("Ошибка ввода!")
