import string

st1 = input('Enter text, please - ')
st = st1.replace('9', ' ')
stripped = st.translate(str.maketrans('', '', string.punctuation))
st1 = stripped.split(' ')

print(st1)

b = 0
result = 0
for i in st1:
    if len(i) > b:
        b = len(i)
        result = i

print(result)
