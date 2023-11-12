# Oriented Object Programming in Python.
# Encapsulation is made by the use of __ (double underscore) before the attribute name, 
# which makes it private, and can only be accessed by methods inside the class (getters and setters).

class Person:
	def __init__(self, name): # Constructor -> __init__
		self.__name = name # Private Attribute

	def __repr__(self):
		return f"Person(Name: {self.__name})"
	
	def __eq__(self, other):
		return self.__name == other.__name

	def say_hi(self): # Method
		print(f"Hello, my name is {self.__name}")

	def set_name(self, name): # Setter
		self.__name = name

	def get_name(self): # Getter
		return self.__name

def main():
	me = Person("Breno") # Constructor -> __init__
	me.say_hi() # Hello, my name is Breno
	me.set_name("Breno Farias") # Setter -> __name = "Breno Farias"
	my_name = me.get_name() # Breno Farias -> Getter -> return self.__name
	print(f"My Name is {my_name}") # Breno Farias

	print(me) # Person(Breno Farias) -> __repr__

	print(f"")

	other = Person("Manoel Campos")
	print(other) # Person(Manoel Campos) -> __repr__
	print(me == other) # False -> __eq__

	other.set_name("Breno Farias")
	print(other) # Person(Breno Farias) -> __repr__
	print(me == other) # True -> __eq__

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
	main() # Call the main function
