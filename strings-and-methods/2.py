

def foo(s):
	Sum = sum(s)

	Sum2 = 0
	for el in s:
		if el%2 == 0:
			Sum2 += el

	diff = max(s) - min(s)

	return Sum, Sum2, diff


print(foo((1, 2, 3, 4, 5)))
