# Files Operations in Python.

import os # Operating System Module.
import glob # Unix style pathname pattern expansion.
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

	# Glob module.
	print(f"{backgroundColors.GREEN}Glob module:{Style.RESET_ALL}")
	for path in glob.glob("../*/*.py"):
		print(f"{backgroundColors.CYAN}{path}{Style.RESET_ALL}")
	print("")

	# OS library functions: 
	# getatime(path) -> last access time, getctime(path) -> creation time, getmtime(path) -> last modification time
	# getsize(path) -> size of the file in bytes, isfile(path) -> check if the path is a file, isdir(path) -> check if the path is a directory
	# islink(path) -> check if the path is a symbolic link.

	print(f"{backgroundColors.GREEN}os.path.getatime(filename) in seconds: {backgroundColors.CYAN}{os.path.getatime(filename)}{Style.RESET_ALL}") # Get the last access time.
	print(f"{backgroundColors.GREEN}os.path.getctime(filename): {backgroundColors.CYAN}{os.path.getctime(filename)}{Style.RESET_ALL}") # Get the creation time.
	print(f"{backgroundColors.GREEN}os.path.getmtime(filename): {backgroundColors.CYAN}{os.path.getmtime(filename)}{Style.RESET_ALL}") # Get the last modification time.
	print(f"{backgroundColors.GREEN}os.path.getsize(filename): {backgroundColors.CYAN}{os.path.getsize(filename)}{Style.RESET_ALL}") # Get the size of the file in bytes.
	print(f"{backgroundColors.GREEN}os.path.isfile(filename): {backgroundColors.CYAN}{os.path.isfile(filename)}{Style.RESET_ALL}") # Check if the path is a file.
	print(f"{backgroundColors.GREEN}os.path.isdir(filename): {backgroundColors.CYAN}{os.path.isdir(filename)}{Style.RESET_ALL}") # Check if the path is a directory.
	print(f"{backgroundColors.GREEN}os.path.islink(filename): {backgroundColors.CYAN}{os.path.islink(filename)}{Style.RESET_ALL}") # Check if the path is a symbolic link.
	print(f"")

	# OS library functions:
	# join(path, *paths) -> join the paths, split(path) -> split the path, realpath(path) -> get the exact path (no symbolic links).
	# split(path) -> split the path, splitext(path) -> split the extension from the path
	# normcase(path) -> normalize the case of the path, normpath(path) -> normalize the path, abspath(path) -> get the absolute path.
	
	current_directory = os.getcwd() # Get the current directory.
	print(f"{backgroundColors.GREEN}os.path.join(current_directory, filename): {backgroundColors.CYAN}{os.path.join(current_directory, filename)}{Style.RESET_ALL}") # Join the paths.
	print(f"{backgroundColors.GREEN}os.path.split(filename): {backgroundColors.CYAN}{os.path.split(filename)}{Style.RESET_ALL}") # Split the path.
	print(f"{backgroundColors.GREEN}os.path.realpath(filename): {backgroundColors.CYAN}{os.path.realpath(filename)}{Style.RESET_ALL}") # Get the exact path (no symbolic links).
	print(f"{backgroundColors.GREEN}os.path.splitext(filename): {backgroundColors.CYAN}{os.path.splitext(filename)}{Style.RESET_ALL}") # Split the extension from the path.
	print(f"{backgroundColors.GREEN}os.path.normcase(filename): {backgroundColors.CYAN}{os.path.normcase(filename)}{Style.RESET_ALL}") # Normalize the case of the path.
	print(f"{backgroundColors.GREEN}os.path.normpath(filename): {backgroundColors.CYAN}{os.path.normpath(filename)}{Style.RESET_ALL}") # Normalize the path.
	print(f"{backgroundColors.GREEN}os.path.abspath(filename): {backgroundColors.CYAN}{os.path.abspath(filename)}{Style.RESET_ALL}") # Get the absolute path.


if __name__ == "__main__":
	main()

