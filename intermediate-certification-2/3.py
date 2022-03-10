

class StrIter:
	def __init__(self, value):
		self.value = value
		self.i = 0

	def __iter__(self):
		return self
	
	def __next__(self):

		if self.i < len(self.value):
			char = self.value[self.i]
			self.i += 1
			return char
		else:
			raise StopIteration

		
a = [1, 2, 3, 4, 5, 6]
hehe = iter(StrIter(a))

for i in hehe:
	print(i)