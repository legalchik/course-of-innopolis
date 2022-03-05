
a = [1, 2, 3, 4, 5, 6]

for i in reversed(range(len(a))):
	if a[i]%2 != 0:
		del a[i]
	else:
		a[i] = a[i] // 2
		
print(a)
