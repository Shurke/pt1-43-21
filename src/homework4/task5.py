"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз. 
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def main():
    a = [int(i) for i in input().split()]
	for i in range(len(a)):
		s = a.count(a[i])
		if s == 1:
			print(a[i])


if __name__ == "__main__":
    main()
