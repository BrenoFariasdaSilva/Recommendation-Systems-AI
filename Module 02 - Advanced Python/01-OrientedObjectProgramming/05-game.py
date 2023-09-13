# Oriented Object Programming in Python.
# Inheritance is made by the use of (ClassName) after the class name.
# Polimorphism is made by the use of the same method name in different classes, which has different implementations (behaviors).

class Character:
	def __init__(self, name: str, life: int, attack: float):
		self._name: str = name
		self._life: int = life
		self._attack: float = attack

	def __str__(self):
		return f"The Character Name is: {self._name}"
	
	def __repr__(self):
		return f"Character(Name: {self._name})"
	
	def __eq__(self, other):
		return f"Character(Name: {self._name})" == f"Character(Name: {other._name})"
	
	def walk(self):
		print(f"{self._name} is walking.")

	def attack(self):
		print(f"{self._name} is attacking.")

class Warrior(Character):
	def __init__(self, name: str, life: int, attack: float, strength: float):
		self.__strength: float = strength
		# super().__init__(name, life, attack)
		Character.__init__(self, name, life, attack)

	def __str__(self):
		return f"The Warrior Name is: {self._name}"

	def __repr__(self):
		return f"Warrior(Name: {self._name}, Sword: {self.__sword})"

	def __eq__(self, other):
		return f"Warrior(Name: {self._name})" == f"Warrior(Name: {other._name})"
	
	def sword_attack(self):
		print(f"{self._name} is attacking with a sword.")

	def attack(self): # Polimorfism of Character.attack() -  Override the attack method, as they have the same name, but different implementations.
		self.sword_attack()

class Magician(Character):
	def __init__(self, name: str, life: int, attack: float, magic_power: float):
		self.__magic_power: float = magic_power
		# super().__init__(name, life, attack)
		Character.__init__(self, name, life, attack)

	def __str__(self):
		return f"The Magician Name is: {self._name}"

	def __repr__(self):
		return f"Magician(Name: {self._name}, Magic Power: {self.__magic_power})"

	def __eq__(self, other):
		return f"Magician(Name: {self._name})" == f"Magician(Name: {other._name})"

	def spell(self):
		print(f"{self._name} is casting a spell.")

	def attack(self): # Polimorfism of Character.attack() -  Override the attack method, as they have the same name, but different implementations.
		return self.spell()

def main():
	warrior = Warrior("Breno Farias", 100, 10, 50)
	print(warrior)
	warrior.walk()
	warrior.attack()
	print(f"")

	magician = Magician("Manoel Campos", 100, 10, 50)
	print(magician)
	magician.walk()
	magician.attack()
	print(f"")

	print(f"{warrior} == {magician}: {warrior == magician}")

if __name__ == "__main__":
	main()