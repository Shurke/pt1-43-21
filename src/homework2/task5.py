# 5. Выведите n-ое число Фибоначчи, используя только временные переменные,
# циклические операторы и условные операторы.
# n - вводится
m = int(input('Enter a number: '))
n = m - 1
a = 1
fib = [0, 1]
x = fib[1]

for a in range(m - a):
    if a < m - 1:
        x = x + fib[a]
        fib.append(x)
        a += 1

print(str(m) + 'th Fibonacci number is - ' + str(fib[n]))
