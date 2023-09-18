# PyTest -> clear; pytest ./main.py
# PyTest is a testing framework that allows us to write test codes using python.
# The type of tests it supports are: Unit, Functional and Integration.

# To create a test, we need to create a function that starts with the word test_.
# The function must contain at least one assert statement, which is used to compare the expected and actual results.

# Install PyTest
from calculator import *

# Test Calculator functions
def test_sum():
	assert sum(3, 4) == 7
	assert sum(4, 3) == 7

def test_subtraction():
	assert subtraction(3, 4) == -1
	assert subtraction(4, 3) == 1

def test_multiplication():
	assert multiplication(3, 4) == 12
	assert multiplication(4, 3) == 12

def test_division():
	assert division(3, 4) == 0.75
	assert division(3, 3) == 1.0
	assert division(3, 2) == 1.5
