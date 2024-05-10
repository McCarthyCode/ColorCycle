""" rgb.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from . import BaseRGB


class RGB(BaseRGB):
	""" Color child class where values are saved and accessed as RGB vakues
	"""

	def __init__(self, red : int, green : int, blue : int, **kwargs : dict) -> None:
		""" Initialization method

		Takes positional and keyword arguments and stores them as instance variables
		"""
		super().__init__(red, green, blue, **kwargs)


	def toHex(self) -> 'Hex':
		""" Conversion method to represent values in hexadecimal
		"""
		from . import Hex

		return Hex(*self)


	def toHSL(self) -> 'HSL':
		""" Convert RGB object to use hue, saturation, and luminence values
		"""
		return super().toHSL()


	def toRGB(self) -> 'RGB':
		""" Conversion method required by parent class Color (useful when context is not known)
		"""
		return self


	def __str__(self):
		""" Return red, green, and blue color values as a string
		"""
		return f'rgb({self.red}, {self.green}, {self.blue})'

