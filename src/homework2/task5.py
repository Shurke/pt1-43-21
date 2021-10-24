m = int(input('Enter a number: '))
n = m - 1
a = 1
l = [0, 1]
x = l[1]

for a in range(m - a):
    if a < m - 1:
        x = x + l[a]
        l.append(x)
        a += 1

print(str(m) + 'th Fibonacci number is - ' + str(l[n]))
