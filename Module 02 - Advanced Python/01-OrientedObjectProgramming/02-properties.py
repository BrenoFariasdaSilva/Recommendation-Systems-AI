# Oriented Object Programming in Python.
# Encapsulation is more simple in Python, just use the @property decorator.

class Person:
	def __init__(self, name): # Constructor -> __init__
		self._name = name # Private Attribute

	def __repr__(self):
		return f"Person(Name: {self._name})"
	
	def __eq__(self, other):
		return self._name == other._name

	def say_hi(self): # Method
		print(f"Hello, my name is {self._name}.")

	@property
	def name(self): # Getter
		return self._name

def main():
	me = Person("Breno") # Constructor -> __init__
	me.say_hi() # Hello, my name is Breno
	me._name = "Breno Farias" # Setter -> __name = "Breno Farias"
	me.say_hi() # Hello, my name is Breno Farias
	my_name = me.name # Breno Farias -> Getter -> return self.__name
	print(f"My Name is {my_name}") # Breno Farias

	print(me) # Person(Breno Farias) -> __repr__
	print(f"")

	other = Person("Manoel Campos")
	print(other) # Person(Manoel Campos) -> __repr__
	print(me == other) # False -> __eq__
	print(f"")

	other._name = "Breno Farias"
	print(other) # Person(Breno Farias) -> __repr__
	print(f"{me} == {other}: {me == other}") # True -> __eq__
	print(f"")

if __name__ == "__main__":
	main()