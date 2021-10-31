''' 4. Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

Учитывать только английские буквы.
'''

entered_symbols = input('Enter some text: ')

lowercased_words = 0
uppercase_words = 0

for symbol in entered_symbols:
    if symbol.isupper():
        uppercase_words += 1
    elif symbol.islower():
        lowercased_words += 1

print('Quantity of lowercase English letters is ' + str(lowercased_words))
print('Quantity of uppercase English letters is ' + str(uppercase_words))
