/**
 * API Service for Text-to-Speech Application
 * Handles all communication with the Flask backend
 */

import axios from 'axios';

// Base URL for API requests from environment variable
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';
const API_TIMEOUT = parseInt(process.env.REACT_APP_API_TIMEOUT) || 30000;

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: API_TIMEOUT,
});

/**
 * API Service object with all endpoint methods
 */
const api = {
  /**
   * Health check endpoint
   * @returns {Promise} Server health status
   */
  healthCheck: async () => {
    try {
      const response = await apiClient.get('/');
      return response.data;
    } catch (error) {
      console.error('Health check failed:', error);
      throw error;
    }
  },

  /**
   * Get supported languages
   * @returns {Promise} List of supported languages
   */
  getLanguages: async () => {
    try {
      const response = await apiClient.get('/languages');
      return response.data;
    } catch (error) {
      console.error('Failed to fetch languages:', error);
      throw error;
    }
  },

  /**
   * Generate speech from text
   * @param {string} text - Text to convert to speech
   * @param {string} language - Language code (e.g., 'en', 'hi')
   * @returns {Promise} Generated audio information
   */
  generateSpeech: async (text, language = 'en') => {
    try {
      const response = await apiClient.post('/tts', {
        text,
        language,
      });
      return response.data;
    } catch (error) {
      console.error('Failed to generate speech:', error);
      throw error;
    }
  },

  /**
   * Get audio file URL
   * @param {string} filename - Audio filename
   * @returns {string} Full audio URL
   */
  getAudioUrl: (filename) => {
    return `${API_BASE_URL}/audio/${filename}`;
  },

  /**
   * Cleanup old audio files
   * @param {number} maxAgeSeconds - Maximum file age in seconds
   * @returns {Promise} Cleanup result
   */
  cleanupFiles: async (maxAgeSeconds = null) => {
    try {
      const response = await apiClient.post('/cleanup', {
        max_age_seconds: maxAgeSeconds,
      });
      return response.data;
    } catch (error) {
      console.error('Cleanup failed:', error);
      throw error;
    }
  },
};

export default api;
