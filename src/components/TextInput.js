/**
 * TextInput Component
 * Handles text input, language selection, and example text buttons
 */

import React from 'react';

const TextInput = ({ text, setText, language, setLanguage, onGenerate, isLoading, languages }) => {
  const MAX_LENGTH = 1000;

  // Example texts for quick testing
  const examples = [
    {
      label: 'English Example',
      text: 'Hello, welcome to our text to speech service.',
      lang: 'en'
    },
    {
      label: 'Hindi Example',
      text: 'नमस्ते, हमारी टेक्स्ट टू स्पीच सेवा में आपका स्वागत है।',
      lang: 'hi'
    },
    {
      label: 'Hinglish Example',
      text: 'Hello दोस्तों, aaj hum seekhenge text to speech के बारे में।',
      lang: 'en'
    }
  ];

  const handleExampleClick = (example) => {
    setText(example.text);
    setLanguage(example.lang);
  };

  const handleClear = () => {
    setText('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim() && !isLoading) {
      onGenerate();
    }
  };

  return (
    <div className="text-input-container">
      <h2>Enter Text</h2>

      <form onSubmit={handleSubmit}>
        {/* Language Selection */}
        <div className="language-selector">
          <label htmlFor="language">Language:</label>
          <select
            id="language"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            disabled={isLoading}
          >
            {Object.entries(languages).map(([code, name]) => (
              <option key={code} value={code}>
                {name}
              </option>
            ))}
          </select>
        </div>

        {/* Text Area */}
        <div className="textarea-wrapper">
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type or paste your text here... (supports Hindi, English, and mixed languages)"
            maxLength={MAX_LENGTH}
            disabled={isLoading}
            rows={8}
          />
          <div className="char-counter">
            {text.length} / {MAX_LENGTH}
          </div>
        </div>

        {/* Example Buttons */}
        <div className="example-buttons">
          <span className="example-label">Quick Examples:</span>
          {examples.map((example, index) => (
            <button
              key={index}
              type="button"
              onClick={() => handleExampleClick(example)}
              disabled={isLoading}
              className="example-btn"
            >
              {example.label}
            </button>
          ))}
        </div>

        {/* Action Buttons */}
        <div className="action-buttons">
          <button
            type="submit"
            disabled={!text.trim() || isLoading}
            className="generate-btn"
          >
            {isLoading ? 'Generating...' : 'Generate Speech'}
          </button>
          <button
            type="button"
            onClick={handleClear}
            disabled={!text || isLoading}
            className="clear-btn"
          >
            Clear
          </button>
        </div>
      </form>
    </div>
  );
};

export default TextInput;
