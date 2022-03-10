import functools


def dec_func(foo):
	@functools.wraps(foo)
	def wrapper(s):
		return foo(s)
	return wrapper

@dec_func
def foo(s):
	"""Функция возвращает результат сложения a и b"""
	return s


print(foo('Реализовать простую функцию с print()'))
print(foo.__name__)
print(foo.__doc__)