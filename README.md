# 🎙️ Text to Speech - English Web Application

A modern, full-stack web application that converts English text to speech using system voices.

![Technology Stack](https://img.shields.io/badge/Frontend-React-61DAFB?style=flat&logo=react)
![Backend](https://img.shields.io/badge/Backend-Flask-000000?style=flat&logo=flask)
![TTS Engine](https://img.shields.io/badge/TTS-pyttsx3-4A90E2?style=flat)

## ✨ Features

### Core Features
- 🗣️ **English Text-to-Speech**: Converts English text to natural-sounding speech
- 🎙️ **System Voice Integration**: Uses pyttsx3 with system voices for text-to-speech conversion
- 🌐 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🎵 **Audio Player**: Interactive player with play/pause, seek, and volume controls
- 💾 **Download Audio**: Download generated speech as WAV files
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Fast & Lightweight**: No heavy AI models to download, uses system resources efficiently

### User Interface
- Modern gradient design with smooth animations
- Real-time server status indicator
- Character counter for text input
- Quick example buttons for testing
- Loading indicators and error messages
- Clean, intuitive user experience

### Technical Features
- RESTful API architecture
- Component-based React frontend
- Flask backend with CORS support
- Audio file management and cleanup
- Error handling and validation
- Production-ready code structure

## 🏗️ Technology Stack

### Frontend
- **React** 18.2.0 - Modern UI framework
- **Axios** 1.6.2 - HTTP client for API calls
- **Custom CSS** - Responsive styling with gradients

### Backend
- **Flask** 3.0.0 - Lightweight web framework
- **pyttsx3** 2.90 - Cross-platform text-to-speech engine
- **Flask-CORS** 4.0.0 - Cross-origin resource sharing

### Audio Processing
- **System TTS engines**: SAPI5 (Windows), NSSpeechSynthesizer (macOS), espeak (Linux)
- WAV format output
- Configurable speech rate and volume

## 📦 Installation

### Prerequisites
- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 14+** - [Download Node.js](https://nodejs.org/)
- **pip** - Python package installer (included with Python)
- **npm** - Node package manager (included with Node.js)
- **System TTS Support**:
  - Windows: Built-in SAPI5 (Windows Speech API)
  - macOS: Built-in NSSpeechSynthesizer
  - Linux: Install espeak (`sudo apt-get install espeak`)

> 📖 **Detailed instructions**: See [INSTALLATION.md](INSTALLATION.md) for step-by-step guide

### Quick Setup

#### Option 1: Automated Setup (Recommended)

**Windows:**
```cmd
setup.bat
```

**Linux/Mac:**
```bash
chmod +x setup.sh
./setup.sh
```

#### Option 2: Manual Setup

**1. Clone or download the project**
```bash
cd text-to-speech
```

**2. Install Python dependencies**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r backend_requirements.txt
```

**3. Install Node.js dependencies**
```bash
npm install
```

## 🚀 Running the Application

You need to run both the backend and frontend servers:

### Terminal 1 - Backend Server
```bash
# Activate virtual environment (if not already active)
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Start Flask server
python app.py
```

The backend will start on `http://localhost:5000`

### Terminal 2 - Frontend Server
```bash
# Start React development server
npm start
```

The frontend will automatically open at `http://localhost:3000`

## 📖 Usage Guide

1. **Enter Text**: Type or paste your English text (up to 1000 characters)
2. **Quick Examples**: Click example buttons for instant demos
3. **Generate Speech**: Click "Generate Speech" to create audio
4. **Listen**: Use the audio player to play the generated speech
5. **Download**: Download the audio file for offline use

### Language Support

**Currently supports: English only**

The application is configured to work with English language text-to-speech using system voices available on Windows, macOS, and Linux.

## 🎨 Example Inputs

### English
```
Hello, welcome to our text to speech service.
```

```
The quick brown fox jumps over the lazy dog.
```

```
This application converts your English text into natural-sounding speech.
```

## 🔧 API Endpoints

### Health Check
```http
GET /api/health
```

### Get Supported Languages
```http
GET /api/languages
```

### Generate Speech
```http
POST /api/tts
Content-Type: application/json

{
  "text": "Your text here",
  "language": "en"
}
```

### Get Audio File
```http
GET /api/audio/{filename}
```

### Cleanup Old Files
```http
POST /api/cleanup
```

## 📁 Project Structure

```
text-to-speech/
├── backend/
│   ├── app.py                 # Flask server
│   ├── tts_service.py         # TTS service logic
│   ├── config.py              # Configuration
│   └── backend_requirements.txt
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── TextInput.js
│   │   │   └── AudioPlayer.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
├── generated_audio/           # Output directory
├── setup.sh                   # Linux/Mac setup
├── setup.bat                  # Windows setup
├── .gitignore
└── README.md
```

## 🛠️ Configuration

Edit `config.py` to customize:

- `HOST` and `PORT` - Server address
- `MAX_TEXT_LENGTH` - Maximum input length (default: 1000 characters)
- `AUDIO_FILE_LIFETIME` - Auto-cleanup interval (default: 1 hour)
- `SPEECH_RATE` - Words per minute (default: 150)
- `SPEECH_VOLUME` - Volume level 0.0-1.0 (default: 1.0)
- `AUDIO_FORMAT` - Output format (default: WAV)

## 🐛 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'flask'` or `'pyttsx3'`
- **Solution**: Activate virtual environment and install dependencies
  ```bash
  # Activate venv first
  venv\Scripts\activate  # Windows
  source venv/bin/activate  # Linux/macOS

  # Then install
  pip install -r backend_requirements.txt
  ```

**Problem**: Audio generation hangs after first request
- **Solution**: This is fixed in the current version. Each request uses a fresh TTS engine instance. Restart the Flask server if issues persist.

**Problem**: No voices available / pyttsx3 initialization fails
- **Windows**: Ensure Windows Speech API is enabled in Settings > Time & Language > Speech
- **Linux**: Install espeak: `sudo apt-get install espeak espeak-data`
- **macOS**: Built-in, should work out of the box

**Problem**: Port 5000 already in use
- **Solution**: Change `PORT` in `config.py` or kill the process using port 5000

### Frontend Issues

**Problem**: `npm install` fails
- **Solution**: Delete `node_modules` and `package-lock.json`, then run `npm install` again

**Problem**: Cannot connect to backend
- **Solution**: Ensure backend is running on `http://localhost:5000` and check CORS settings

**Problem**: Audio not playing
- **Solution**: Check browser console for errors, ensure backend generated the file successfully

## 🔐 Security Considerations

- Input validation and sanitization
- Text length limits to prevent abuse
- CORS configuration for localhost only
- Automatic cleanup of old audio files
- No sensitive data in error messages

## 🚀 Deployment

### Production Checklist

1. **Environment Variables**
   - Set `DEBUG = False` in `config.py`
   - Configure production CORS origins
   - Use environment variables for sensitive config

2. **Backend**
   - Use Gunicorn or uWSGI instead of Flask dev server
   ```bash
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Frontend**
   - Build production bundle
   ```bash
   npm run build
   ```
   - Serve with nginx or Apache

4. **Audio Storage**
   - Configure cloud storage (AWS S3, etc.) for audio files
   - Implement CDN for faster delivery

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is created for educational purposes as part of a technical assignment.

## 🙏 Acknowledgments

- **pyttsx3** - Cross-platform text-to-speech library
- **React & Flask** - Excellent web frameworks
- **System TTS Engines** - SAPI5, NSSpeechSynthesizer, espeak
- Open-source community for amazing tools and libraries

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Open an issue on the repository

---

**Built with ❤️ using Modern Web Technologies**

*Powered by pyttsx3 | React | Flask*
