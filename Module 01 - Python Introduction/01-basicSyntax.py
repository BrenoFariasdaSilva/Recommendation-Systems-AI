print(f"BASIC PYTHON SYNTAX:")

## Print Statements:
print(f"PRINT STATEMENTS:")
print(f"Hello World!") # Strings can be used with double quotes
print(f'Hello World!') # Strings can be used with single quotes
print(f"") # Empty print statement

## Comments:
# Single Line Comment:
# print(f"Hello World!")

# Multi Line Comment:
'''
print(f"Hello World!")
print(f"Hello World!")
print(f"Hello World!")
'''

## Variables:
print(f"VARIABLES:")
integer_variable = 1 # Integer
float_variable = 1.0 # Float
string_variable = "Hello World!" # String
boolean_variable = True # Boolean

## Print Variables in different formats:
print("integer variable:", integer_variable)
print("type(integer_variable):", type(integer_variable))
print(f"") # Empty print statement

print("float variable: " + str(float_variable)) # To concatenate a string with a float, we need to convert the float to a string
print("type(float_variable): " + str(type(float_variable))) # To concatenate a string with a float, we need to convert the float to a string
print(f"") # Empty print statement

print(f"string variable: {str(string_variable)}")
print(f"type(string_variable): {str(type(string_variable))}")
print(f"") # Empty print statement

print("boolean variable: {}".format(boolean_variable))
print("type(boolean_variable): {}".format(type(boolean_variable)))
print(f"") # Empty print statement

## Type Conversion:
print(f"TYPE CONVERSION:")
print(f"float(integer_variable): {float(integer_variable)}")
print(f"type(float(integer_variable)): {type(float(integer_variable))}")
print(f"") # Empty print statement

print(f"int(float_variable): {int(float_variable)}")
print(f"type(int(float_variable)): {type(int(float_variable))}")
print(f"") # Empty print statement

print(f"str(integer_variable): {str(integer_variable)}")
print(f"type(str(integer_variable)): {type(str(integer_variable))}")
print(f"") # Empty print statement

print(f"str(float_variable): {str(float_variable)}")
print(f"type(str(float_variable)): {type(str(float_variable))}")
print(f"") # Empty print statement

print(f"str(boolean_variable): {str(boolean_variable)}")
print(f"type(str(boolean_variable)): {type(str(boolean_variable))}")
print(f"") # Empty print statement

## Arithmetic Operators:
print(f"ARITHMETIC OPERATORS:")
print(f"SUM: integer_variable + integer_variable: {integer_variable + integer_variable}")
print(f"SUBTRACTION: integer_variable - integer_variable: {integer_variable - integer_variable}")
print(f"MULTIPLICATION: integer_variable * integer_variable: {integer_variable * integer_variable}")
print(f"DIVISION: integer_variable / integer_variable: {integer_variable / integer_variable}")
print(f"EXPONENTIATION: integer_variable ** integer_variable: {integer_variable ** integer_variable}")
print(f"DIVISION (INTEGER): integer_variable // integer_variable: {integer_variable // integer_variable}")
print(f"DIVISION (REMAINDER): integer_variable % integer_variable: {integer_variable % integer_variable}")
print(f"") # Empty print statement

## Attribution Operators:
print(f"ATTRIBUTION OPERATORS:")
print(f"EQUALS: =")
print(f"SUM: +=")
print(f"SUBTRACTION: -=")
print(f"MULTIPLICATION: *=")
print(f"DIVISION: /=")
print(f"EXPONENTIATION: **=")
print(f"") # Empty print statement

## Comparison Operators:
print(f"COMPARISON OPERATORS:")
print(f"EQUALS: ==")
print(f"DIFFERENT: !=")
print(f"GREATER THAN: >")
print(f"LESS THAN: <")
print(f"GREATER THAN OR EQUALS: >=")
print(f"LESS THAN OR EQUALS: <=")
print(f"") # Empty print statement

## Logical Operators:
print(f"LOGICAL OPERATORS:")
print(f"AND: and")
if integer_variable == 1 and float_variable == 1.0:
	print(f"integer_variable == 1 and float_variable == 1.0: {integer_variable == 1 and float_variable == 1.0}")
print(f"OR: or")
if integer_variable == 1 or float_variable == 1.0:
	print(f"integer_variable == 1 or float_variable == 1.0: {integer_variable == 1 or float_variable == 1.0}")
print(f"NOT: not")
if not integer_variable == -1:
	print(f"not integer_variable == -1: {not integer_variable == 1}")
print(f"") # Empty print statement

## String and Indexing:
print(f"STRING, INDEXING AND SLICING:")
string_variable = "Hello World!"
print(f"string_variable: {string_variable}")
print(f"string_variable[0]: {string_variable[0]}") # Indexing starts from 0
print(f"string_variable[1]: {string_variable[1]}") # Indexing starts from 0
print(f"string_variable[-1]: {string_variable[-1]}") # Indexing starts from -1
print(f"string_variable[0:5]: {string_variable[0:5]}") # The last index is not included
print(f"string_variable[-6:-1]: {string_variable[-6:-1]}") # The last index is not included
print(f"") # Empty print statement

## String Operators:
print(f"STRING OPERATORS:")
print(f"IN: in") # Returns True if the string is in the string
print(f"'Hello' in {string_variable}: {'Hello' in string_variable}")
print(f"NOT IN: not in") # Returns True if the string is not in the string
print(f"'Hello' not in {string_variable}: {'Hello' not in string_variable}")
print(f"CONCATENATION: +") # Concatenates two strings
print(f"'Hello' + 'World!': {'Hello' + 'World!'}")
print(f"REPETITION: *") # Repeats the string n times
print(f"'Hello ' * 3: {'Hello ' * 3}")
second_string_variable = string_variable
print(f"IS: is") # Returns True if the strings are the same object
print(f"{string_variable} is {second_string_variable}: {string_variable is second_string_variable}")
print(f"") # Empty print statement

## Importing Modules:
print(f"IMPORTING MODULES:")
import math
print(f"math.sqrt(4): {math.sqrt(4)}")
print(f"math.pi: {math.pi}")
print(f"math.e: {math.e}")
print(f"math.cos(math.pi): {math.cos(math.pi)}")
print(f"math.sin(math.pi): {math.sin(math.pi)}")
print(f"math.tan(math.pi): {math.tan(math.pi)}")
print(f"") # Empty print statement

# Nicknaming Modules:
print(f"NICKNAMING MODULES:")
import math as m
print(f"m.sqrt(4): {m.sqrt(4)}")
print(f"") # Empty print statement

# Importing Specific Functions:
print(f"IMPORTING SPECIFIC FUNCTIONS:")
from math import sqrt
print(f"sqrt(4): {sqrt(4)}")
print(f"") # Empty print statement