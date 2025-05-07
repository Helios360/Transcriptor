#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status
set -u  # Treat unset variables as an error
setxkbmap us
TERM=xterm
export DISPLAY=:0

# Activate virtual environment
if [ -f "my-venv/bin/activate" ]; then
    source my-venv/bin/activate
else
    echo "Error: Virtual environment not found at my-venv/bin/activate"
    exit 1
fi

python Bot.py

setxkbmap fr
echo "Keyboard back into french azerty"
