# Name of the virtual environment directory
VENV := venv
# Python command to use
PYTHON := python3

.PHONY: all venv dependencies pytest verbose everything fast_mark slow_mark

all: venv dependencies

venv: $(VENV)/bin/activate

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	touch $(VENV)/bin/activate

dependencies:
	$(VENV)/bin/pip install -r requirements.txt

pytest:
	$(VENV)/bin/pytest ./test_calculator.py

verbose:
	$(VENV)/bin/pytest -v ./test_calculator.py

everything:
	$(VENV)/bin/pytest -v

fast_mark:
	$(VENV)/bin/pytest -v -m fast

slow_mark:
	$(VENV)/bin/pytest -v -m slow
