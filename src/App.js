/**
 * Main App Component
 * Text to Speech Web Application
 */

import React, { useState, useEffect } from 'react';
import './App.css';
import TextInput from './components/TextInput';
import AudioPlayer from './components/AudioPlayer';
import api from './services/api';

function App() {
  const [text, setText] = useState('');
  const [language, setLanguage] = useState('en');
  const [languages, setLanguages] = useState({ en: 'English', hi: 'Hindi' });
  const [audioUrl, setAudioUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [serverStatus, setServerStatus] = useState('checking');

  // Check server health on mount
  useEffect(() => {
    checkServerHealth();
    fetchLanguages();
  }, []);

  const checkServerHealth = async () => {
    try {
      await api.healthCheck();
      setServerStatus('online');
    } catch (error) {
      setServerStatus('offline');
      console.error('Server health check failed:', error);
    }
  };

  const fetchLanguages = async () => {
    try {
      const response = await api.getLanguages();
      if (response.languages) {
        setLanguages(response.languages);
      }
    } catch (error) {
      console.error('Failed to fetch languages:', error);
    }
  };

  const handleGenerate = async () => {
    if (!text.trim()) {
      setError('Please enter some text');
      return;
    }

    setIsLoading(true);
    setError(null);
    setAudioUrl(null);

    try {
      const response = await api.generateSpeech(text, language);

      if (response.success && response.filename) {
        const audioUrl = api.getAudioUrl(response.filename);
        setAudioUrl(audioUrl);
      } else {
        setError('Failed to generate speech');
      }
    } catch (error) {
      console.error('Error generating speech:', error);

      if (error.response && error.response.data && error.response.data.error) {
        setError(error.response.data.error);
      } else if (error.message === 'Network Error') {
        setError('Cannot connect to server. Please make sure the backend is running.');
        setServerStatus('offline');
      } else {
        setError('An error occurred while generating speech. Please try again.');
      }
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      {/* Header */}
      <header className="app-header">
        <h1>🎙️ Text to Speech</h1>
        <p className="subtitle">Multilingual Speech Synthesis Service</p>
        <div className={`server-status ${serverStatus}`}>
          <span className="status-dot"></span>
          Server: {serverStatus === 'online' ? 'Online' : serverStatus === 'offline' ? 'Offline' : 'Checking...'}
        </div>
      </header>

      {/* Main Content */}
      <main className="app-main">
        <div className="container">
          {/* Text Input Section */}
          <div className="section">
            <TextInput
              text={text}
              setText={setText}
              language={language}
              setLanguage={setLanguage}
              onGenerate={handleGenerate}
              isLoading={isLoading}
              languages={languages}
            />
          </div>

          {/* Error Message */}
          {error && (
            <div className="error-message">
              <span className="error-icon">⚠️</span>
              {error}
            </div>
          )}

          {/* Loading Indicator */}
          {isLoading && (
            <div className="loading-container">
              <div className="spinner"></div>
              <p>Generating speech...</p>
            </div>
          )}

          {/* Audio Player Section */}
          {audioUrl && !isLoading && (
            <div className="section">
              <AudioPlayer audioUrl={audioUrl} />
            </div>
          )}

          {/* Instructions */}
          {!audioUrl && !isLoading && !error && (
            <div className="instructions">
              <h3>How to Use</h3>
              <ol>
                <li>Select your desired language from the dropdown</li>
                <li>Type or paste your text (supports Hindi, English, and mixed languages)</li>
                <li>Click "Generate Speech" to convert text to audio</li>
                <li>Use the audio player to listen or download your speech</li>
              </ol>
              <p className="tip">
                💡 <strong>Tip:</strong> Try the quick example buttons for instant demos!
              </p>
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="app-footer">
        <p>Powered by Coqui TTS (XTTS v2) | Built with React & Flask</p>
        <p className="tech-info">
          Supports 16+ languages including Hindi (हिन्दी), English, Spanish, French, and more
        </p>
      </footer>
    </div>
  );
}

export default App;
