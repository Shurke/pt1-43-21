m = 4
n = m - 1
a = 1
l = [0, 1]
x = l[1]
for a in range(m - a):

    if a < m:
        print(l)
        x = x + l[a]
        l.append(x)
        a += 1


print(l)
print(l[n])
print(len(l))
