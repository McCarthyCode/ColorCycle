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
	""" TODO
	"""

	def __init__(self):
		""" TODO
		"""
		from signal import signal, SIGINT

		signal(SIGINT, self.interrupt_handler)


	def create_image(self, pixel : RGB, filepath : Path = None) -> Path:
		""" TODO
		"""
		from PIL import Image

		filepath : Path  = filepath or Path(f'/tmp/{pixel:hex}.png')
		image    : Image = Image.new("RGB", (1, 1), pixel.args)

		if not filepath.exists():
			image.save(filepath)

		return filepath


	def set_wallpaper_darwin(self, pixel : RGB) -> int:
		""" TODO
		"""
		from os import system

		applescript = f'''
			tell application "System Events"
				tell every desktop
					set picture to "/tmp/{pixel:hex}.png"
				end tell
			end tell
		'''.strip()
		exit_status = system(f"osascript -e '{applescript}'")

		return exit_status


	def update(self, pixel : RGB, last_pixel : RGB = None) -> RGB:
		""" TODO
		"""
		last_pixel = last_pixel or RGB(0, 0, 0)

		if f'{pixel:hex}' != f'{last_pixel:hex}':
			print(f'[{datetime.now()}] #{pixel:hex}')
			self.create_image(pixel)

		self.set_wallpaper_darwin(pixel)

		return pixel


	def interrupt_handler(self, sig, frame):
		""" TODO
		"""
		# Log on a new line
		print('\nInterrupt signal received')

		# Allow the main execution loop to cleanly exit
		self.running = False


	def run(self):
		""" TODO
		"""
		from time import sleep

		from src.colorcycle import Time

		previous_rgb : RGB  = None
		self.running : bool = True

		while self.running:
			current_time : time = datetime.now().time()
			time_obj     : Time = Time(current_time.hour, current_time.minute, current_time.second)
			hsl          : HSL  = time_obj.toHSL()
			rgb          : RGB  = hsl.toRGB()

			previous_rgb = self.update(rgb, previous_rgb)

			if self.running:
				sleep(1)

