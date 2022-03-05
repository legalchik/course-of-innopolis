

class Base:
	def __init__(self, name, type, health, armor):
		self.name = name
		self.type = type
		self.health = health
		self.armor = armor

	def attack(self):
		if self.health >= 0:
			if self.armor >= 0:
				self.health -= 5
				self.armor -= 20
			elif self.armor <= 0:
				self.health -= 10
		if self.health<0 or self.armor<0:
			self.health = 0
			self.armor = 0

	def info(self):
		print(f'Name: {self.name}', 
			  f'Type: {self.type}', 
			  f'Health: {self.health}', 
			  f'Armor: {self.armor}', 
			  sep='\n', end='\n\n')


class Archer(Base):
	def __init__(self, name, type='Archer', health=80, armor=100):
		super().__init__(type, name, health, armor)


class Wizard(Base):
	def __init__(self, name, type='wizard', health=50, armor=80):
		super().__init__(type, name, health, armor)

	def add_health(self):
		self.health += 5


arch = Archer(name='kaha')
wizard = Wizard(name='legal')

arch.info()
for i in range(5):
	arch.attack()
	print(arch.health, 'hp', sep='', end=' ')
print()
arch.info()

print()

wizard.info()
for i in range(5):
	wizard.attack()
	print(wizard.health, 'hp', sep='', end=' ')
print()
wizard.info()
