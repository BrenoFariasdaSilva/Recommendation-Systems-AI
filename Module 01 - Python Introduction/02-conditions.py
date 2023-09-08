## Conditional Statements
print(f"CONDITIONAL STATEMENTS:")

## If Statements:
print(f"IF STATEMENTS:")
if True:
	print(f"True")

if False == False:
	print(f"False")

integer_variable = 10 # Integer

if integer_variable == 10:
	print(f"x is equal to 10")

if integer_variable > 0:
	print(f"x is greater than 0")

if type(integer_variable) == int:
	print(f"x is an integer")

string_variable = "Hello World!" # String
if string_variable == "Hello World!":
	print(f"string_variable is equal to Hello World!")

if type(string_variable) == str:
	print(f"string_variable is a string")

if 'Hello' in string_variable:
	print(f"Hello is in string_variable")

print(f"") # Empty print statement

## If Else Statements:
print(f"IF ELSE STATEMENTS:")

age = 18
if age >= 18:
	print(f"You are old enough to vote!")
else:
	print(f"You are not old enough to vote!")

print(f"") # Empty print statement

## If Elif Else Statements:
print(f"IF ELIF ELSE STATEMENTS:")
age = 18
if age < 12:
	print(f"You're a child!")
elif age < 18:
	print(f"You're a teenager!")
elif age < 65:
	print(f"You're an adult!")
else:
	print(f"You're a senior citizen!")

print(f"") # Empty print statement

## Nested If Statements:
integer_variable = 10 # Integer
if integer_variable > 0:
	print(f"x is greater than 0")
	if integer_variable % 2 == 0:
		print(f"x is even")
	else:
		print(f"x is odd")
else:
	print(f"x is less or equal to 0")
	