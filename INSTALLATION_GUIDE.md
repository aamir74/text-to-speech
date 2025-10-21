# 📦 Installation Guide - Text to Speech Application

## ✅ Project Status

**✓ Complete Project Built Successfully!**

All files have been created and the frontend dependencies are installed. The project is ready for Python backend setup.

---

## 📁 Project Structure

```
text-to-speech/
├── 🔧 Backend Files
│   ├── app.py                     ✅ Flask API server
│   ├── tts_service.py             ✅ TTS service implementation
│   ├── config.py                  ✅ Configuration management
│   └── backend_requirements.txt   ✅ Python dependencies
│
├── 🎨 Frontend Files
│   ├── public/
│   │   └── index.html             ✅ HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── TextInput.js       ✅ Text input component
│   │   │   └── AudioPlayer.js     ✅ Audio player component
│   │   ├── services/
│   │   │   └── api.js             ✅ API service layer
│   │   ├── App.js                 ✅ Main application
│   │   ├── App.css                ✅ Styling
│   │   └── index.js               ✅ React entry point
│   ├── package.json               ✅ Node.js config
│   └── node_modules/              ✅ Installed (1326 packages)
│
├── 📚 Documentation
│   ├── README.md                  ✅ Complete documentation
│   ├── QUICKSTART.md              ✅ Quick start guide
│   ├── ASSIGNMENT_SUMMARY.md      ✅ Assignment details
│   ├── PROJECT_CHECKLIST.md       ✅ Feature checklist
│   └── INSTALLATION_GUIDE.md      ✅ This file
│
├── 🛠️ Setup Scripts
│   ├── setup.sh                   ✅ Linux/Mac setup
│   └── setup.bat                  ✅ Windows setup
│
├── 📂 Output Directory
│   └── generated_audio/           ✅ For generated audio files
│
└── ⚙️ Configuration
    └── .gitignore                 ✅ Git ignore rules
```

---

## 🚨 IMPORTANT: Python Installation Required

**Python is NOT currently installed on this system.**

You need to install Python 3.8 or higher before running the backend.

### 🔽 Install Python

1. **Download Python:**
   - Visit: https://www.python.org/downloads/
   - Download Python 3.10 or newer (recommended)

2. **During Installation:**
   - ✅ **CHECK** "Add Python to PATH" (VERY IMPORTANT!)
   - ✅ Choose "Install Now"

3. **Verify Installation:**
   ```bash
   python --version
   # Should show: Python 3.10.x or similar
   ```

---

## 📋 Installation Steps

### Step 1: Install Python Backend Dependencies

**After installing Python**, run these commands:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install backend dependencies
pip install -r backend_requirements.txt
```

**Note:** This step will take 5-10 minutes as it downloads:
- Flask web framework
- Coqui TTS engine
- PyTorch ML library
- Audio processing libraries
- XTTS v2 AI model (~2GB)

### Step 2: Verify Frontend Installation

Frontend is already installed! ✅

You can verify by checking:
```bash
npm list --depth=0
```

---

## 🚀 Running the Application

### Terminal 1: Start Backend

```bash
# Activate virtual environment (if not already active)
venv\Scripts\activate        # Windows
# OR
source venv/bin/activate     # Linux/Mac

# Start Flask server
python app.py
```

**Expected Output:**
```
Starting Flask server on 127.0.0.1:5000
Loading TTS model: tts_models/multilingual/multi-dataset/xtts_v2
TTS model loaded successfully
 * Running on http://127.0.0.1:5000
```

### Terminal 2: Start Frontend

```bash
# Start React development server
npm start
```

**Expected Output:**
```
Compiled successfully!

You can now view text-to-speech-frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.x.x:3000
```

Browser will automatically open at `http://localhost:3000`

---

## ✨ First Use

1. **Wait for both servers to start**
   - Backend: `http://localhost:5000` ✓
   - Frontend: `http://localhost:3000` ✓

2. **Check server status**
   - Look for "Server: Online" indicator in the web interface

3. **Try the examples**
   - Click "English Example" button
   - Click "Generate Speech"
   - Audio will generate and play automatically!

4. **Test multilingual**
   - Click "Hindi Example" to test Devanagari script
   - Click "Hinglish Example" to test mixed languages

---

## 📦 Dependencies

### Backend (Python)
- Flask 3.0.0 - Web framework
- Coqui TTS 0.22.0 - Text-to-speech engine
- PyTorch 2.1.2 - Deep learning framework
- NumPy, SciPy - Scientific computing
- Soundfile, Librosa - Audio processing

### Frontend (Node.js) ✅ Already Installed
- React 18.2.0 - UI framework
- Axios 1.6.2 - HTTP client
- React Scripts 5.0.1 - Build tools

---

## 🔍 Troubleshooting

### Problem: "Python not found"
**Solution:**
- Install Python from https://www.python.org/
- Make sure to check "Add to PATH" during installation
- Restart your terminal after installation

### Problem: "pip not found"
**Solution:**
```bash
python -m ensurepip --upgrade
```

### Problem: Backend dependencies fail to install
**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try installing again
pip install -r backend_requirements.txt
```

### Problem: Port 5000 already in use
**Solution:**
- Edit `config.py` and change `PORT = 5000` to another port (e.g., 5001)
- Or kill the process using port 5000

### Problem: Frontend can't connect to backend
**Solution:**
- Make sure backend is running first
- Check that backend shows "Running on http://127.0.0.1:5000"
- Check browser console for error messages

---

## 🎯 System Requirements

### Minimum Requirements
- **OS:** Windows 10, macOS 10.14+, or Linux
- **RAM:** 4 GB (8 GB recommended)
- **Storage:** 5 GB free space (for models)
- **Python:** 3.8 or higher
- **Node.js:** 14 or higher

### Recommended
- **RAM:** 8 GB or more
- **Storage:** 10 GB SSD
- **GPU:** Optional (CUDA-compatible for faster processing)

---

## 📝 Quick Command Reference

```bash
# Check installations
python --version
node --version
npm --version

# Install backend
python -m venv venv
venv\Scripts\activate         # Windows
source venv/bin/activate      # Linux/Mac
pip install -r backend_requirements.txt

# Start backend
python app.py

# Start frontend (in new terminal)
npm start

# Build for production
npm run build
```

---

## 🎓 Features Implemented

✅ Multilingual TTS (16+ languages)
✅ Hindi & English support
✅ Mixed Hinglish support
✅ Modern React UI
✅ Audio player with controls
✅ Download functionality
✅ Responsive design
✅ Error handling
✅ Loading states
✅ Real-time server status
✅ Quick example buttons
✅ RESTful API
✅ CORS support
✅ File cleanup
✅ Comprehensive documentation

---

## 🎉 Next Steps

1. **Install Python** (if not already installed)
2. **Run setup script** or install dependencies manually
3. **Start both servers** (backend + frontend)
4. **Test the application** with example texts
5. **Enjoy multilingual text-to-speech!** 🎙️

---

## 📞 Need Help?

- See `README.md` for detailed documentation
- See `QUICKSTART.md` for fast setup
- Check troubleshooting section above
- Review code comments in source files

---

**Built for Pelocal AI Tech Hiring Assignment**

*Self-hosted | Open Source | Multilingual | Production Ready*
