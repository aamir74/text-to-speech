#!/usr/bin/env bash
set -e

# Install system dependencies at runtime
apt-get update && apt-get install -y espeak-ng

# Upgrade pip (optional)
pip install --upgrade pip

# Install Python dependencies
pip install -r backend_requirements.txt

# Verify installation
which espeak-ng || echo "espeak-ng not found!"
espeak-ng --version || echo "espeak-ng not working!"
