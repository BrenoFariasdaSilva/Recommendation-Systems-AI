# Regular Expressions in Python.
# Regular Expressions are a sequence of characters that define a search pattern.

import re # Regular Expressions Module
from colorama import Style # For coloring the terminal

# Macros:
class backgroundColors: # Colors for the terminal
	CYAN = "\033[96m" # Cyan
	GREEN = "\033[92m" # Green
	YELLOW = "\033[93m" # Yellow
	RED = "\033[91m" # Red
	BOLD = "\033[1m" # Bold
	UNDERLINE = "\033[4m" # Underline
	CLEAR_TERMINAL = "\033[H\033[J" # Clear the terminal

def main():
	name = "Breno Farias da Silva"
	print(f"{backgroundColors.GREEN}Name: {backgroundColors.CYAN}{name}{Style.RESET_ALL}")
	print(f"")

	# Search for a pattern in a string.
	# The search() method returns the first match.
	# The match() method returns a match object if there is a match at the beginning of the string.
	# The fullmatch() method returns a match object if all characters in the string match the pattern. Doesn't need anchors.
	# The findall() method returns a list containing all matches.
	# The finditer() method returns an iterator containing all matches.
	# The split() method returns a list where the string has been split at each match.
	# The sub() method replaces the matches with the text of your choice.
	# The subn() method returns a tuple containing the new string value and the number of replacements made.
	# The escape() method returns a string with backslashes before characters that need to be escaped.
	# The purge() method clears the regular expression cache.

	result = re.search(r"a|b", name, flags=re.IGNORECASE) # Search for a or b in name and ignore case sensitive.
	print(f"{backgroundColors.GREEN}Search for a or b in {backgroundColors.CYAN}{name}{backgroundColors.GREEN}: {backgroundColors.CYAN}{result}{Style.RESET_ALL}")

	# Anchors:
	# ^ -> Start of line.
	# $ -> End of line.
	# \A -> Start of string.
	# \Z -> End of string.

	result = re.search(r"\ABreno", name) # Search for Breno at the start of the string.
	print(f"{backgroundColors.GREEN}Search for Breno at the start of the string {backgroundColors.CYAN}{name}{backgroundColors.GREEN}: {backgroundColors.CYAN}{result}{Style.RESET_ALL}")

	numbers = "12123123"
	result = re.search(r"\A(0|1|2|3)*\Z", numbers) # Search for Silva at the end of the string.
	print(f"{backgroundColors.GREEN}Search numbers: {backgroundColors.CYAN}{result}{Style.RESET_ALL}")
	print(f"")

	test=re.compile(r"ab*") # Compile the pattern.
	entry = "abbb" # Entry to test.
	# entry = "abbbbbaaaaab" # Entry to test.
	result=test.findall(entry) # Match the entry.
	print(f"{backgroundColors.GREEN}Test: {backgroundColors.CYAN}{result}{Style.RESET_ALL}")
	print(f"")

	# Abbreaviations:
	# \d -> Any numéric digit [0-9].
	# \D -> Any non-numéric digits (not a number) [^0-9].
	# \w -> Any alphanumeric character [a-zA-Z0-9_].
	# \W -> Any non-alphanumeric character (not a number) [^a-zA-Z0-9_].
	# \s -> Any whitespace character [ \t\n\r\f\v].
	# \S -> Any non-whitespace character (not a number) [^ \t\n\r\f\v].	

	test=re.compile(r"\d{5}-?\d{3}") # Compile the pattern.
	print(f"{backgroundColors.GREEN}test.match('77800-000123'): {backgroundColors.CYAN}{test.fullmatch('77800-000123')}{Style.RESET_ALL}")
	print(f"{backgroundColors.GREEN}test.match('77800-000'): {backgroundColors.CYAN}{test.match('77800-000')}{Style.RESET_ALL}")
	print(f"{backgroundColors.GREEN}test.match('77800000'): {backgroundColors.CYAN}{test.match('77800000')}{Style.RESET_ALL}")
	print(f"")

	test=re.compile(r"\s") # Compile the pattern.
	print(f"{backgroundColors.GREEN}test.split('I am Studying Computer Science'): {backgroundColors.CYAN}{test.split('I am Studying Computer Science')}{Style.RESET_ALL}")
	print(f"")

	test=re.compile("alunos") # Compile the pattern.
	print(f"{backgroundColors.GREEN}test.sub('estudantes', 'Os alunos estão estudando'): {backgroundColors.CYAN}{test.sub('estudantes', 'Os alunos estão estudando')}{Style.RESET_ALL}")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main() # Call the main function
