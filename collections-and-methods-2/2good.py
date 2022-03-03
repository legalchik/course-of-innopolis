import os, sys, time
from prettytable import PrettyTable
from prettytable import ALL as ALL


try:
	os.system("title Accounting for ratings")
except:
	sys.stdout.write("\x1b]2;Accounting for ratings\x07")



def read():
	with open("db.txt", 'r') as file:
		data = file.read()
	return [el.split() for el in data.split('\n')]

def save(data):
	with open("db.txt", 'w') as file:
		file.write('\n'.join([' '.join(el1) for el1 in data]))


def lesson_add(name):
	data = read()
	if name in data[0]:
		return
	data[0].append(name)
	for i in range(1, len(data)):
		data[i].append('None')
	save(data)
	return True

def lesson_del(name):
	data = read()
	for i, el in enumerate(data[0]):
		if name == el:
			data[0].pop(i)
			for j in range(1, len(data)):
				data[j].pop(i+1)
			save(data)
			return True


def student_add(name):
	data = read()
	for el in data[1::]:
		if name == el[0]:
			return
	n = len(data[0])
	data.append([name]+n*['None'])
	save(data)
	return True

def student_del(name):
	data = read()
	for i, el in enumerate(data[1::]):
		if el[0] == name:
			data.pop(i+1)
			save(data)
			return True


def score_add(name, lesson, v):
	data = read()
	for i1, el1 in enumerate(data[0]):
		if lesson == el1:
			for i2, el2 in enumerate(data[1::]):
				if el2[0] == name:
					if data[i2+1][i1+1] == 'None':
						data[i2+1][i1+1] = v
					else:
						data[i2+1][i1+1] += v
					save(data)
					return True

def score_del_1(name, lesson):
	data = read()
	for i1, el1 in enumerate(data[0]):
		if lesson == el1:
			for i2, el2 in enumerate(data[1::]):
				if el2[0] == name:
					if data[i2+1][i1+1] != 'None':
						data[i2+1][i1+1] = data[i2+1][i1+1][:-1:]
						if data[i2+1][i1+1] == '':
							data[i2+1][i1+1] = 'None'
					save(data)
					return True


def table():
	data = read()

	for y, el1 in enumerate(data[1::]):
		for x, el2 in enumerate(el1[1::]):
			if el2 == 'None':
				data[y+1][x+1] = '-'

	table = PrettyTable()
	table.field_names = ["Уч/оц"]+data[0]
	table.add_rows(data[1::])
	print(table)


def menu():
	menu = PrettyTable(hrules=1)
	menu.field_names = ['Действия']
	menu.add_rows([['1. Показать общий табель.'],
	['2. Добавить ученика.  3. Удалить ученика.'],
	['4. Добавить предмет.  5. Удалить предмет.'],
	['6. Поставить оценку.  7. Удалить оценку  '],
	['0. Выйти.']])
	print(menu)

def menu2():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Добавление ученика']
	menu.add_rows([['Введите имя ученика'], ['0. Выйти.']])
	print(menu)

def menu3():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Удаление ученика']
	menu.add_rows([['Введите имя ученика'], ['0. Выйти.']])
	print(menu)

def menu4():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Добавление предмета']
	menu.add_rows([['Введите название предмета'], ['0. Выйти.']])
	print(menu)

def menu5():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Удаление предмета']
	menu.add_rows([['Введите название предмета'], ['0. Выйти.']])
	print(menu)

def menu6():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Поставить оценку']
	menu.add_rows([['Введите название предмета'], ['Введите имя ученика'], ['Введите оценку'], ['0. Выйти.']])
	print(menu)

def menu7():
	menu = PrettyTable(hrules=3)
	menu.field_names = ['Поставить оценку']
	menu.add_rows([['Введите название предмета'], ['Введите имя ученика'], ['0. Выйти.']])
	print(menu)


def main():
	global m 
	m = 0

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		
		if m == 0:
			menu()
			m = int(input('>>'))
			if m == 0:
				exit()
				os.system('cls' if os.name == 'nt' else 'clear')

		elif m == 1:
			table()
			m = 0
			input()

		elif m == 2:
			menu2()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if student_add(name=q) == True:
					print('Успешно')
				else:
					print('Error')


		elif m == 3:
			menu3()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if student_del(name=q) == True:
					print('Успешно')
				else:
					print('Error')
				

		elif m == 4:
			menu4()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if lesson_add(name=q) == True:
					print('Успешно')
				else:
					print('Error')
				

		elif m == 5:
			menu5()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if lesson_del(name=q) == True:
					print('Успешно')
				else:
					print('Error')
				

		elif m == 6:
			menu6()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if score_add(lesson = q, name = input('>>'), v = input('>>')) == True:
					print('Успешно')
				else:
					print('Error')
				
		elif m == 7:
			menu7()
			q = input('>>')
			if q == '0':
				m = 0
			else:
				if score_del_1(lesson = q, name = input('>>')) == True:
					print('Успешно')
				else:
					print('Error')
		
		time.sleep(0.3)


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()
		