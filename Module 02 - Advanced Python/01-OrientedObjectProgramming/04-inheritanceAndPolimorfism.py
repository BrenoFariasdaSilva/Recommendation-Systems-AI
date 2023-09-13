# Oriented Object Programming in Python.
# Inheritance is made by the use of (ClassName) after the class name.
# Polimorphism is made by the use of the same method name in different classes, which has different implementations (behaviors).

# The Animal class is the parent class of Dog and Cat.
class Animal:
	def __init__(self, name):
		self._name = name

	def __repr__(self):
		return f"Animal(Name: {self._name})"
	
	def __eq__(self, other):
		return f"Animal(Name: {self._name})" == f"Animal(Name: {other._name})"
	
	def walk(self):
		print(f"{self._name} is walking.")

# The Dog class is the child class of Animal.
# The Dog class inherits all the attributes and methods from the Animal class, like: __init__(), __repr__(), __eq__(), walk().
class Dog(Animal):
	def __init__(self, name, dog_breed): # Constructor -> __init__
		self.__dog_breed = dog_breed # Private Attribute that has been created in the Dog class.
		super().__init__(name) # Call the parent class constructor

	def __repr__(self): # Override the __repr__ method, as they have the same name, but different implementations.
		return f"Dog(Name: {self._name}, Dog Breed: {self.__dog_breed})" # Return a string representation of the object.
	
	def __eq__(self, other): # Override the __eq__ method, as they have the same name, but different implementations.
		return f"Dog(Name: {self._name})" == f"Dog(Name: {other._name})"
	
	def bark(self): # New Method, specific to the Dog class.
		print(f"{self._name} is barking.") # Print a message to the console.

	def get_dog_breed(self):
		return self.__dog_breed

# The Cat class is the child class of Animal.
# The Cat class inherits all the attributes and methods from the Animal class, like: __init__(), __repr__(), __eq__(), walk().
class Cat(Animal):
	def __init__(self, name): # Constructor -> __init__
		super().__init__(name) # Call the parent class constructor

	def __repr__(self): # Override the __repr__ method, as they have the same name, but different implementations.
		return f"Cat(Name: {self._name})" # Return a string representation of the object.
	
	def __eq__(self, other): # Override the __eq__ method, as they have the same name, but different implementations.
		return f"Cat(Name: {self._name})" == f"Cat(Name: {other._name})" # Return a boolean value.
	
	def meow(self): # New Method, specific to the Cat class.
		print(f"{self._name} is meowing.") # Print a message to the console

def main():
	animal = Animal("Animal") # Constructor -> __init__
	animal.walk() # Animal is walking.
	print(animal) # Animal(Name: Animal)
	print(f"")

	dog = Dog("Dog", "Shih Tzu") # Constructor -> __init__
	dog.walk() # Dog is walking.
	dog.bark() # Dog is barking.
	print(dog) # Dog(Name: Dog)
	dog_breed = dog.get_dog_breed()
	print(f"Dog Breed: {dog_breed}.")
	print(f"")

	cat = Cat("Cat") # Constructor -> __init__
	cat.walk() # Cat is walking.
	cat.meow() # Cat is meowing.
	print(cat) # Cat(Name: Cat)
	print(f"")

	print(f"{animal} == {dog}: {animal == dog}") # False
	print(f"{animal} == {cat}: {animal == cat}") # False
	print(f"{dog} == {cat}: {dog == cat}") # False
	print(f"{dog} == {dog}: {dog == dog}") # True
	print(f"{cat} == {cat}: {cat == cat}") # True

if __name__ == "__main__":
	main()