# Files Operations in Python.

import os  # Operating System Module.
import glob  # Unix style pathname pattern expansion.
from colorama import Style  # For coloring the terminal.

# Macros:
class BackgroundColors:  # Colors for the terminal
   CYAN = "\033[96m" # Cyan
   GREEN = "\033[92m" # Green
   YELLOW = "\033[93m" # Yellow
   RED = "\033[91m" # Red
   BOLD = "\033[1m" # Bold
   UNDERLINE = "\033[4m" # Underline
   CLEAR_TERMINAL = "\033[H\033[J" # Clear the terminal

# Relative path to the current directory is the path to the current directory relative to the current directory.
# Absolute path to the current directory is the path to the current directory relative to the root directory.
# print(f"{BackgroundColors.GREEN}Absolute Path: {BackgroundColors.CYAN}{os.getcwd()}") # Get the current directory.
def main():
   # Get the current file.
   print(f"{BackgroundColors.GREEN}Current File: {BackgroundColors.CYAN}{__file__}{Style.RESET_ALL}")

   # List the files in the current directory.
   print(f"{BackgroundColors.GREEN}Files in the current directory: {BackgroundColors.CYAN}{os.listdir()}{Style.RESET_ALL}")

   filename = "file.txt"  # File name.
   print("")

   # Access the file. "os.access(path, mode)"
   # Modes: os.F_OK - Existence, os.R_OK - Readability, os.W_OK - Writability, os.X_OK - Executability.
   # Check if the file is readable.
   print(f"{BackgroundColors.GREEN}os.access(filename, os.R_OK): {BackgroundColors.CYAN}{os.access(filename, os.R_OK)}{Style.RESET_ALL}")

   # Check if the file exists.
   print(f"{BackgroundColors.GREEN}os.path.exists(filename): {BackgroundColors.CYAN}{os.path.exists(filename)}{Style.RESET_ALL}")
   print("")

   # Walk through the current directory.
   print(f"{BackgroundColors.GREEN}Walking through the current directory:{Style.RESET_ALL}")
   for path in os.walk("."):
      print(f"{BackgroundColors.CYAN}{path}{Style.RESET_ALL}")
   print("")

   # Glob module.
   print(f"{BackgroundColors.GREEN}Glob module:{Style.RESET_ALL}")
   for path in glob.glob("../*/*.py"):
      print(f"{BackgroundColors.CYAN}{path}{Style.RESET_ALL}")
   print("")

   # OS library functions:
   # getatime(path) -> last access time, getctime(path) -> creation time, getmtime(path) -> last modification time
   # getsize(path) -> size of the file in bytes, isfile(path) -> check if the path is a file, isdir(path) -> check if the path is a directory
   # islink(path) -> check if the path is a symbolic link.

   # Get the last access time.
   print(f"{BackgroundColors.GREEN}os.path.getatime(filename) in seconds: {BackgroundColors.CYAN}{os.path.getatime(filename)}{Style.RESET_ALL}")
   # Get the creation time.
   print(f"{BackgroundColors.GREEN}os.path.getctime(filename): {BackgroundColors.CYAN}{os.path.getctime(filename)}{Style.RESET_ALL}")
   # Get the last modification time.
   print(f"{BackgroundColors.GREEN}os.path.getmtime(filename): {BackgroundColors.CYAN}{os.path.getmtime(filename)}{Style.RESET_ALL}")
   # Get the size of the file in bytes.
   print(f"{BackgroundColors.GREEN}os.path.getsize(filename): {BackgroundColors.CYAN}{os.path.getsize(filename)}{Style.RESET_ALL}")
   # Check if the path is a file.
   print(f"{BackgroundColors.GREEN}os.path.isfile(filename): {BackgroundColors.CYAN}{os.path.isfile(filename)}{Style.RESET_ALL}")
   # Check if the path is a directory.
   print(f"{BackgroundColors.GREEN}os.path.isdir(filename): {BackgroundColors.CYAN}{os.path.isdir(filename)}{Style.RESET_ALL}")
   # Check if the path is a symbolic link.
   print(f"{BackgroundColors.GREEN}os.path.islink(filename): {BackgroundColors.CYAN}{os.path.islink(filename)}{Style.RESET_ALL}")
   print(f"")

   # OS library functions:
   # join(path, *paths) -> join the paths, split(path) -> split the path, realpath(path) -> get the exact path (no symbolic links).
   # split(path) -> split the path, splitext(path) -> split the extension from the path
   # normcase(path) -> normalize the case of the path, normpath(path) -> normalize the path, abspath(path) -> get the absolute path.

   current_directory = os.getcwd()  # Get the current directory.
   # Join the paths.
   print(f"{BackgroundColors.GREEN}os.path.join(current_directory, filename): {BackgroundColors.CYAN}{os.path.join(current_directory, filename)}{Style.RESET_ALL}")
   # Split the path.
   print(f"{BackgroundColors.GREEN}os.path.split(__file__): {BackgroundColors.CYAN}{os.path.split(__file__)}{Style.RESET_ALL}")
   # Get the exact path (no symbolic links).
   print(f"{BackgroundColors.GREEN}os.path.realpath(filename): {BackgroundColors.CYAN}{os.path.realpath(filename)}{Style.RESET_ALL}")
   # Split the extension from the path.
   print(f"{BackgroundColors.GREEN}os.path.splitext(filename): {BackgroundColors.CYAN}{os.path.splitext(filename)}{Style.RESET_ALL}")
   # Normalize the case of the path.
   print(f"{BackgroundColors.GREEN}os.path.normcase(filename): {BackgroundColors.CYAN}{os.path.normcase(filename)}{Style.RESET_ALL}")
   # Normalize the path.
   print(f"{BackgroundColors.GREEN}os.path.normpath(filename): {BackgroundColors.CYAN}{os.path.normpath(filename)}{Style.RESET_ALL}")
   # Get the absolute path.
   print(f"{BackgroundColors.GREEN}os.path.abspath(filename): {BackgroundColors.CYAN}{os.path.abspath(filename)}{Style.RESET_ALL}")
   print(f"")

   # Create file named "file.txt" in the current directory, if it doesn't exist.
   file = open(filename, "w")  # Open the file in write mode.
   file.write(f"Hello World!\n")  # Write to the file.
   for i in range(10):
      file.write(f"{i} ")
   file.close()  # Close the file.

   # Read the file content.
   file = open(filename, "r")  # Open the file in read mode.
   # Read the file.
   print(f"{BackgroundColors.GREEN}file.read(): \n{BackgroundColors.CYAN}{file.read()}{Style.RESET_ALL}")
   print(f"")

   # Read the an specific line of the file.
   file = open(filename, "r")  # Open the file in read mode.
   # Read the second line of the file.
   print(
      f"{BackgroundColors.GREEN}file.readlines()[2]: {BackgroundColors.CYAN}{file.readlines()[1]}{Style.RESET_ALL}")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
   main() # Call the main function
