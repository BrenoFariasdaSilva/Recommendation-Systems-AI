# Regular Expressions in Python.
# Regular Expressions are a sequence of characters that define a search pattern.

import re  # Regular Expressions Module
from colorama import Style  # For coloring the terminal

# Macros:
class backgroundColors:  # Colors for the terminal
   CYAN = "\033[96m"  # Cyan
   GREEN = "\033[92m"  # Green
   YELLOW = "\033[93m"  # Yellow
   RED = "\033[91m"  # Red
   BOLD = "\033[1m"  # Bold
   UNDERLINE = "\033[4m"  # Underline
   CLEAR_TERMINAL = "\033[H\033[J"  # Clear the terminal

def main():
   # Compile the pattern.
   standard_cpf = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}|^\d{11}$")

   cpfs = ["123.456.789-00", "12345678900", "1234567890012", "123456789"]

   for cpf in cpfs:
      result = standard_cpf.findall(cpf)
      print(f"result: {result}")
      if result:
         print(f"{backgroundColors.GREEN}CPF: {backgroundColors.CYAN}{cpf}{backgroundColors.GREEN} is valid.{Style.RESET_ALL}")
      else:
         print(f"{backgroundColors.RED}CPF: {backgroundColors.CYAN}{cpf}{backgroundColors.RED} is invalid.{Style.RESET_ALL}")
      print("")

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
   main() # Call the main function
