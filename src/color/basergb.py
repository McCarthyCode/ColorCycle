""" basergb.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from .color import Color


class BaseRGB(Color):
	""" Shared base class of RGB and Hex. Inherits from Color
	"""
	def __init__(self, red : int, green : int, blue : int, **kwargs : dict) -> None:
		bitMask : int                  = 0xff
		args    : tuple[int, int, int] = (red, green, blue)
		args                           = tuple(map(lambda x: int(x) & bitMask, args))

		super().__init__(*args, **kwargs)

	@property
	def red(self) -> int:
		""" Property containing the red byte value (within range 0-255)
		"""
		return int(self.args[0])


	@property
	def green(self) -> int:
		""" Property containing the green byte value (within range 0-255)
		"""
		return int(self.args[1])


	@property
	def blue(self) -> int:
		""" Property containing the blue byte value (within range 0-255)
		"""
		return int(self.args[2])


	@classmethod
	def rgbToHSL(cls, red : int, green : int, blue : int) -> 'HSL':
		""" Calculate HSL values based on red, green, and blue values
		"""

		from math import acos

		from . import HSL

		maximum      : int   = max(red, green, blue)
		minimum      : int   = min(red, green, blue)
		difference   : int   = (maximum - minimum) // 0xff
		luminescence : float = (maximum + minimum) / 510
		saturation   : float = max(difference / (1 - abs(2 * luminescence - 1)), 0)
		numerator    : float = red - (green / 2) - (blue / 2)
		denominator  : float = (red ** 2 + green ** 2 + blue ** 2 - red * green - red * blue - green * blue) ** 0.5
		hue          : float = acos(numerator / denominator)
		hue                  = 360 - hue if blue > green else hue

		return HSL(hue, saturation, luminescence)


	def toHSL(self) -> 'HSL':
		""" Convert the object to an HSL object
		"""

		from . import HSL

		hsl : HSL = BaseRGB.rgbToHSL(*self.args)

		return hsl


	def __str__(self):
		""" Raise an error if not defined in child class
		"""
		raise NotImplementedError()

