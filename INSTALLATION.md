# 📦 Installation Guide

Complete installation instructions for the Text-to-Speech Frontend Application.

**Note**: This is the frontend only. You must have the Node.js backend running separately on port 5000.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Node.js**: 14.0 or higher
- **RAM**: 2GB minimum (4GB recommended)
- **Disk Space**: 500MB free space
- **Internet**: Required for initial setup
- **Backend**: Node.js backend server (separate repository) running on `http://localhost:5000`

### Software Prerequisites

#### Node.js Installation

**Windows:**
1. Download Node.js from [nodejs.org](https://nodejs.org/)
2. Run installer (includes npm)
3. Verify installation:
   ```cmd
   node --version
   npm --version
   ```

**macOS:**
```bash
# Using Homebrew
brew install node

# Verify
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

## Installation

### Step 1: Get the Project

```bash
# If using Git
git clone <repository-url>
cd text-to-speech-frontend

# Or download and extract ZIP
cd text-to-speech-frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

This will install:
- React 18.2.0
- React DOM 18.2.0
- React Scripts 5.0.1
- Axios 1.6.2
- All required build tools

**Installation time**: 2-3 minutes depending on internet speed

### Step 3: Verify Backend

**CRITICAL**: Ensure your Node.js backend (separate repository) is:
1. Running on `http://localhost:5000`
2. Properly configured with CORS
3. Exposing the required API endpoints

Test backend:
```bash
curl http://localhost:5000/api/health
```

You should see a JSON health response.

**Without the backend running, this frontend will not function.**

## Configuration

### Backend URL Configuration

The frontend is configured to connect to the Node.js backend at `http://localhost:5000` via proxy.

**To change the backend URL** (if your Node.js backend runs on a different port), edit `package.json`:

```json
{
  "proxy": "http://localhost:5000"
}
```

Change the port number to match your Node.js backend's port.

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
REACT_APP_API_URL=http://localhost:5000
PORT=3000
```

## Verification

### Verify Installation

1. **Start the frontend**:
   ```bash
   npm start
   ```

2. **Expected output**:
   ```
   Compiled successfully!

   You can now view text-to-speech-frontend in the browser.

     Local:            http://localhost:3000
     On Your Network:  http://192.168.x.x:3000
   ```

3. **Browser opens** at `http://localhost:3000`

4. **Check connection**: Top-right should show "🟢 Server Online"

5. Press `Ctrl+C` to stop

## Troubleshooting Installation Issues

### Node.js Issues

**Problem**: `node: command not found`
- **Solution**: Node.js not in PATH. Reinstall Node.js and ensure "Add to PATH" is checked

**Problem**: npm version too old
- **Solution**: Update npm:
  ```bash
  npm install -g npm@latest
  ```

### Installation Issues

**Problem**: `npm install` fails with network errors
- **Solution**:
  ```bash
  npm config set registry https://registry.npmjs.org/
  npm cache clean --force
  npm install
  ```

**Problem**: `npm install` fails with permission errors (Linux/macOS)
- **Solution**:
  ```bash
  sudo chown -R $USER:$(id -gn $USER) ~/.npm
  sudo chown -R $USER:$(id -gn $USER) ~/.config
  npm install
  ```

**Problem**: Port 3000 already in use
- **Solution**:
  ```bash
  # Windows
  netstat -ano | findstr :3000
  taskkill /PID <PID> /F

  # Linux/macOS
  lsof -ti:3000 | xargs kill -9
  ```

**Problem**: Cannot connect to backend
- **Solution**:
  1. **Verify Node.js backend (separate repository) is running**: `curl http://localhost:5000/api/health`
  2. Check CORS is enabled on the Node.js backend
  3. Verify proxy in `package.json` points to correct backend URL
  4. Check browser console for specific errors
  5. Ensure backend is listening on all interfaces or localhost

### React Issues

**Problem**: Browser shows blank page
- **Solution**:
  1. Check browser console for errors
  2. Clear browser cache
  3. Rebuild: `npm run build && npm start`

**Problem**: Hot reload not working
- **Solution**:
  ```bash
  # Create/edit .env file
  echo "FAST_REFRESH=true" > .env
  npm start
  ```

## Running the Application

### Development Mode

```bash
npm start
```

- Runs on `http://localhost:3000`
- Hot reload enabled
- Source maps for debugging

### Production Build

```bash
npm run build
```

Creates optimized production build in `build/` directory.

### Serve Production Build

```bash
# Install serve globally
npm install -g serve

# Serve the build
serve -s build -p 3000
```

## Project Structure

```
text-to-speech-frontend/
├── node_modules/          # Dependencies (auto-generated)
├── public/
│   ├── index.html         # HTML template
│   └── favicon.ico        # Favicon
├── src/
│   ├── components/
│   │   ├── TextInput.js   # Text input component
│   │   └── AudioPlayer.js # Audio player component
│   ├── services/
│   │   └── api.js         # API service layer
│   ├── App.js             # Main app component
│   ├── App.css            # App styles
│   └── index.js           # Entry point
├── .gitignore             # Git ignore rules
├── .gitattributes         # Git line ending rules
├── package.json           # Dependencies & scripts (includes backend proxy)
├── package-lock.json      # Dependency lock file
├── README.md              # Documentation
├── QUICKSTART.md          # Quick start guide
└── INSTALLATION.md        # This file
```

**Note**: This is frontend only. Backend files are in a separate Node.js repository.

## Deployment

### Build for Production

```bash
npm run build
```

### Deploy to Vercel

```bash
npm install -g vercel
vercel deploy
```

### Deploy to Netlify

1. Build the project: `npm run build`
2. Drag and drop `build` folder to Netlify
3. Or use Netlify CLI:
   ```bash
   npm install -g netlify-cli
   netlify deploy --prod
   ```

### Deploy to AWS S3

```bash
# Build
npm run build

# Upload to S3 (requires AWS CLI)
aws s3 sync build/ s3://your-bucket-name --acl public-read
```

### Deploy with Docker

Create `Dockerfile`:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-p", "3000"]
EXPOSE 3000
```

Build and run:
```bash
docker build -t tts-frontend .
docker run -p 3000:3000 tts-frontend
```

## Uninstallation

### Remove Dependencies

```bash
# Remove node_modules
rm -rf node_modules

# Remove package lock
rm package-lock.json
```

### Remove Build Files

```bash
rm -rf build
```

### Complete Clean

```bash
# Remove all generated files
rm -rf node_modules build package-lock.json
```

## Next Steps

After installation:
1. **Ensure your Node.js backend (separate repository) is running on port 5000**
2. Read [QUICKSTART.md](QUICKSTART.md) to start using the app
3. Read [README.md](README.md) for full documentation
4. Test with example texts

## Getting Help

If you encounter issues:
1. **First, ensure Node.js backend (separate repository) is running on port 5000**
2. Check [Troubleshooting](#troubleshooting-installation-issues) section
3. Review error messages in terminal
4. Check browser console for errors
5. Verify backend is accessible: `curl http://localhost:5000/api/health`
6. Verify Node.js and npm versions

---

**Ready to run?** See [QUICKSTART.md](QUICKSTART.md) for next steps!
