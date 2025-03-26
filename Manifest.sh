#!/bin/bash

echo "Removing __pycache__ and .pytest_cache directories..."

# Remove all __pycache__ directories recursively from the entire project
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove all .pytest_cache directories recursively from the entire project
find . -type d -name ".pytest_cache" -exec rm -rf {} +

echo "__pycache__ and .pytest_cache directories removed."

# Now run pytest
echo "Running pytest..."
pytest

