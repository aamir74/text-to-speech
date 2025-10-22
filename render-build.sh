#!/usr/bin/env bash
set -o errexit

# Install system dependencies
apt-get update -y
apt-get install -y espeak-ng libespeak-ng1

# Upgrade pip (optional)
pip install --upgrade pip

# Then install Python deps
pip install -r backend_requirements.txt
