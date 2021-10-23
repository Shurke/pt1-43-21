#65 - 90 - BIG
#97 - 122 - small

st = input('Enter some text: ')

a = 0
b = 0

for i in st:
    if (65 <= ord(i) <= 90):
        a += 1
    elif (97 <= ord(i) <= 122):
        b += 1

print('Quantity of lowercase English letters is ' + str(b))
print('Quantity of uppercase English letters is ' + str(a))
