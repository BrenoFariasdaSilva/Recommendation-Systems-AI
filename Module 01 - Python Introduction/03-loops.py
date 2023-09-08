# Loops Statements:
print(f"LOOPS STATEMENTS:")

## While Loops:
print(f"WHILE LOOPS: while i < stop:")
i = 0 # Integer
while i < 10: # While i is less than 10
	print(f"{i}", end=' ') # Print i
	i += 1 # Increment i by 1
print(f"") # Empty print statement
print(f"") # Empty print statement

## For Loops:
print(f"FOR LOOPS: for i in range(stop):")
for i in range(10): # For i in range 0 to 9
	print(f"{i}", end=' ') # Print i
print(f"") # Empty print statement
print(f"") # Empty print statement

## Different ways to use For Loops:
print(f"DIFFERENT WAYS TO USE FOR LOOPS:")
print(f"FOR LOOPS WITH LISTS: for name in names_list:")
names_list = ["Breno", "Manoel", "Marcia", "Amanda"]
print(f"Names List: ", end='')
for name in names_list: # For name in names_list
	print(f"{name}", end=' ') # Print name
print(f"") # Empty print statement
print(f"") # Empty print statement

## For Loops with Range:
print(f"FOR LOOPS WITH RANGE: for i in range(start, stop):")
for i in range(1, 11): # For i in range 1 to 10
	print(f"{i}", end=' ') # Print i
print(f"") # Empty print statement
print(f"") # Empty print statement

## For Loops with Range and Step:
print(f"FOR LOOPS WITH RANGE AND STEP: for i in range(start, stop, step):")
for i in range(1, 11, 2): # For i in range 1 to 10 with step 2
	print(f"{i}", end=' ') # Print i
print(f"") # Empty print statement
print(f"") # Empty print statement

## For Loops with Range and Negative Step:
print(f"FOR LOOPS WITH RANGE AND NEGATIVE STEP: for i in range(start, stop, -step):")
for i in range(10, 0, -1): # For i in range 10 to 1 with step -1
	print(f"{i}", end=' ') # Print i
print(f"") # Empty print statement
print(f"") # Empty print statement

## Nested For Loops:
print(f"NESTED FOR LOOPS:")
for i in range(6): # For i in range 0 to 5
	print(f"Times Table for {i}:", end=' ')
	for j in range(11): # For j in range 0 to 10
		print(f"{i*j}", end=' ') # Print ij
	print(f"") # Empty print statement
print(f"") # Empty print statement

## Break Statements:
print(f"BREAK STATEMENTS: break")
attendance_list = ["Breno", "Manoel", "Marcia", "Amanda"]
for name in attendance_list: # For name in names_list
	if name == "Manoel": # If name is Manoel
		print(f"Manoel is here!") # Print Manoel is here!
		break # Break the loop
print(f"") # Empty print statement

## Continue Statements:
print(f"CONTINUE STATEMENTS: continue")
attendance_list = ["Breno", "Manoel", "Marcia", "Amanda"]
for name in attendance_list: # For name in names_list
	if name == "Manoel": # If name is Manoel
		print(f"Manoel is here!") # Print Manoel is here!
		continue # Continue the loop
	if name == "Marcia":
		print(f"Marcia is here!")
		break