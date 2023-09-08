# Sets - Sets are a unordered collection of unique elements that could be of any/mixed data type
# Fronzensets - Frozensets are immutable sets

# Create a set
set = {1, 2, 3, 4, 5}
print(f"set: {set}")
print(f"") # Empty line

# Set Comprenhension
set = {x for x in range(1, 6)}
print(f"set: {set}")
print(f"") # Empty line

# Set Operators
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
print(f"set1 | set2: {set1 | set2}")
print(f"set1.union(set2): {set1.union(set2)}")
print(f"") # Empty line

# Intersection
print(f"set1 & set2: {set1 & set2}")
print(f"set1.intersection(set2): {set1.intersection(set2)}")
print(f"") # Empty line

# Difference
print(f"set1 - set2: {set1 - set2}")
print(f"set1.difference(set2): {set1.difference(set2)}")
print(f"") # Empty line

# Symmetric Difference - Elements that are in one set or the other but not both
print(f"set1 ^ set2: {set1 ^ set2}")
print(f"set1.symmetric_difference(set2): {set1.symmetric_difference(set2)}")
print(f"") # Empty line

# Frozen Set
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"frozen_set: {frozen_set}")
print(f"frozen_set: {type(frozen_set)}")
print(f"") # Empty line

# Sets Methods - isdisjoint(), issubset(), issuperset(), copy(), add(), remove(), discard(), pop(), clear()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# isdisjoint() - Returns True if two sets have a null intersection
print(f"Disjoint sets is a set whose intersection is the empty set")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")
print(f"") # Empty line

# issubset() - Returns True if another set contains this set
print(f"Subset is a set A is a subset of a set B if all elements of A are in B")
print(f"set1.issubset(set2): {set1.issubset(set2)}")
print(f"") # Empty line

# issuperset() - Returns True if this set contains another set
print(f"Superset is a set A is a superset of a set B if all elements of B are in A")
print(f"set1.issuperset(set2): {set1.issuperset(set2)}")
print(f"") # Empty line

# copy() - Returns a shallow copy of a set
set3 = set1.copy()

# add() - Adds an element to the set
set1.add(6)
print(f"set1.add(6): {set1}")

# remove() - Removes an element from the set. If the element is not a member, raises a KeyError
set1.remove(6)
print(f"set1.remove(6): {set1}")

# discard() - Removes an element from the set if it is a member. If the element is not a member, does nothing
set1.discard(6)
print(f"set1.discard(6): {set1}")

# pop() - Removes and returns an arbitrary set element. Raises KeyError if the set is empty
element = set1.pop()
print(f"element = set1.pop(): {set1}, element: {element}")

# clear() - Removes all elements from the set
set1.clear()
print(f"set1.clear(): {set1}")
print(f"") # Empty line

# Mutale Sets Methods - update(), intersection_update(), difference_update(), symmetric_difference_update()	
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# update() - Update a set with the union of itself and others
set1.update(set2)
print(f"set1.update(set2): {set1}")

# intersection_update() - Update a set with the intersection of itself and another
set1.intersection_update(set2)
print(f"set1.intersection_update(set2): {set1}")

# difference_update() - Update a set with the difference of itself and another
set1.difference_update(set2)
print(f"set1.difference_update(set2): {set1}")

# symmetric_difference_update() - Update a set with the symmetric difference of itself and another
set1.symmetric_difference_update(set2)
print(f"set1.symmetric_difference_update(set2): {set1}")
