#!/bin/bash
# Text-to-Speech Application Setup Script for Linux/Mac
# This script sets up both backend and frontend dependencies

echo "========================================"
echo "Text-to-Speech Application Setup"
echo "========================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python installation
echo "[1/6] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}ERROR: Python 3 is not installed${NC}"
    echo "Please install Python 3.8 or higher"
    exit 1
fi
echo -e "${GREEN}Python is installed$(NC)"
python3 --version
echo ""

# Check Node.js installation
echo "[2/6] Checking Node.js installation..."
if ! command -v node &> /dev/null; then
    echo -e "${RED}ERROR: Node.js is not installed${NC}"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi
echo -e "${GREEN}Node.js is installed${NC}"
node --version
echo ""

# Create virtual environment
echo "[3/6] Creating Python virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}Virtual environment created${NC}"
else
    echo -e "${YELLOW}Virtual environment already exists${NC}"
fi
echo ""

# Activate virtual environment and install Python dependencies
echo "[4/6] Installing Python backend dependencies..."
echo -e "${YELLOW}This may take several minutes as it downloads ML models...${NC}"
source venv/bin/activate
pip install --upgrade pip
pip install -r backend_requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Failed to install Python dependencies${NC}"
    exit 1
fi
echo -e "${GREEN}Backend dependencies installed successfully${NC}"
echo ""

# Install Node.js dependencies
echo "[5/6] Installing Node.js frontend dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo -e "${RED}ERROR: Failed to install Node.js dependencies${NC}"
    exit 1
fi
echo -e "${GREEN}Frontend dependencies installed successfully${NC}"
echo ""

# Create audio output directory
echo "[6/6] Creating directories..."
if [ ! -d "generated_audio" ]; then
    mkdir -p generated_audio
    touch generated_audio/.gitkeep
    echo -e "${GREEN}Created generated_audio directory${NC}"
fi
echo ""

echo "========================================"
echo -e "${GREEN}Setup completed successfully!${NC}"
echo "========================================"
echo ""
echo "To start the application:"
echo ""
echo "1. Start the backend (in Terminal 1):"
echo "   source venv/bin/activate"
echo "   python app.py"
echo ""
echo "2. Start the frontend (in Terminal 2):"
echo "   npm start"
echo ""
echo "3. Open your browser to http://localhost:3000"
echo ""
echo "========================================"
