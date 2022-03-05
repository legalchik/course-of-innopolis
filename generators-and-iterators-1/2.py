

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

		

Str = iter(StrIter(['as', 'soon', 'as']))

for i in Str:
	print(i)
