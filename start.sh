#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status
set -u  # Treat unset variables as an error

TERM=xterm
export DISPLAY=:0

# Activate virtual environment
if [ -f "my-venv/bin/activate" ]; then
    source my-venv/bin/activate
else
    echo "Error: Virtual environment not found at my-venv/bin/activate"
    exit 1
fi

# Put your commands that need the virtual environment here
# For example:
python Bot.py
