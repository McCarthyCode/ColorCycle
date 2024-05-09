""" main.py

Copyright (c) Matt McCarthy 2024
See LICENSE for details.
"""

if __name__ == "__main__":
	from colorcycle import Client

	# Initialize client application
	client : Client = Client()

	# Run the client app
	client.run()

	# Log when program has finished executing
	print('Exited cleanly')

