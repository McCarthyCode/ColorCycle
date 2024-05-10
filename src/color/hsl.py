""" hsl.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from . import Color


class HSL(Color):
	""" Color child class where values are saved and accessed as HSL vakues
	"""

	def __init__(self, hue : float, saturation : float, luminescence : float, **kwargs : dict) -> None:
		""" Initialization method

		Takes positional and keyword arguments and stores them as instance variables
		"""
		super().__init__(hue, saturation, luminescence, **kwargs)


	def __str__(self) -> str:
		""" Return hue, saturation, and luminescence color values as a string
		"""
		return f'hsl({self.hue:.1f}, {self.saturation:.3f}, {self.luminescence:.3f})'


	@property
	def hue(self) -> float:
		""" Property describing the hue value as a float
		"""
		return self.args[0]


	@property
	def saturation(self) -> float:
		""" Property describing the saturation value as a float
		"""
		return self.args[1]


	@property
	def luminescence(self) -> float:
		""" Property describing the luminescence value as a float
		"""
		return self.args[2]


	@classmethod
	def hslToRGB(cls, hue : float, saturation : float, luminescence : float) -> 'RGB':
		""" Class method to convert HSL values to RGB
		"""
		from . import RGB

		x : float = saturation * (1 - abs(2 * luminescence - 1))
		y : float = 0xff * (luminescence - 0.5 * x)
		z : float = x * (1 - abs((hue / 60) % 2 - 1))

		x = 0xff * x + y
		z = 0xff * z + y

		if hue < 60.0 and hue >= 0.0:
			rgb = (x, z, y)
		elif hue < 120.0 and hue >= 60.0:
			rgb = (z, x, y)
		elif hue < 180.0 and hue >= 120.0:
			rgb = (y, x, z)
		elif hue < 240.0 and hue >= 180.0:
			rgb = (y, z, x)
		elif hue < 300.0 and hue >= 240.0:
			rgb = (z, y, x)
		elif hue < 360.0 and hue >= 300.0:
			rgb = (x, y, z)
		else:
			raise ValueError(hue)

		return RGB(*map(int, rgb))


	def toHex(self) -> 'Hex':
		""" Convert Hex object to use hue, saturation, and luminence values
		"""
		from . import Hex, RGB

		rgb : RGB = HSL.hslToRGB(*self)
		hex : Hex = Hex(*rgb)

		return hex


	def toHSL(self) -> 'HSL':
		""" Conversion method required by parent class Color (useful when context is not known)
		"""
		return self


	def toRGB(self) -> 'RGB':
		""" Convert HSL object to use red, green, and blue values
		"""
		return HSL.hslToRGB(*self)

