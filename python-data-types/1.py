
l = int(input('Длина списка: '))

Sum = 0
pro = 1
for i in range(l):
	In = int(input(f'{i+1}: '))
	Sum += In
	pro *= In

print(f'\nСумма: {Sum}\nПроизведение: {pro}')
