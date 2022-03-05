num = input('номер месяца: ')
#num = '13'

if num in [str(n) for n in range(1, 13)]:   # проверка что это число 1-12

	num = int(num)

	if num in [12, 1, 2]:
		print('зима')

	elif num in [3, 4, 5]:
		print('весна')

	elif num in [6, 7, 8]:
		print('лето')

	elif num in [9, 10, 11]:
		print('осень')
		