from dataclasses import dataclass

@dataclass()
class Product:
	id: int
	name: str
	price: float
	quantity: int

	def increase_quantity(self, quantity: int):
		self.quantity += quantity

	def decrease_quantity(self, quantity: int):
		self.quantity -= quantity
