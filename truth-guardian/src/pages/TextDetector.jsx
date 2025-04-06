// src/pages/TextDetector.jsx
import React, { useState } from 'react';
import './texts.css';

const TextDetector = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (text.trim().length === 0) {
      setResult('Please enter some text to analyze.');
      return;
    }

    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/analyze_text', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      console.log("Response from API:", data); // helpful for debugging
      setResult(data);
    } catch (error) {
      console.error('Error analyzing text:', error);
      setResult({ verdict: 'Server error. Please try again later.' });
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>📝 Text Misinformation Detector</h1>
      <p style={{ fontSize: '1.1rem', marginBottom: '30px' }}>
        Paste any text below to analyze its authenticity using our AI-powered engine.
      </p>

      <textarea
        rows="10"
        placeholder="Paste the news article, statement, or message here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze'}
      </button>

      {result && typeof result === 'string' ? (
        <div className="result-card">{result}</div>
      ) : result ? (
        <div className="result-card">
          <h2>🔍 Analysis Result</h2>
          <p><strong>Verdict:</strong> {result.verdict}</p>
          <p><strong>Confidence:</strong> {result.confidence}</p>

          {Array.isArray(result.suggestions) && result.suggestions.length > 0 && (
            <>
              <h3>Recommended Actions:</h3>
              <ul>
                {result.suggestions.map((tip, idx) => (
                  <li key={idx}>{tip}</li>
                ))}
              </ul>
            </>
          )}
        </div>
      ) : null}
    </div>
  );
};

export default TextDetector;
