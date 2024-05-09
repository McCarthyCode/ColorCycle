""" time.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from datetime import datetime

from src.collections.argsiterable import ArgsIterable
from src.color.hsl                import HSL


class Time(ArgsIterable):
	""" A time object that is convertable to a hue value or an image
	"""

	def __init__(self, hour : int, minute : int, second: int = 0):
		""" The time, in hours, minutes, and (optionally) seconds

		:param hour:   The hour of the day
		:param minute: The minute of the hour
		:param second: [OPT] The second of the minute
		"""

		super().__init__(hour, minute, second)


	def __str__(self) -> str:
		""" The time as a formatted string

		:return: A string formatted as <HH:MM:SS>
		"""

		return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'


	@property
	def hour(self) -> int:
		""" Property definition of the object's first internal argument: hour

		:return: The hour value of the time object
		"""

		return self.args[0]


	@property
	def minute(self) -> int:
		""" Property definition of the object's second internal argument: minute

		:return: The minute value of the time object
		"""

		return self.args[1]


	@property
	def second(self) -> int:
		""" Property definition of the object's third internal argument: second

		:return: The second value of the time object
		"""

		return self.args[2]


	def toHue(self, startHue : float = 0.0, reverse : bool = False, spanMinutes : float = 60) -> float:
		""" Convert the time to a hue value

		:return: A hue value greater than or equal to 0 and less than 360
		"""

		minute, second = self.minute, self.second

		seconds = (minute * 60) + second
		hue     = float(seconds) * 360.0 / (60 * spanMinutes)
		hue     = (hue + startHue) % 360.0

		if reverse:
			hue = (360.0 - hue) % 360.0

		return hue


	def toHSL(self, saturation : float = 0.25, luminescence : float = 0.5, startHue : float = 0.0, reverse : bool = False, spanMinutes : float = 60) -> HSL:
		""" Convert time so HUE/SAT/LUM value

		:param saturation:    The saturation of the color to be generated
		:param luminescence:  The luminescence of the color to be generated
		:param startHue:      The minute of the day
		:param reverse:       True if colors are to rotate in reverse on the spectrum

		:return: The HSL-formatted image data
		"""

		hue : float = self.toHue(startHue, reverse, spanMinutes)
		hsl : HSL   = HSL(hue, saturation, luminescence)

		return hsl


	@classmethod
	def getTime(cls) -> 'Time':
		""" Retrieve the time from datetime.now() and create an image-convertable object

		:return: The image-convertible time object
		"""

		now = datetime.now()

		return Time(now.hour, now.minute, now.second)

