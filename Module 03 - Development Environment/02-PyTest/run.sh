#!/bin/bash

# Run:
# chmod +x ./run.sh
# ./run.sh

# Install dependencies/requirments
pip install -r requirements.txt

# Run specific test
# pytest ./file_name.py

# Run all tests -> Works only if the file name starts with test_ or ends with _test
# pytest

# Pytest -v -> Command to run the test in verbose mode
pytest -v
