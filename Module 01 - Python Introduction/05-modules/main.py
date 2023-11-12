import my_module.my_module as module # Import the module

def main():
	a, b = 1, 2 # Integer variables
	sum_result = module.sum(a, b) # Call the sum function from the module
	print(f"sum({a}, {b}): {sum_result}")

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
	main() # Call the main function
