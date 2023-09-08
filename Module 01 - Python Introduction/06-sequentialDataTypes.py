# Sequential Data Types:

## Lists: Lists are mutable, ordered, and can contain any data type.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(f"list1: {list1}")

if 1 in list1:
	print("1 is in list")

if 6 not in list1:
	print("6 is not in list")

# Concatenate the lists
list3 = list1 + list2
print(f"list1 + list2: {list3}")

# Multiply the list1 by 2
print(f"list1 * 2: {list1 * 2}")

# Get element at index 0
print(f"list1[0]: {list1[0]}")

# Get elements from index 0 to 2
print(f"list1[0:2]: {list1[0:2]}")

# Get elements from index 0 to 5 with step 2
print(f"list1[0:5:2]: {list1[0:5:2]}")

# Create a reference to a list
list1_reference = list1
print(f"list1_reference is list1: {list1_reference is list1}")
print(f"list1_reference: {list1_reference}")

list1 += [6]
print(f"list1: {list1}")

print(f"list1_reference: {list1_reference}")
print(f"list1_reference is list1: {list1_reference is list1}")

# List Indexes
print(f"list1.index(1): {list1.index(1)}")
print(f"list1.index(5): {list1.index(5)}")

# list.index(element, start, end)
# Find the index of the element 4 between index 2 and 5
print(f"list1.index(4, 2, 5): {list1.index(4, 2, 5)}")

# Min and Max
print(f"min(list1): {min(list1)}")
print(f"max(list1): {max(list1)}")

# Count
list1 += [1, 1, 1, 1]
print(f"list1.count(1): {list1.count(1)}")

# Append
list1.append(11)
print(f"list1: {list1}")
