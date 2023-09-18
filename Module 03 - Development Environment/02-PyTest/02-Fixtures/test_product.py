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
	