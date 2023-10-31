#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
  echo "Python is already installed."
else
  echo "Python is not installed. Please install Python 3."
  exit 1
fi

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

pip install -r requirements.txt

echo "Virtual environment created and requirements installed."


# run this script with -> source project_setup.sh
