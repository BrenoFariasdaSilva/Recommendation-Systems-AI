# Name of the virtual environment directory
VENV := venv
# Python command to use
PYTHON := python3

.PHONY: all venv dependencies pytest verbose everything

all: venv dependencies

venv: $(VENV)/bin/activate

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	touch $(VENV)/bin/activate

dependencies:
	$(VENV)/bin/pip install pytest

pytest:
	$(VENV)/bin/pytest ./test_product.py

verbose:
	$(VENV)/bin/pytest -v ./test_product.py

everything:
	$(VENV)/bin/pytest -v
