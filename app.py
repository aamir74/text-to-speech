"""
Flask Backend Server for Text-to-Speech Application
Provides RESTful API endpoints for TTS conversion
"""

import logging
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pathlib import Path
from config import Config
from tts_service import TTSService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={
    r"/api/*": {
        "origins": Config.CORS_ORIGINS,
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Initialize configuration
Config.init_app()

# Initialize TTS service
logger.info("Initializing TTS service...")
tts_service = TTSService()
logger.info("TTS service initialized successfully")


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        health_status = tts_service.health_check()
        return jsonify({
            "status": "ok",
            "service": health_status
        }), 200
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Get supported languages"""
    try:
        languages = tts_service.get_supported_languages()
        return jsonify({
            "languages": languages
        }), 200
    except Exception as e:
        logger.error(f"Error fetching languages: {str(e)}")
        return jsonify({
            "error": "Failed to fetch languages"
        }), 500


@app.route('/api/tts', methods=['POST'])
def generate_speech():
    """
    Generate speech from text

    Expected JSON payload:
    {
        "text": "Text to convert to speech",
        "language": "en"  # Optional, defaults to 'en'
    }
    """
    try:
        # Get request data
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data provided"
            }), 400

        # Extract parameters
        text = data.get('text', '').strip()
        language = data.get('language', 'en')

        # Validate text
        if not text:
            return jsonify({
                "error": "Text is required"
            }), 400

        if len(text) < Config.MIN_TEXT_LENGTH:
            return jsonify({
                "error": "Text is too short"
            }), 400

        if len(text) > Config.MAX_TEXT_LENGTH:
            return jsonify({
                "error": f"Text exceeds maximum length of {Config.MAX_TEXT_LENGTH} characters"
            }), 400

        logger.info(f"Generating speech for text (length: {len(text)}, language: {language})")

        # Generate speech
        file_path, filename = tts_service.generate_speech(text, language)

        # Return success response
        return jsonify({
            "success": True,
            "filename": filename,
            "audio_url": f"/api/audio/{filename}",
            "text_length": len(text),
            "language": language
        }), 200

    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({
            "error": str(e)
        }), 400

    except Exception as e:
        logger.error(f"Error generating speech: {str(e)}")
        return jsonify({
            "error": "Failed to generate speech. Please try again."
        }), 500


@app.route('/api/audio/<filename>', methods=['GET'])
def serve_audio(filename):
    """Serve generated audio file"""
    try:
        file_path = Config.AUDIO_OUTPUT_DIR / filename

        if not file_path.exists():
            return jsonify({
                "error": "Audio file not found"
            }), 404

        return send_file(
            file_path,
            mimetype='audio/wav',
            as_attachment=False,
            download_name=filename
        )

    except Exception as e:
        logger.error(f"Error serving audio: {str(e)}")
        return jsonify({
            "error": "Failed to serve audio file"
        }), 500


@app.route('/api/cleanup', methods=['POST'])
def cleanup_files():
    """Cleanup old audio files"""
    try:
        max_age = request.json.get('max_age_seconds') if request.json else None
        tts_service.cleanup_old_files(max_age)

        return jsonify({
            "success": True,
            "message": "Cleanup completed"
        }), 200

    except Exception as e:
        logger.error(f"Cleanup error: {str(e)}")
        return jsonify({
            "error": "Cleanup failed"
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        "error": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        "error": "Internal server error"
    }), 500


if __name__ == '__main__':
    logger.info(f"Starting Flask server on {Config.HOST}:{Config.PORT}")
    logger.info(f"CORS enabled for: {Config.CORS_ORIGINS}")

    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
