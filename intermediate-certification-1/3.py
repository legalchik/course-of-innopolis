

class List(list):
	def append(self, a):
		for i in range(len(self)):
			self[i] = self[i]**a

a = List([1,2,3,4])
a.append(2)

print(a)
