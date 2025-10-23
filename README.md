# 🎙️ Text to Speech - Frontend Application

A modern React-based frontend for a Text-to-Speech application. This frontend connects to a separate Node.js backend service (running on http://localhost:5000) for text-to-speech conversion.

![Technology Stack](https://img.shields.io/badge/Frontend-React-61DAFB?style=flat&logo=react)
![Backend](https://img.shields.io/badge/Backend-Node.js-339933?style=flat&logo=node.js)

**Note**: This is the frontend only. The Node.js backend must be running separately on port 5000.

## ✨ Features

### Core Features
- 🗣️ **English Text-to-Speech**: Converts English text to natural-sounding speech via backend API
- 🎵 **Audio Player**: Interactive player with play/pause, seek, and volume controls
- 💾 **Download Audio**: Download generated speech as WAV files
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Fast & Lightweight**: Clean React application with minimal dependencies

### User Interface
- Modern gradient design with smooth animations
- Real-time server status indicator
- Character counter for text input
- Quick example buttons for testing
- Loading indicators and error messages
- Clean, intuitive user experience

### Technical Features
- RESTful API integration
- Component-based React architecture
- Axios for HTTP requests
- Error handling and validation
- Production-ready code structure

## 🏗️ Technology Stack

### Frontend
- **React** 18.2.0 - Modern UI framework
- **Axios** 1.6.2 - HTTP client for API calls
- **React Scripts** 5.0.1 - Build tooling
- **Custom CSS** - Responsive styling with gradients

### Backend (Separate Repository)
- **Node.js** - Backend runtime
- **Express** - Backend framework (assumed)
- Runs on `http://localhost:5000`

## 📦 Installation

### Prerequisites
- **Node.js 14+** - [Download Node.js](https://nodejs.org/)
- **npm** - Node package manager (included with Node.js)
- **Backend Server** - Running Node.js backend on `http://localhost:5000`

### Frontend Setup

1. **Clone or download the project**
```bash
cd text-to-speech-frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Ensure backend is running**
   - Make sure your Node.js backend is running on `http://localhost:5000`
   - The frontend is configured to proxy API requests to this address

## 🚀 Running the Application

### Start Frontend Server
```bash
npm start
```

The frontend will automatically open at `http://localhost:3000`

**Note**: Ensure your Node.js backend is running on `http://localhost:5000` before starting the frontend.

## 📖 Usage Guide

1. **Enter Text**: Type or paste your English text (up to 1000 characters)
2. **Quick Examples**: Click example buttons for instant demos
3. **Generate Speech**: Click "Generate Speech" to create audio
4. **Listen**: Use the audio player to play the generated speech
5. **Download**: Download the audio file for offline use

### Language Support

**Currently supports: English only**

The application is configured to work with English language text-to-speech through the backend API.

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

## 🔧 API Integration

The frontend expects the backend to expose the following endpoints:

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

## 📁 Project Structure

```
text-to-speech-frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── TextInput.js
│   │   └── AudioPlayer.js
│   ├── services/
│   │   └── api.js
│   ├── App.js
│   ├── App.css
│   └── index.js
├── package.json
├── .gitignore
└── README.md
```

## 🛠️ Configuration

### Backend API URL

The backend URL is configured in `package.json`:

```json
{
  "proxy": "http://localhost:5000"
}
```

To change the backend URL, update this proxy setting.

### Environment Variables (Optional)

You can create a `.env` file for configuration:

```env
REACT_APP_API_URL=http://localhost:5000
```

## 🐛 Troubleshooting

### Frontend Issues

**Problem**: `npm install` fails
- **Solution**: Delete `node_modules` and `package-lock.json`, then run `npm install` again

**Problem**: Cannot connect to backend
- **Solution**:
  - Ensure backend is running on `http://localhost:5000`
  - Check browser console for CORS errors
  - Verify proxy setting in `package.json`

**Problem**: Audio not playing
- **Solution**:
  - Check browser console for errors
  - Ensure backend generated the file successfully
  - Check network tab in browser DevTools

**Problem**: Port 3000 already in use
- **Solution**:
  ```bash
  # Windows
  netstat -ano | findstr :3000
  taskkill /PID <PID> /F

  # Linux/macOS
  lsof -ti:3000 | xargs kill -9
  ```

## 🚀 Building for Production

### Create Production Build
```bash
npm run build
```

This creates an optimized build in the `build/` directory.

### Serve Production Build
```bash
npx serve -s build
```

### Deploy to Hosting
- **Vercel**: `vercel deploy`
- **Netlify**: Drag and drop `build` folder
- **AWS S3**: Upload `build` folder contents

## 🔐 Security Considerations

- Input validation and sanitization
- Text length limits to prevent abuse
- CORS configuration for allowed origins
- No sensitive data in error messages

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review the code comments
- Check browser console for errors

---

**Built with ❤️ using React**

*Frontend for Node.js Text-to-Speech Backend*
