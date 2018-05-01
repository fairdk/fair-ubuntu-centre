.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:  ## Displays this help text
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

dist:  ## Builds the distributable build/installscripts.tar.gz
	./build.sh

clean:  ## Removes files from build processes
	rm -rf build
	$(MAKE) -C docs clean

lint:  ## Checks that our docs are correctly written
	$(MAKE) -C docs linkcheck

docs: clean  ## Builds docs
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html
