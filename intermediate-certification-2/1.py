# не абсурд
from module1 import calc_all

#s = input()
s = '132123+213321'
print(calc_all(s))


# абсурд
from module1 import sum, div, mult, sub

#s = input()
s = '132123+213321'

if s.find('+') != -1:
	print(sum(s.split('+')))

elif s.find('*') != -1:
	print(mult(s.split('*')))

elif s.find('/') != -1:
	print(div(s.split('/')))

elif s.find('-') != -1:
	print(sub(s.split('-')))