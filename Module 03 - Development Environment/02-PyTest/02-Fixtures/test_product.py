# Fixtures:
# Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
# Advantage of Pytest Fixtures: Reusability, Reduce lines of code, Easy to maintain

from product import Product
import pytest

@pytest.fixture
def product():
	return Product(1, 'Product 1', 10.0, 10)

def test_product_constructor(product):
	assert product.id == 1
	assert product.name == 'Product 1'
	assert product.price == 10.0
	assert product.quantity == 10

def test_product_increase_quantity(product):
	product.increase_quantity(5)
	assert product.quantity == 15

def test_product_decrease_quantity(product):
	product.decrease_quantity(5)
	assert product.quantity == 5
	