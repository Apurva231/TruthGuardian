// src/pages/AudioDetector.jsx
import React, { useState } from 'react';

const AudioDetector = () => {
  const [selectedAudio, setSelectedAudio] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setSelectedAudio(e.target.files[0]);
    setResult(null);
    setError('');
  };

  const handleSubmit = async () => {
    if (!selectedAudio) {
      setError('Please upload an audio file first.');
      return;
    }

    const formData = new FormData();
    formData.append('audio', selectedAudio);

    setIsLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch('http://localhost:8000/api/audio-detect', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Server error. Please try again.');

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || 'Something went wrong!');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Audio Fake News Detection</h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '30px' }}>
        Upload an audio file to check for manipulated or fake speech content.
      </p>

      <input type="file" accept="audio/*" onChange={handleFileChange} />
      <br />
      <button onClick={handleSubmit}>
        {isLoading ? 'Analyzing...' : 'Detect Fake Audio'}
      </button>

      {error && (
        <div className="result-card" style={{ borderLeftColor: '#ff4d4f' }}>
          <h2>Error</h2>
          <p>{error}</p>
        </div>
      )}

      {result && (
        <div className="result-card">
          <h2>🧠 Analysis Result</h2>
          <p><strong>Authenticity Score:</strong> {result.score}%</p>
          <p><strong>Detected Label:</strong> {result.label}</p>
          {result.notes && (
            <>
              <h3>Details:</h3>
              <ul>
                {result.notes.map((note, idx) => (
                  <li key={idx}>{note}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default AudioDetector;