import random, os, time, pyfiglet
from progress.bar import IncrementalBar


def clear_cmd():
	try:
		os.system('cls')
	except:
		os.system('clear')


#  Start the game
print(pyfiglet.figlet_format("TAG GAME"))
print('''Добро пожаловать в игру пятнашки
Правила: соберите все костяшки в порядке возрастания
Нажмите Enter для начала игры...''', end='')
input()

loading = [10, 33, 66, 88, 99]

bar = IncrementalBar('Загрузка: ', max=len(loading))
for el in loading:
    bar.next()
    time.sleep(random.uniform(0, 0.3))
bar.finish()


#  Creating area
number_list = [i for i in range(1, 16)]
number_list.append(' ')

result_list = list(zip(*[iter(number_list)] * 4))

for i in range(len(result_list)):
    result_list[i] = list(result_list[i])

random.shuffle(number_list)

area = list(zip(*[iter(number_list)] * 4))
for i in range(len(area)):
    area[i] = list(area[i])

col_width = max(len(str(num)) for row in area for num in row) + 2


# logic of the game
while True:
	if result_list == area:
		input('Поздравляю! Вы победили')
		break

	clear_cmd()

	for row in area:
		print(''.join(str(num).ljust(col_width) for num in row))

	row1 = int(input('\nВведите строку, откуда вы хотите переместить элемент: ')) - 1
	column1 = int(input('Введите столбец, откуда вы хотите переместить элемент: ')) - 1
	row2 = int(input('\nВведите строку, куда вы хотите переместить элемент: ')) - 1
	column2 = int(input('Введите столбец, куда вы хотите переместить элемент: ')) - 1
	
# changes:
	try:
		if area[row2][column2] == ' ':
			if row1 == row2 and column1-1 <= column2 <= column1+1 or column1 == column2 and row1-1 <= row2 <= row1+1:
				area[row1][column1], area[row2][column2] = area[row2][column2], area[row1][column1]
				print('\nХод выполнен')
			else:
				print('\nСлишком далеко')
		else:
			print('\nЯчейка занята')

	except IndexError:
		print('\nТакого элемента нет')

	finally:
		time.sleep(1)
		continue
