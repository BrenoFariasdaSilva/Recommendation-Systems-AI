# Dictionarioes are unordered collections of data in key:value pairs
# Dictionaries are mutable and the keys must be unique
# You can have the value of a key be a list, tuple, or another dictionary

# Create a dictionary
dictionary = {"Breno": "22", "Amanda": "25", "Manoel": "42", "Marcia": "42"}

# Print the dictionary
print(f"dictionary: {dictionary}")
print(f"") # Empty line

# Loop Dictionary
for key, value in dictionary.items():
	print(f"Name: {key}, Age: {value}.")
print(f"") # Empty line

# Operations
print(f"dictionary['Breno']: {dictionary['Breno']}")
print(f"") # Empty line

# Add a new key:value pair
dictionary["Maria"] = "50"
print(f"dictionary: {dictionary}")

# Dictionary Methods
print(f"dictionary.keys(): {dictionary.keys()}")
print(f"dictionary.values(): {dictionary.values()}")
print(f"dictionary.items(): {dictionary.items()}")
print(f"dictionary.copy(): {dictionary.copy()}")
print(f"dictionary.pop('Maria'): {dictionary.pop('Maria')}")
print(f"") # Empty line

# Other methods: popitem, get, setdefault, update, clear
print(f"dicionary.popitem(): {dictionary.popitem()}")
print(f"dictionary.get('Breno'): {dictionary.get('Breno')}")
print(f"dictionary.setdefault('Breno', '22'): {dictionary.setdefault('Breno', '22')}")

dictionary.update({'Breno': '23'})
print(f"dictionary.update: {dictionary}")
print(f"dictionary.clear(): {dictionary.clear()}")
print(f"") # Empty line

# Create Dictionary from List Comprehension
new_dictionary = {key: value for key, value in zip(["Breno", "Amanda", "Manoel", "Marcia"], ["22", "25", "42", "42"])}
print(f"new_dictionary: {new_dictionary}")
print(f"") # Empty line