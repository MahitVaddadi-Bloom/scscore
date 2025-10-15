#!/bin/bash

# SCScore Installation Script
# This script sets up the SCScore package for installation with uv

echo "Setting up SCScore package..."

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed. Please install uv first:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
uv venv

# Activate virtual environment and install package
echo "Installing SCScore package..."
source .venv/bin/activate
uv pip install -e .

echo ""
echo "Installation complete! To use SCScore:"
echo "1. Activate the environment: source .venv/bin/activate"
echo "2. Use in Python: from scscore import SCScorer, get_score"
echo "3. Use CLI: scscore 'CCO' 'CCC'"
echo ""
echo "Test the installation by running: python -c \"from scscore import get_score; print(get_score('CCO'))\""