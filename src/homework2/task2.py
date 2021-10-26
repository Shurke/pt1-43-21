# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении есть знаки препинания.
import string
# Улучшенное решение
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
for i_ in d:
    if len(i_) > f:
        f = len(i_)
for i__ in d:
    if len(i__) == f:
        print(i__)
