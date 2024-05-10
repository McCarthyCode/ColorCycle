""" hex.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from . import BaseRGB


class Hex(BaseRGB):
	""" Color child class where values are saved as RGB and accessed as hex vakues
	"""

	def __init__(self, red : int, green : int, blue : int, **kwargs : dict) -> None:
		""" Initialization method

		Takes positional and keyword arguments and stores them as instance variables
		"""
		super().__init__(red, green, blue, **kwargs)


	def toHex(self) -> 'Hex':
		""" Conversion method required by parent class Color (useful when context is not known)
		"""
		return self


	def toHSL(self) -> 'HSL':
		""" Convert Hex object to use hue, saturation, and luminence values
		"""
		return super().toHSL()


	def toRGB(self) -> 'RGB':
		""" Convert Hex object to use red, green, and blue values
		"""
		from . import RGB

		return RGB(*self)


	def __str__(self) -> str:
		""" Return color values as a hexadecimal string
		"""
		return f'{self.red:02x}{self.green:02x}{self.blue:02x}'


