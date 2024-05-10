""" client.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

# Standard libraries
from datetime import datetime, time
from pathlib  import Path

# Project code
from src.color import RGB, HSL



class Client:
	""" Runtime logic definitions for terminal application
	"""

	def __init__(self):
		""" Initialization method for client
		"""
		from signal import signal, SIGINT

		# Cancel running on keyboard interrupt
		signal(SIGINT, self.interruptHandler)


	def createImage(self, pixel : RGB, filepath : Path = None) -> None:
		""" Create a single-pixel image in PNG format

		:param pixel:    The RGB values of the pixel to be used as a background
		:param filepath: The complete path (including directory and filename) of the output file. If no filepath is specified, the location used is the '/tmp' directory and the image is named after its hex values with a PNG extention.
		"""
		from PIL import Image

		filepath : Path  = filepath or Path(f'/tmp/{pixel:hex}.png')
		image    : Image = Image.new("RGB", (1, 1), pixel.args)

		if not filepath.exists():
			image.save(filepath)


	def setWallpaperDarwin(self, pixel : RGB) -> int:
		""" Set the wallpaper via applescript

		:param pixel:      The RGB values of the pixel to be used as a background

		:return: The exit status of the `osascript` command
		"""
		from os import system

		applescript = f'''
			tell application "System Events"
				tell every desktop
					set picture to "/tmp/{pixel:hex}.png"
				end tell
			end tell
		'''.strip()

		return system(f"osascript -e '{applescript}'")


	def update(self, pixel : RGB, lastPixel : RGB = None) -> None:
		""" Create image if it does not exist, and set the wallpaper tio that image

		:param pixel:     The RGB values of the pixel to be used as a background
		:param lastPixel: The RGB values previously used (for skipping repeat logs)
		"""
		lastPixel = lastPixel or RGB(0, 0, 0)

		if f'{pixel:hex}' != f'{lastPixel:hex}':
			print(f'[{datetime.now()}] #{pixel:hex}')

		self.createImage(pixel)
		self.setWallpaperDarwin(pixel)


	def interruptHandler(self, sig, frame) -> None:
		""" Handle a keyboard interrupt (^C) to break main program execution
		"""
		# Log on a new line
		print('\nInterrupt signal received')

		# Allow the main execution loop to cleanly exit
		self.running = False


	def run(self) -> None:
		""" Main program execution loop
		"""
		from time import sleep

		from src.colorcycle import Time

		previousRGB  : RGB  = None
		self.running : bool = True

		while self.running:
			currentTime : time = datetime.now().time()
			timeObj     : Time = Time(currentTime.hour, currentTime.minute, currentTime.second)
			hsl         : HSL  = timeObj.toHSL()
			rgb         : RGB  = hsl.toRGB()

			self.update(rgb, previousRGB)

			previousRGB = rgb

			sleep(1)

