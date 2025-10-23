/**
 * AudioPlayer Component
 * Handles audio playback with controls (play/pause, seek, volume, download)
 */

import React, { useState, useRef, useEffect } from 'react';

const AudioPlayer = ({ audioUrl }) => {
  const audioRef = useRef(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [volume, setVolume] = useState(1);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    // Event listeners
    const handleLoadedMetadata = () => {
      setDuration(audio.duration);
    };

    const handleTimeUpdate = () => {
      setCurrentTime(audio.currentTime);
    };

    const handleEnded = () => {
      setIsPlaying(false);
      setCurrentTime(0);
    };

    audio.addEventListener('loadedmetadata', handleLoadedMetadata);
    audio.addEventListener('timeupdate', handleTimeUpdate);
    audio.addEventListener('ended', handleEnded);

    // Auto-play when new audio is loaded
    audio.play().then(() => {
      setIsPlaying(true);
    }).catch((error) => {
      console.error('Auto-play failed:', error);
    });

    return () => {
      audio.removeEventListener('loadedmetadata', handleLoadedMetadata);
      audio.removeEventListener('timeupdate', handleTimeUpdate);
      audio.removeEventListener('ended', handleEnded);
    };
  }, [audioUrl]);

  const togglePlayPause = () => {
    const audio = audioRef.current;
    if (isPlaying) {
      audio.pause();
    } else {
      audio.play();
    }
    setIsPlaying(!isPlaying);
  };

  const handleSeek = (e) => {
    const audio = audioRef.current;
    const seekTime = parseFloat(e.target.value);
    audio.currentTime = seekTime;
    setCurrentTime(seekTime);
  };

  const handleVolumeChange = (e) => {
    const audio = audioRef.current;
    const newVolume = parseFloat(e.target.value);
    audio.volume = newVolume;
    setVolume(newVolume);
  };

  const handleDownload = () => {
    const link = document.createElement('a');
    link.href = audioUrl;
    link.download = `speech_${Date.now()}.mp3`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const formatTime = (time) => {
    if (isNaN(time)) return '0:00';
    const minutes = Math.floor(time / 60);
    const seconds = Math.floor(time % 60);
    return `${minutes}:${seconds.toString().padStart(2, '0')}`;
  };

  return (
    <div className="audio-player">
      <h3>Generated Audio</h3>

      <audio ref={audioRef} src={audioUrl} preload="metadata" />

      {/* Play/Pause Button */}
      <div className="player-controls">
        <button
          onClick={togglePlayPause}
          className="play-pause-btn"
          title={isPlaying ? 'Pause' : 'Play'}
        >
          {isPlaying ? '⏸️' : '▶️'}
        </button>

        {/* Time Display */}
        <div className="time-display">
          <span>{formatTime(currentTime)}</span>
          <span> / </span>
          <span>{formatTime(duration)}</span>
        </div>

        {/* Download Button */}
        <button
          onClick={handleDownload}
          className="download-btn"
          title="Download Audio"
        >
          ⬇️ Download
        </button>
      </div>

      {/* Progress Bar */}
      <div className="progress-container">
        <input
          type="range"
          min="0"
          max={duration || 0}
          value={currentTime}
          onChange={handleSeek}
          className="progress-bar"
        />
      </div>

      {/* Volume Control */}
      <div className="volume-container">
        <label>🔊 Volume:</label>
        <input
          type="range"
          min="0"
          max="1"
          step="0.1"
          value={volume}
          onChange={handleVolumeChange}
          className="volume-slider"
        />
        <span>{Math.round(volume * 100)}%</span>
      </div>

      {/* Audio Info */}
      <div className="audio-info">
        <p>Format: MP3 | Generated via Google TTS</p>
      </div>
    </div>
  );
};

export default AudioPlayer;
