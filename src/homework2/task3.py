st1 = input('Enter "abrakadabra"')
st = st1.replace(' ', '')

a = st[0]
for i in st:
    if i not in a:
        a = a + i

print(a)
