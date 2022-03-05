

class Class(list):
	def append(self):
		return self.pop()

a = Class([1,2,3])
a.append()

print(a)
