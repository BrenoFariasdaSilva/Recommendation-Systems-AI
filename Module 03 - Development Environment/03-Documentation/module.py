"""Example of the use of docstrings in Python.

This is a multiline comment at module level.
It is used to describe the overall purpose of the module.
"""

class Example:
	"""Example class of the use of docstrings in this Python module."""

	def __init__(self, name: str) -> None:
		"""Constructor of the class.

		Args:
			name (str): Name of the example.
		"""
		self.name = name