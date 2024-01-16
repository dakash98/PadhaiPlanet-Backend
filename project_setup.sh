#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
  echo "Python is already installed."
else
  echo "Python is not installed. Please install Python 3."
  exit 1
fi

if [ -d "venv" ]; then
    echo "Virtual environment 'venv' exists in the current directory."

    # Path to your requirements.txt file
    requirements_file="requirements.txt"

    # Loop through each line in the requirements.txt file
    while IFS= read -r line; do
        # Check if the package is installed in the virtual environment

        if ! pip show "$line" > /dev/null 2>&1; then
            echo "Package '$line' is missing."
            pip install $line
        fi
    done < "$requirements_file"

else
    echo "No virtual environment found in the current directory."
    echo "Creating a virtual environment"
    
    python3 -m venv venv
    echo "Virtual environment created"

    echo "Installing requirements from requirements.txt file."
    pip3 install -r requirements.txt
    echo "Requirements installed successfully"
fi

# Activate the virtual environment
echo "--- Activating Virtual Environment ---"
source venv/bin/activate

# pip install -r requirements.txt

echo "--------------------- Virtual environment activated -----------------------"


echo "Running Server"
python3 run.py
