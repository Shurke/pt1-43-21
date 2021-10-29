# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Улучшенный вариант

import string

a = 'somedaa task,sdsdss klon! kul'
b = ""
for i in a:
    if i not in string.punctuation:
        b = b + i
    else:
        b = b + " "
c = b.replace("  ", " ")
d = c.split(" ")
print(max(d, key=len))
