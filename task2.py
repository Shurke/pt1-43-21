a = str(input(' введите предложение'))
a1 = a

for i in '!"#$%&*+,.:;?':
    a1 = a1.replace(i, ' ')
	
b = a1.split(' ')
c = 0
res = 0

for i in b:
    if len(i) > c:
        c = len(i)
        res = i

print(res)
