# List Operations:

## Modify Elements:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list[0] = -1
print(f"list[0] = -1: {list}")

list[0:3] = [-1, -2, -3]
print(f"list[0:3] = [-1, -2, -3]: {list}")

print(f"") # Empty line

## Delete Elements:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

del list[-1]
print(f"del list[-1]: {list}")

del list[0:3]
print(f"del list[0:3]: {list}")

print(f"") # Empty line

## Instance Methods:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Append (Add)
list.append(6)
print(f"list.append(6): {list}")
print(f"") # Empty line

# Extend (Concatenate)
list.extend([7, 8, 9, 10])
print(f"list.extend([7, 8, 9, 10]): {list}")
print(f"") # Empty line

# Insert value at a specific index
list.insert(0, 0)
print(f"list.insert(0, 0): {list}")
print(f"") # Empty line

# Remove a specific value from the list
list.remove(0)
print(f"list.remove(0): {list}")
print(f"") # Empty line

# Pop (Remove the last element)
list.pop()
print(f"list.pop(): {list}")
print(f"") # Empty line

# Reverse
list.reverse()
print(f"list.reverse(): {list}")
print(f"") # Empty line

# Clear (Remove all elements)
list.clear()
print(f"list.clear(): {list}")

## Sort - Data must be of the same type (int, float, str)
list = [5, 4, 3, 2, 1]

list.sort()
print(f"list.sort(): {list}")
print(f"") # Empty line

# Sort with Key
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list.sort(reverse=True)
print(f"list.sort(reverse=True): {list}")
print(f"") # Empty line

## List Comprehension:
list = [1, 2, 3, 4, 5]
square_list = [x ** 2 for x in list]
print(f"square_list: {square_list}")

letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5]
letter_number_list = [(letter, number) for letter in letters for number in numbers]
print(f"letter_number_list: {letter_number_list}")
print(f"") # Empty line

# List Comprehension with Conditionals:
list = [1, 2, 3, 4, 5]
even_list = [x for x in list if x % 2 == 0]
print(f"even_list: {even_list}")
print(f"") # Empty line

## Tuples - Immutable Lists:
tuple = (1, 2, 3, 4, 5)
print(f"tuple: {tuple}")
print(f"") # Empty line

# Packing and Unpacking:
clock = 9,30,0
(h, m, s) = clock
print(f"clock: {clock}")
print(f"{h}h:{m}m:{s}s")
