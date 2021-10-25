num_3 = num_2 = num_1 = int(input("Enter the number: "))


num_res = 0
count = 0

while num_1//10:
    num_1 //= 10
    count += 1

for i in range(count + 1):
    num_res += (num_2 % 10) * 10 ** ((count) - i)
    num_2 //= 10
print(num_res == num_3)
