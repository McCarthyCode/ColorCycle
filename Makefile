# Makefile

# Copyright (c) Matt McCarthy 2024
# See LICENSE for details.


PIP=.venv/bin/pip
PYINSTALLER=.venv/bin/pyinstaller


dist: dependencies
	$(PYINSTALLER) -F src/main.py -n colorcycle

clean:
	rm -rf .venv build dist colorcycle.spec
	find . -type d -name '__pycache__' -exec rm -rf {} \;

run: dist
	dist/colorcycle

dependencies: .venv
	$(PIP) install -r requirements.txt

.venv:
	virtualenv .venv

