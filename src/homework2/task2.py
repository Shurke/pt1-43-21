# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
# Улучшенный вариант

import string

a = 'somed task,sdsdss klon! kul'
b = ""
for i in a:
    if i not in string.punctuation:
        b = b + i
    else:
        b = b + " "
c = b.replace("  ", " ")
d = c.split(" ")
f = 0
for i__ in d:
    if len(i__) == max(len(d)):
        print(i__)
