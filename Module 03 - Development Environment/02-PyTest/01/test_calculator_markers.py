# PyTest -> clear; pytest ./main.py
# PyTest is a testing framework that allows us to write test codes using python.
# The type of tests it supports are: Unit, Functional and Integration.

# Test Calculator functions
from calculator import *

# Import PyTest Library
import pytest

# Test Calculator functions
@pytest.mark.fast
def test_sum():
	assert sum(3, 4) == 7

@pytest.mark.fast
def test_subtraction():
	assert subtraction(3, 4) == -1

@pytest.mark.slow
def test_multiplication():
	assert multiplication(3, 4) == 12

@pytest.mark.slow
def test_division():
	assert division(3, 4) == 0.75