# Найти самое длинное слово в введенном предложении. Учтите что в предложении
# есть знаки препинания.
import string
my_string = input()
for x in my_string:
    if x in string.punctuation:
        my_string = my_string.replace(x, "")
result = ""
new_string = my_string.split()
for i in new_string:
    if len(i) > len(result):
        result = i
print(f"Самое длинное слово в предложении: {result}")
