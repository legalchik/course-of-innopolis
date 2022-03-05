

class Tank:
	def __init__(
		self,
		name: str,
		color: str,
		strength: int = 100,
		power: int = None,
		speed: int = None,
		damage: int = None,
	):
		self.name = name
		self.color = color
		self.damage = damage
		self.speed = speed
		self.power = power
		self.strength = strength

	def beep(self):
		print(f"Tank {self.name}: B{10*10*'e'}p!!!")

	def feature(self):
		feature = {
			"Tank": self.name, 
			"color": self.color, 
			"damage": self.damage, 
			"speed": self.speed, 
			"power": self.power, 
			"strength": self.strength
		}
		for el in feature:
			if feature[el] != None:
				print(f"{el}: {feature[el]}")
		print()



tank1 = Tank("SUPRA", 'rainbow')
tank1.damage = 10
tank1.power = 100

tank2 = Tank("PORSHE", 'pink')
tank2.strength = 120

tank3 = Tank(name="ZHIGULE", color='matte-black', damage=10**10, power=100)
tank1.speed = 34

tank1.feature()
tank2.feature()
tank3.feature()

tank2.beep()
