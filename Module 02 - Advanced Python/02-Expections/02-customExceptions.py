# Exceptions in Python
# Exceptions are used to handle errors and other events that may occur during the execution of a program.
# The try statement works as follows:
# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# If an exception occurs during execution of the try clause, the rest of the clause is skipped.
# Then if its type matches the exception named after the except keyword, the except clause is executed,
# and then execution continues after the try statement.

class UnknownAnimalError(Exception):
	def __init__(self, animal, message="Unknown Animal."):
		self.animal = animal
		self.message = message
		super().__init__(self.message)

def add_animal(inventory, animal):
	known_animals = ["dog", "cat", "fish"]
	if animal not in known_animals:
		raise UnknownAnimalError(animal)
	else:
		inventory.append(animal)

def main():
	inventory = [] # Empty List
	try:
		add_animal(inventory, "dog")
		add_animal(inventory, "cat")
		add_animal(inventory, "fish")
		add_animal(inventory, "bird")
	except UnknownAnimalError as e:
		print(f"Error: {e.message} -> {e.animal} is not a known animal.")
	finally:
		print(f"Inventory: {inventory}")

if __name__ == "__main__":
	main()
