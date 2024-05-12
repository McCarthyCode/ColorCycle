# Makefile

# Copyright (c) Matt McCarthy 2024
# See LICENSE for details.


NULL=2>/dev/null
PIP=.venv/bin/pip
PYINSTALLER=.venv/bin/pyinstaller


colorcycle :: dependencies
	$(PYINSTALLER) -F src/main.py -n colorcycle

clean ::
	find . -type d -name '__pycache__' -exec rm -rf {} $(NULL) \;
	rm -rf build colorcycle.spec .venv

clean-dist :: clean
	rm -rf dist

run :: colorcycle
	dist/colorcycle

dependencies :: .venv
	$(PIP) install -r requirements.txt

.venv ::
	virtualenv .venv

