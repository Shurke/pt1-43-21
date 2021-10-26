import string

str = input('Enter string: ')
low = 0
cap = 0

for i in str:
    if i.lower() in string.ascii_lowercase:
        low += i.islower()
        cap += i.isupper()
print("Lowercase - ", low, "\n", "Capitalize - ", cap, sep='')
