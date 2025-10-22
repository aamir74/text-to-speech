#!/usr/bin/env bash
set -o errexit

# Install system dependencies
apt-get update && apt-get install -y espeak-ng

# Then install Python deps
pip install -r backend_requirements.txt
