try:
	u = input('Пользователь ввел число ')   # там так и было сказано...))

	u = int(u)

	if u < 2:
		print(f'{u} компьютер')

	elif u < 5:
		print(f'{u} компьютера')

	else:
		print(f'{u} компьютеров')

except:...