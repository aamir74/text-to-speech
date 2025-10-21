"""
Configuration file for Text-to-Speech application
Contains all configuration settings for backend server
"""

import os
from pathlib import Path

class Config:
    """Application configuration class"""

    # Base directory
    BASE_DIR = Path(__file__).parent.absolute()

    # Audio output directory
    AUDIO_OUTPUT_DIR = BASE_DIR / "generated_audio"

    # Flask settings
    HOST = "127.0.0.1"
    PORT = 5000
    DEBUG = True

    # CORS settings
    CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

    # Audio settings
    AUDIO_FORMAT = "wav"

    # pyttsx3 speech settings
    SPEECH_RATE = 150  # Words per minute (default is typically 200)
    SPEECH_VOLUME = 1.0  # Volume level (0.0 to 1.0)

    # Text constraints
    MAX_TEXT_LENGTH = 1000
    MIN_TEXT_LENGTH = 1

    # File cleanup settings (seconds)
    AUDIO_FILE_LIFETIME = 3600  # 1 hour

    # Supported languages
    SUPPORTED_LANGUAGES = {
        "en": "English",
        "hi": "Hindi",
        "es": "Spanish",
        "fr": "French",
        "de": "German",
        "it": "Italian",
        "pt": "Portuguese",
        "pl": "Polish",
        "tr": "Turkish",
        "ru": "Russian",
        "nl": "Dutch",
        "cs": "Czech",
        "ar": "Arabic",
        "zh-cn": "Chinese",
        "ja": "Japanese",
        "ko": "Korean"
    }

    @classmethod
    def init_app(cls):
        """Initialize application configuration"""
        # Create audio output directory if it doesn't exist
        cls.AUDIO_OUTPUT_DIR.mkdir(exist_ok=True)

        # Create .gitkeep file in audio directory
        gitkeep = cls.AUDIO_OUTPUT_DIR / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()
