""" argsiterable.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from collections.abc import Iterable


class ArgsIterable(Iterable):
	""" Abstract base collection class that stores positional and keyword arguments
	"""

	def __init__(self, *args : list, **kwargs : dict) -> None:
		""" Initialization method

		Takes positional and keyword arguments and stores them as instance variables
		"""
		self.args   = args
		self.kwargs = kwargs


	def __iter__(self) -> ...:
		""" Iterator method

		Describes the object as an iterator, through self.args

		:yield: The instance's positional arguments stored at initialization
		:rtype: Iterator[...]
		"""
		yield from self.args

