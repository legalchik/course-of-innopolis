from time import sleep

def bye(foo):
	foo()

	def wrapper():
		sleep(3)
		print('bye')
	return wrapper

@bye
def hello():
	print('hello')


hello()