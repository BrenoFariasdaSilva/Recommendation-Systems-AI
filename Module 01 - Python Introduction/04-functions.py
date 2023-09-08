# FUNCTIONS:
print(f"FUNCTIONS:")

## Function Definition:
def hello_world():
	print(f"Hi from the Hello World Function!")

# The type of the arguments is not a requirement, but it is a good practice
# The return type is not a requirement, but it is a good practice
# Those types will not be enforced by the interpreter, so if you pass floats to the sum function, it will work, just like in line 28 and 29.
def sum(a: int, b: int = 0) -> int:
	# if not isinstance(a, int) or not isinstance(b, int):
		# raise ValueError("Both 'a' and 'b' must be integers")
	return a + b

## Function Call:
hello_world()
print(f"") # Empty print statement

sum_result = sum(1, 2)
print(f"sum(1, 2): {sum_result}")
print(f"") # Empty print statement

sum_result = sum(1)
print(f"sum(1): {sum_result}")
print(f"") # Empty print statement

sum_result = sum(1.2, 2.3)
print(f"sum(1.2, 2.3): {sum_result}")
print(f"") # Empty print statement

