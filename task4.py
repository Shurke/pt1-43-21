a = str(input())
am = 0
ab = 0

for i in a:
    if 'a' <= i <= 'z':
        am += 1
    else:
        ab += 1

print('больших', ab)
print('маленьких', am)
