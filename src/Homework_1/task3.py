str = input('Enter string: ')
result = ''
for i in str.replace(' ', ''):
    if i not in result:
        result += i
print(result)
