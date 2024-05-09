""" color.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

from pathlib import Path
from typing  import Callable

from src.collections.argsiterable import ArgsIterable


class Color(ArgsIterable):
	""" Base class for all color formats
	"""
	MODES            : set[str] = {'hsl', 'hex', 'rgb'}
	EXTS             : set[str] = {'png'}
	DEFAULT_EXT      : str      = 'png'


	def __init__(self, *args : list, **kwargs : dict) -> None:
		""" Initializer method for Color base class

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		if type(self) is Color:
			raise NotImplementedError()

		super().__init__(*args, **kwargs)


	def updatePath(self, dir : str = None, filename : str = None, ext : str = None) -> None:
		""" Define the path, filename, and extension of the pixel file to be saved

		:param dir:       The directory to which the pixel data shall be saved, defaults to DEFAULT_SAVE_DIR
		:type dir:        str, optional
		:param filename:  The name of the file, without path and file extension; defaults to None, which means a hex value
		:type filename:   str, optional
		:param ext:       The file extention; defaults to None, which adds '.png'
		:type ext:        str, optional

		:raises ValueError: Raises if the extension is not supported
		"""
		from .hex import Hex

		_hex      : Hex = self     if self is Hex else self.toHex()
		_dir      : str = dir      if dir         else environ.get(DEFAULT_SAVE_DIR)
		_filename : str = filename if filename    else f'{_hex.red:02x}{_hex.green:02x}{_hex.blue:02x}'
		_ext      : str = ext      if ext         else self.DEFAULT_EXT

		if _ext not in self.EXTS:
			raise ValueError()

		self._dir      : str = _dir
		self._filename : str = _filename
		self._ext      : str = _ext


	@property
	def pathFilename(self) -> Path:
		""" Property defining the complete filepath for the pixel file

		:return: The complete filepath: directory path, filename, and extension
		:rtype: str
		"""
		pathFilename    : Path = Path(self._dir) / self._filename
		pathFilenameExt : Path = Path(f"{pathFilename}.{self._ext}")

		return pathFilenameExt


	def __format__(self, mode : str = 'hex') -> str:
		""" Internal method for displaying the color as a formatted string

		:param mode:  The type of format for the return value, of 'hsl', 'hex', or 'rgb'; defaults to 'hex'
		:type mode:   str

		:raises NotImplementedError:  Raises when called directly, rather than by a child class object
		:raises ValueError:           Raises when the mode parameter is invalid

		:return:  The color values as a custom-formatted string
		:rtype:   str
		"""
		from . import HSL, Hex, RGB

		cls : HSL | Hex | RGB | Color = type(self)

		if cls is Color:
			raise NotImplementedError('Unable to determine color type.')

		if mode not in {'', *self.MODES}:
			raise ValueError(f'Unable to determine color mode.\nExpected: {self.MODES}\nGot: {mode}')

		values : str = ''

		if mode in self.MODES:
			modeConvert : dict[str, Callable] = {
				'hsl' : cls.toHSL,
				'hex' : cls.toHex,
				'rgb' : cls.toRGB,
			}

			color : cls = modeConvert[mode](self)
			values      = str(color)

		return values


	def exportImage(self, dir : str = None, filename : str = None, ext : str = None) -> None:
		""" Save the image to the filesystem via helper methods

		:param dir:       The directory to which the pixel data shall be saved, defaults to DEFAULT_SAVE_DIR
		:type dir:        str, optional
		:param filename:  The name of the file, without path and file extension; defaults to None, which means a hex value
		:type filename:   str, optional
		:param ext:       The file extention; defaults to None, which adds '.png'
		:type ext:        str, optional

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		if type(self) is Color:
			raise NotImplementedError()

		self.updatePath(dir, filename, ext)

		modeToExportMethod : dict[str, Callable] = {
			'png' : self.toPNG,
			# TODO: more export methods go here (as needed)
		}

		exportMethod : Callable = modeToExportMethod[self._ext]

		exportMethod()


	def toPNG(self) -> None:
		""" Export as a PNG file

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		if type(self) is Color:
			raise NotImplementedError()

		from png import Writer

		rgb      : Color            = self.toRGB()
		image    : list[tuple[int]] = [rgb]
		filepath : str              = self.pathFilename
		img      : Path             = Path(filepath)
		imgDir   : Path             = Path(self.DEFAULT_SAVE_DIR)

		if not (img.exists() or imgDir.exists()):
			from os import mkdir

			mkdir(self.DEFAULT_SAVE_DIR)
			# self.log.info('Saving pixel image to:', filepath)

			writer : Writer = Writer(1, 1, greyscale=False)

			with open(filepath, 'wb+') as file:
				writer.write(file, image)


	def toHex(self) -> None:
		""" Conversion method to a Hex object (to be defined by the child class)

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		raise NotImplementedError()


	def toHSL(self) -> None:
		""" Conversion method to a HSL object (to be defined by the child class)

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		raise NotImplementedError()


	def toRGB(self) -> None:
		""" Conversion method to a RGB object (to be defined by the child class)

		:raises NotImplementedError: Raises when called directly, rather than by a child class object
		"""
		raise NotImplementedError()

