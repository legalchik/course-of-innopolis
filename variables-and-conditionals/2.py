
n = int(input('количество городов: '))

cities = []
for i in range(n):
	city = input('Название города: ')
	if city not in cities:
		cities.append(city)
	else:
		print('No')
