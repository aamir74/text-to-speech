"""
Text-to-Speech Service using pyttsx3
Handles audio generation from text input with multilingual support
"""

import os
import time
import logging
from pathlib import Path
from typing import Optional, Tuple
import pyttsx3
import threading
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global lock for thread-safe pyttsx3 usage
_engine_lock = threading.Lock()


class TTSService:
    """Text-to-Speech service using pyttsx3"""

    def __init__(self):
        """Initialize TTS service with engine"""
        self.engine = None
        logger.info("Initializing pyttsx3 TTS engine")
        self._load_engine()

    def _load_engine(self):
        """Initialize the TTS engine"""
        try:
            self.engine = pyttsx3.init()

            # Set properties
            self.engine.setProperty('rate', Config.SPEECH_RATE)
            self.engine.setProperty('volume', Config.SPEECH_VOLUME)

            # Get available voices
            voices = self.engine.getProperty('voices')
            if voices:
                logger.info(f"Found {len(voices)} voices available")
                # Set default voice (first available)
                self.engine.setProperty('voice', voices[0].id)

            logger.info("TTS engine loaded successfully")
        except Exception as e:
            logger.error(f"Failed to load TTS engine: {str(e)}")
            raise

    def generate_speech(
        self,
        text: str,
        language: str = "en",
        speaker_wav: Optional[str] = None
    ) -> Tuple[str, str]:
        """
        Generate speech from text

        Args:
            text: Input text to convert to speech
            language: Language code (e.g., 'en', 'hi') - note: pyttsx3 uses system voices
            speaker_wav: Optional path to speaker reference audio (ignored for pyttsx3)

        Returns:
            Tuple of (file_path, filename)
        """
        # Validate text
        if not text or len(text.strip()) < Config.MIN_TEXT_LENGTH:
            raise ValueError("Text is too short")

        if len(text) > Config.MAX_TEXT_LENGTH:
            raise ValueError(f"Text exceeds maximum length of {Config.MAX_TEXT_LENGTH}")

        # Validate language
        if language not in Config.SUPPORTED_LANGUAGES:
            logger.warning(f"Unsupported language '{language}', defaulting to 'en'")
            language = "en"

        # Use lock to ensure only one pyttsx3 operation at a time
        with _engine_lock:
            engine = None
            try:
                # Generate unique filename
                timestamp = int(time.time() * 1000)
                filename = f"speech_{timestamp}.{Config.AUDIO_FORMAT}"
                output_path = Config.AUDIO_OUTPUT_DIR / filename

                logger.info(f"Generating speech for text (length: {len(text)}, language: {language})")

                # Initialize engine with explicit driver to avoid caching issues
                try:
                    # Try SAPI5 driver on Windows (more reliable)
                    engine = pyttsx3.init('sapi5', debug=False)
                except:
                    # Fallback to default driver
                    logger.warning("SAPI5 driver not available, using default driver")
                    engine = pyttsx3.init(debug=False)

                # Set properties
                engine.setProperty('rate', Config.SPEECH_RATE)
                engine.setProperty('volume', Config.SPEECH_VOLUME)

                # Try to set voice based on language
                self._set_voice_for_language_on_engine(engine, language)

                # Generate speech and save to file
                engine.save_to_file(text, str(output_path))
                engine.runAndWait()

                logger.info(f"Speech generated successfully: {filename}")
                return str(output_path), filename

            except Exception as e:
                logger.error(f"Error generating speech: {str(e)}")
                raise RuntimeError(f"Failed to generate speech: {str(e)}")
            finally:
                # Always cleanup the engine
                if engine is not None:
                    try:
                        engine.stop()
                        del engine
                    except:
                        pass

    def _set_voice_for_language_on_engine(self, engine, language: str):
        """
        Try to set appropriate voice for the given language on a specific engine

        Args:
            engine: pyttsx3 engine instance
            language: Language code
        """
        try:
            voices = engine.getProperty('voices')

            # Language to voice mapping patterns
            language_patterns = {
                'en': ['english', 'en_', 'en-'],
                'es': ['spanish', 'es_', 'es-'],
                'fr': ['french', 'fr_', 'fr-'],
                'de': ['german', 'de_', 'de-'],
                'it': ['italian', 'it_', 'it-'],
                'pt': ['portuguese', 'pt_', 'pt-'],
                'ru': ['russian', 'ru_', 'ru-'],
                'zh-cn': ['chinese', 'zh_', 'zh-', 'mandarin'],
                'ja': ['japanese', 'ja_', 'ja-'],
                'ko': ['korean', 'ko_', 'ko-'],
                'hi': ['hindi', 'hi_', 'hi-'],
                'ar': ['arabic', 'ar_', 'ar-'],
            }

            patterns = language_patterns.get(language, [language])

            # Try to find matching voice
            for voice in voices:
                voice_name_lower = voice.name.lower()
                voice_id_lower = voice.id.lower()

                for pattern in patterns:
                    if pattern.lower() in voice_name_lower or pattern.lower() in voice_id_lower:
                        engine.setProperty('voice', voice.id)
                        logger.info(f"Set voice to: {voice.name} for language: {language}")
                        return

            logger.warning(f"No specific voice found for language '{language}', using default English voice")

        except Exception as e:
            logger.warning(f"Error setting voice for language: {str(e)}")

    def _set_voice_for_language(self, language: str):
        """
        Try to set appropriate voice for the given language (legacy method for self.engine)

        Args:
            language: Language code
        """
        if self.engine:
            self._set_voice_for_language_on_engine(self.engine, language)

    def cleanup_old_files(self, max_age_seconds: int = None):
        """
        Remove audio files older than specified age

        Args:
            max_age_seconds: Maximum file age in seconds
        """
        if max_age_seconds is None:
            max_age_seconds = Config.AUDIO_FILE_LIFETIME

        current_time = time.time()
        removed_count = 0

        try:
            for audio_file in Config.AUDIO_OUTPUT_DIR.glob(f"*.{Config.AUDIO_FORMAT}"):
                file_age = current_time - audio_file.stat().st_mtime

                if file_age > max_age_seconds:
                    audio_file.unlink()
                    removed_count += 1
                    logger.info(f"Removed old audio file: {audio_file.name}")

            if removed_count > 0:
                logger.info(f"Cleanup complete: {removed_count} files removed")

        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")

    def get_supported_languages(self) -> dict:
        """Get list of supported languages"""
        return Config.SUPPORTED_LANGUAGES

    def get_available_voices(self) -> list:
        """Get list of available voices on the system"""
        try:
            voices = self.engine.getProperty('voices')
            return [{"id": voice.id, "name": voice.name, "languages": voice.languages}
                    for voice in voices]
        except Exception as e:
            logger.error(f"Error getting voices: {str(e)}")
            return []

    def health_check(self) -> dict:
        """Check if TTS service is healthy"""
        return {
            "status": "healthy" if self.engine else "unhealthy",
            "engine": "pyttsx3",
            "supported_languages": len(Config.SUPPORTED_LANGUAGES),
            "available_voices": len(self.get_available_voices())
        }
