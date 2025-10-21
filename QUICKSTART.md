# 🚀 Quick Start Guide

Get up and running with the Text-to-Speech application in under 5 minutes!

## Prerequisites

- ✅ Python 3.8+ installed ([Download](https://www.python.org/downloads/))
- ✅ Node.js 14+ installed ([Download](https://nodejs.org/))
- ✅ Internet connection (for downloading dependencies)

> **New to this?** See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

## Setup Steps

### 1. Automated Setup (Easiest Method)

Navigate to the project directory and run:

**Windows (Command Prompt):**
```cmd
cd path\to\text-to-speech
setup.bat
```

**Linux/macOS (Terminal):**
```bash
cd path/to/text-to-speech
chmod +x setup.sh
./setup.sh
```

**What the setup script does:**
- Creates Python virtual environment
- Installs all backend dependencies (Flask, pyttsx3, etc.)
- Installs all frontend dependencies (React, Axios, etc.)
- Creates necessary directories

⏱️ **Time**: 3-5 minutes (depending on internet speed)

### 2. Start Backend Server

Open **Terminal 1** (or Command Prompt):

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate

# Start Flask server
python app.py
```

**Expected output:**
```
INFO:__main__:Initializing TTS service...
INFO:tts_service:Initializing pyttsx3 TTS engine
INFO:tts_service:Found 2 voices available
INFO:tts_service:TTS engine loaded successfully
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

✅ **Backend is ready when you see**: `Running on http://127.0.0.1:5000`

### 3. Start Frontend Server

Open **Terminal 2** (keep Terminal 1 running):

```bash
npm start
```

**Expected behavior:**
- React development server starts
- Browser automatically opens at `http://localhost:3000`
- You see the Text-to-Speech interface

✅ **Frontend is ready when**: Browser opens with the app interface

## First Test

Try the application with these steps:

1. **Check Status**: Top-right should show "🟢 Server Online"
2. **Select Language**: Choose "English" from dropdown
3. **Use Example**: Click "English Example" button (auto-fills text)
4. **Generate**: Click "Generate Speech" button
5. **Listen**: Audio player appears - click play ▶️
6. **Download**: (Optional) Download the WAV file

🎉 **Success!** You should hear the generated speech.

## Testing Different Languages

### English
```
Hello, welcome to our text to speech service!
```

### Spanish (if voice installed)
```
Hola, bienvenido a nuestro servicio de texto a voz.
```

### French (if voice installed)
```
Bonjour, bienvenue dans notre service de synthèse vocale.
```

> **Note**: Language support depends on voices installed on your system. See [INSTALLATION.md](INSTALLATION.md#installing-additional-language-voices) to add more languages.

## Common Issues & Quick Fixes

### ❌ Backend won't start

**Problem**: `ModuleNotFoundError: No module named 'flask'`
```bash
# Make sure virtual environment is activated (you should see (venv) in prompt)
# Windows:
venv\Scripts\activate

# Then install dependencies:
pip install -r backend_requirements.txt
```

**Problem**: Port 5000 already in use
```bash
# Windows: Find and kill process
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/macOS: Kill process
lsof -ti:5000 | xargs kill -9
```

### ❌ Frontend shows "Server Offline"

**Fix**:
1. Check Terminal 1 - is Flask running?
2. Visit `http://localhost:5000/api/health` in browser
3. If you see JSON response, backend is working
4. Refresh frontend (`http://localhost:3000`)

### ❌ Audio generation hangs

**Fix**:
1. Stop Flask server (Ctrl+C)
2. Restart: `python app.py`
3. Try again (each request uses fresh TTS engine)

### ❌ No voices available

**Windows**:
- Open Settings > Time & Language > Speech
- Ensure speech is enabled
- Download additional voices if needed

**Linux**:
```bash
sudo apt-get install espeak espeak-data
```

**macOS**:
- System Preferences > Accessibility > Speech
- Install additional voices

## Stopping the Application

### Stop Servers Properly

**Terminal 1** (Backend):
```
Press Ctrl+C
```

**Terminal 2** (Frontend):
```
Press Ctrl+C
```

### Deactivate Virtual Environment

```bash
deactivate
```

## Next Steps

### Learn More
- 📖 [README.md](README.md) - Full documentation
- 📦 [INSTALLATION.md](INSTALLATION.md) - Detailed setup guide
- 🔧 [config.py](config.py) - Configuration options

### Customize
- Change speech rate/volume in `config.py`
- Modify UI colors in `src/App.css`
- Add API endpoints in `app.py`

### Deploy
See [README.md - Deployment](README.md#-deployment) for production deployment guide

## Need Help?

**Still having issues?**
1. Check [INSTALLATION.md - Troubleshooting](INSTALLATION.md#troubleshooting-installation-issues)
2. Review console output for specific errors
3. Ensure prerequisites are correctly installed
4. Try manual installation method

**Everything working?** 🎉
- Try different languages
- Experiment with longer texts
- Download audio files
- Check out the API endpoints

---

**Ready for Production?** See [README.md](README.md#-deployment) for deployment guidelines.

**Happy Coding! 🚀**
