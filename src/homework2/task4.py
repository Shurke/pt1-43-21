# Посчитать количество строчных (маленьких) и прописных (больших) букв в
# введенной строке. Учитывать только английские буквы.

import string

my_string = input()
uppercase = 0
lowercase = 0
for i in my_string:
    if i in string.ascii_uppercase:
        uppercase = uppercase + 1
    elif i in string.ascii_lowercase:
        lowercase = lowercase + 1

print(f"Больших букв: {uppercase}")
print(f"Маленьких букв: {lowercase}")
