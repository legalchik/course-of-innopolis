
l = int(input('Длина списка: '))

s = []
for i in range(l):
	s.append(int(input(f'{i+1}: ')))

print()

for el in s:
	if el == 237:
		break
	else:
		if el%2 == 0:
			print(el)
			