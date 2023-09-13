# Files Operations in Python.

import os # Operating System Module.
from colorama import Style # For coloring the terminal.

# Macros:
class backgroundColors: # Colors for the terminal
	CYAN = "\033[96m" # Cyan
	GREEN = "\033[92m" # Green
	YELLOW = "\033[93m" # Yellow
	RED = "\033[91m" # Red

# Relative path to the current directory is the path to the current directory relative to the current directory.
# Absolute path to the current directory is the path to the current directory relative to the root directory.
# print(f"{backgroundColors.GREEN}Absolute Path: {backgroundColors.CYAN}{os.getcwd()}") # Get the current directory.

def main():
	print(f"{backgroundColors.GREEN}Current File: {backgroundColors.CYAN}{__file__}{Style.RESET_ALL}") # Get the current file.

	# List the files in the current directory.
	print(f"{backgroundColors.GREEN}Files in the current directory: {backgroundColors.CYAN}{os.listdir()}{Style.RESET_ALL}")

	filename = "file.txt" # File name.
	# Create file named "file.txt" in the current directory.
	file = open(filename, "w")
	file.write("Hello World!")

	# Close the file.
	file.close()

	print("")

	# Access the file. "os.access(path, mode)"
	# Modes: os.F_OK - Existence, os.R_OK - Readability, os.W_OK - Writability, os.X_OK - Executability.
	print(f"{backgroundColors.GREEN}os.access(filename, os.R_OK): {backgroundColors.CYAN}{os.access(filename, os.R_OK)}{Style.RESET_ALL}") # Check if the file is readable.

	# Check if the file exists.
	print(f"{backgroundColors.GREEN}os.path.exists(filename): {backgroundColors.CYAN}{os.path.exists(filename)}{Style.RESET_ALL}")
	print("")

	# Walk through the current directory.
	print(f"{backgroundColors.GREEN}Walking through the current directory:{Style.RESET_ALL}")
	for path in os.walk("."):
		print(f"{backgroundColors.CYAN}{path}{Style.RESET_ALL}")
	print("")




if __name__ == "__main__":
	main()