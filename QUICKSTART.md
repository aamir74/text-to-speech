# 🚀 Quick Start Guide

Get your frontend running and connected to the Node.js backend in under 2 minutes!

## Prerequisites

- ✅ Node.js 14+ installed ([Download](https://nodejs.org/))
- ✅ **Node.js backend running on `http://localhost:5000`** (separate repository)

## Setup Steps

### 1. Install Dependencies

```bash
cd text-to-speech-frontend
npm install
```

⏱️ **Time**: 1-2 minutes (depending on internet speed)

### 2. Verify Backend is Running

**IMPORTANT**: Make sure your Node.js backend (separate repository) is running on `http://localhost:5000`

Test it by visiting: `http://localhost:5000/api/health`

You should see a JSON response indicating the server is healthy.

**Note**: This frontend will NOT work without the backend running.

### 3. Start Frontend Server

```bash
npm start
```

**Expected behavior:**
- React development server starts
- Browser automatically opens at `http://localhost:3000`
- You see the Text-to-Speech interface
- Top-right shows "🟢 Server Online" if backend is connected

## First Test

Try the application with these steps:

1. **Check Status**: Top-right should show "🟢 Server Online"
2. **Use Example**: Click "English Example" button (auto-fills text)
3. **Generate**: Click "Generate Speech" button
4. **Listen**: Audio player appears - click play ▶️
5. **Download**: (Optional) Download the WAV file

🎉 **Success!** You should hear the generated speech.

## Testing

### Quick Test
```
Hello, welcome to our text to speech service!
```

### Longer Test
```
The quick brown fox jumps over the lazy dog. This is a test of the text to speech system.
```

## Common Issues & Quick Fixes

### ❌ Frontend shows "Server Offline"

**Fix**:
1. Check if Node.js backend is running on port 5000
2. Visit `http://localhost:5000/api/health` in browser
3. If no response, start your Node.js backend
4. Refresh frontend (`http://localhost:3000`)

### ❌ CORS Errors

**Fix**:
- Ensure your Node.js backend has CORS enabled
- Check backend allows `http://localhost:3000` origin
- Verify proxy setting in `package.json`

### ❌ Port 3000 already in use

**Fix**:
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Linux/macOS
lsof -ti:3000 | xargs kill -9
```

### ❌ npm install fails

**Fix**:
```bash
# Clean install
rm -rf node_modules package-lock.json
npm install
```

## Stopping the Application

```bash
# In the terminal running npm start
Press Ctrl+C
```

## Next Steps

### Learn More
- 📖 [README.md](README.md) - Full documentation
- 🔧 [package.json](package.json) - Configuration

### Customize
- Modify UI colors in `src/App.css`
- Update API endpoints in `src/services/api.js`
- Adjust proxy in `package.json`

### Deploy
- Build: `npm run build`
- Deploy to Vercel, Netlify, or AWS S3

## Project Structure

```
Frontend (this repo)     Backend (separate repo)
http://localhost:3000    http://localhost:5000
        │                        │
        └────── API calls ───────┘
                 (proxied)
```

## Need Help?

**Backend not responding?**
- Ensure Node.js backend is running
- Check backend terminal for errors
- Verify backend port is 5000

**Frontend issues?**
- Check browser console for errors
- Verify npm dependencies installed
- Try `npm start` again

**Everything working?** 🎉
- Try different texts
- Experiment with longer sentences
- Download audio files
- Open DevTools to see API calls

---

**Happy Coding! 🚀**

*Make sure your Node.js backend is running first!*
