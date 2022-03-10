

def calc_all(data):
	data.replace("=", "")
	return data+" = "+str(eval(data))


def sum(*args):
	res = 0
	s = [int(i) for i in args[0]]

	for el in s:
		res += el
	return res

def mult(*args):
	res = 1
	s = [int(i) for i in args[0]]

	for el in s:
		res *= el
	return res

def div(*args):
	s = [int(i) for i in args[0]]
	res = s[0]

	for el in s[1:]:
		res /= el
	return res

def sub(*args):
	s = [int(i) for i in args[0]]
	res = s[0]

	for el in s[1:]:
		res -= el
	return res
