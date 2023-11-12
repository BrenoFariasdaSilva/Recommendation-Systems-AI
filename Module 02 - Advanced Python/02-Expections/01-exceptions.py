# Exceptions in Python
# Exceptions are used to handle errors and other events that may occur during the execution of a program.
# The try statement works as follows:
# First, the try clause (the statement(s) between the try and except keywords) is executed.
# If no exception occurs, the except clause is skipped and execution of the try statement is finished.
# If an exception occurs during execution of the try clause, the rest of the clause is skipped.
# Then if its type matches the exception named after the except keyword, the except clause is executed,
# and then execution continues after the try statement.

def open_file(filename):
	f = open(filename, "r")

def open_file_with_exception(filename):
	try: # Required
		f = open(filename, "r")
	except FileNotFoundError as e: # Optional
		print(f"File {filename} ERROR: {e}")
		return None
	else: # Optional - Runs if no exception occurs.
		print("Else runs if no exception occurs.")
		return f
	finally: # Optional - Always runs, independent if any exception occurs or not.
		print("Finally always runs.")
		return None

def main():
	# Open File without Exception.
	# open_file("random.txt")
	# print(f"")

	# Open File with Exception.
	open_file_with_exception("random.txt")
	print(f"")

	print("End of Program.")

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
	main() # Call the main function

