# Oriented Object Programming in Python.
# Dataclasses are a simple way to create classes that are mainly used to store data.

from dataclasses import dataclass

# @dataclass decorator automatically generates special methods for you, like __init__(), __repr__(), __eq__(), and more.
# The attributed using the dataclass are public by default, but you can make them protected by using a single underscore before the attribute name.

# Example:
# @dataclass
# class Person:
# 	_name: str
#	_age: int

@dataclass
class Person:
	name: str
	age: int

	def say_hi(self):
		print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

def main():
	me = Person("Breno", 23)
	me.say_hi() # Hello, my name is Breno and I'm 23 years old.

	me.name = "Breno Farias"
	me.age = 24 # Update the age attribute
	me.say_hi() # Hello, my name is Breno Farias and I'm 23 years old.

	print(me) # Person(name='Breno Farias', age=24)
	print(f"")

	other = Person("Manoel Campos", 42)
	print(other) # Person(name='Manoel Campos', age=42)
	print(f"")

	print(f"{me} == {other}: {me == other}") # False

	other.name = "Breno Farias"
	other.age = 24
	print(other) # Person(name='Breno Farias', age=24)
	print(f"")

	print(f"{me} == {other}: {me == other}") # True

if __name__ == "__main__":
	main()