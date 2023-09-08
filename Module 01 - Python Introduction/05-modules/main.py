# Run: pip install module

import my_module.my_module as module # Import the module

def main():
	a, b = 1, 2 # Integer variables
	sum_result = module.sum(a, b) # Call the sum function from the module
	print(f"sum({a}, {b}): {sum_result}")

if __name__ == "__main__":
	main()