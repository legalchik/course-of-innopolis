

class Child:
	def __init__(
		self, 
		name: str, 
		surname: str, 
		age: int
		):
		self.name = name
		self.surname = surname
		self.age = age

	def get_all(self):
		print(self.name, self.surname, self.age, sep='\n')


rifat = Child(name='Рифат', surname='Гилазов', age=3)

rifat.get_all()
