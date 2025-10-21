# 📦 Installation Guide

Complete step-by-step installation instructions for the Text-to-Speech application.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: 3.8 or higher
- **Node.js**: 14.0 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 2GB free space
- **Internet**: Required for initial setup

### Software Prerequisites

#### 1. Python Installation

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run installer
3. **Important**: Check "Add Python to PATH"
4. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

**macOS:**
```bash
# Using Homebrew
brew install python@3.10

# Verify
python3 --version
pip3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

#### 2. Node.js Installation

**Windows/macOS:**
1. Download from [nodejs.org](https://nodejs.org/)
2. Run installer
3. Verify installation:
   ```bash
   node --version
   npm --version
   ```

**Linux (Ubuntu/Debian):**
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify
node --version
npm --version
```

## Installation Methods

### Method 1: Automated Setup (Recommended)

This is the easiest way to get started.

**Windows:**
1. Open Command Prompt or PowerShell
2. Navigate to project directory:
   ```cmd
   cd path\to\text-to-speech
   ```
3. Run setup script:
   ```cmd
   setup.bat
   ```

**Linux/macOS:**
1. Open Terminal
2. Navigate to project directory:
   ```bash
   cd path/to/text-to-speech
   ```
3. Make script executable and run:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

The script will:
- Create Python virtual environment
- Install all Python dependencies
- Install all Node.js dependencies
- Create necessary directories

### Method 2: Manual Installation

For more control over the installation process.

#### Step 1: Clone or Download Project

```bash
# If using Git
git clone <repository-url>
cd text-to-speech

# Or download and extract ZIP
cd text-to-speech
```

#### Step 2: Backend Setup

**Create Virtual Environment:**

```bash
# Windows
python -m venv venv

# Linux/macOS
python3 -m venv venv
```

**Activate Virtual Environment:**

```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux/macOS
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

**Install Python Dependencies:**

```bash
# Upgrade pip first
pip install --upgrade pip

# Install dependencies
pip install -r backend_requirements.txt
```

This will install:
- Flask and flask-cors (Web framework)
- pyttsx3 (Text-to-speech engine)
- All required audio processing libraries

**Note**: Installation may take 5-10 minutes depending on your internet speed.

#### Step 3: Frontend Setup

**Install Node.js Dependencies:**

```bash
npm install
```

This will install:
- React and ReactDOM
- Axios (HTTP client)
- Development tools
- All required build dependencies

## Verification

### Verify Backend Installation

1. Activate virtual environment (if not already active)
2. Start Flask server:
   ```bash
   python app.py
   ```

You should see:
```
INFO:__main__:Initializing TTS service...
INFO:tts_service:Initializing pyttsx3 TTS engine
INFO:tts_service:Found X voices available
INFO:tts_service:TTS engine loaded successfully
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

3. Press `Ctrl+C` to stop

### Verify Frontend Installation

1. Start development server:
   ```bash
   npm start
   ```

2. Browser should automatically open at `http://localhost:3000`
3. You should see the Text-to-Speech interface
4. Press `Ctrl+C` to stop

## Troubleshooting Installation Issues

### Python Issues

**Problem**: `python: command not found`
- **Solution**: Python not in PATH. Reinstall Python with "Add to PATH" option

**Problem**: `pip: command not found`
- **Solution**:
  ```bash
  python -m ensurepip --upgrade
  ```

**Problem**: Virtual environment activation fails on Windows PowerShell
- **Solution**: Run PowerShell as Administrator:
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```

**Problem**: Package installation fails with permission errors
- **Solution**:
  - Don't use `sudo` with virtual environment
  - Ensure virtual environment is activated
  - Try: `pip install --user -r backend_requirements.txt`

### Node.js Issues

**Problem**: `npm install` fails with EACCES errors
- **Solution** (Linux/macOS):
  ```bash
  sudo chown -R $USER:$(id -gn $USER) ~/.npm
  sudo chown -R $USER:$(id -gn $USER) ~/.config
  ```

**Problem**: `npm install` fails with network errors
- **Solution**:
  ```bash
  npm config set registry https://registry.npmjs.org/
  npm cache clean --force
  npm install
  ```

**Problem**: Port 3000 already in use
- **Solution**: Kill process or use different port:
  ```bash
  # Windows
  netstat -ano | findstr :3000
  taskkill /PID <PID> /F

  # Linux/macOS
  lsof -ti:3000 | xargs kill -9
  ```

### pyttsx3 Issues

**Problem**: `pyttsx3.init()` fails on Windows
- **Solution**: Install/repair Windows Speech API:
  - Open Windows Settings
  - Go to Time & Language > Speech
  - Ensure speech is enabled

**Problem**: No voices available
- **Solution** (Windows):
  - Open Settings > Time & Language > Speech
  - Download additional languages/voices
  - Restart application

**Problem**: `pyttsx3` fails on Linux
- **Solution**: Install espeak:
  ```bash
  sudo apt-get install espeak espeak-data libespeak-dev
  ```

**Problem**: `pyttsx3` fails on macOS
- **Solution**: macOS has built-in TTS. Ensure you have:
  - System Preferences > Accessibility > Speech enabled
  - At least one system voice installed

### General Issues

**Problem**: Port 5000 already in use
- **Solution**: Change port in `config.py`:
  ```python
  PORT = 5001  # Use different port
  ```

**Problem**: Out of disk space during installation
- **Solution**:
  - Free up at least 2GB disk space
  - Clear pip cache: `pip cache purge`
  - Clear npm cache: `npm cache clean --force`

## Installing Additional Language Voices

### Windows

1. Open **Settings** > **Time & Language** > **Language**
2. Click **Add a language**
3. Select desired language (e.g., Spanish, French, Hindi)
4. Click **Next** and **Install**
5. Go to **Speech** settings
6. Download voices for installed languages

### macOS

1. Open **System Preferences** > **Accessibility** > **Spoken Content**
2. Click **System Voice** dropdown
3. Click **Customize**
4. Download additional voices

### Linux

```bash
# For espeak (basic voices)
sudo apt-get install espeak-data

# For better quality voices (festival)
sudo apt-get install festival festival-dev
```

## Post-Installation

After successful installation:

1. Read [QUICKSTART.md](QUICKSTART.md) to run the application
2. Read [README.md](README.md) for full documentation
3. Test with example texts in different languages

## Uninstallation

### Remove Python Environment

```bash
# Deactivate first
deactivate

# Remove virtual environment
# Windows
rmdir /s venv

# Linux/macOS
rm -rf venv
```

### Remove Node Modules

```bash
# Windows
rmdir /s node_modules

# Linux/macOS
rm -rf node_modules
```

### Remove Generated Files

```bash
# Windows
rmdir /s generated_audio build

# Linux/macOS
rm -rf generated_audio build
```

## Getting Help

If you encounter issues not covered here:

1. Check the [Troubleshooting](#troubleshooting-installation-issues) section above
2. Review error messages carefully
3. Search for similar issues online
4. Open an issue on the repository with:
   - Your OS and version
   - Python and Node.js versions
   - Complete error message
   - Steps to reproduce

---

**Ready to run?** See [QUICKSTART.md](QUICKSTART.md) for next steps!
