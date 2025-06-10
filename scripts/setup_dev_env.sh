#!/bin/bash
set -e

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Initialize database
flask db upgrade

echo "Development environment setup complete!"
