// src/pages/ImageDetector.jsx
import React, { useState } from 'react';
import './Image.css';
const ImageDetector = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [previewURL, setPreviewURL] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
    setPreviewURL(URL.createObjectURL(file));
    setResult(null);
    setError('');
  };

//   const handleSubmit = async () => {
//     if (!selectedImage) {
//       setError('Please upload an image first.');
//       return;
//     }

//     const formData = new FormData();
//     formData.append('image', selectedImage);

//     setIsLoading(true);
//     setError('');
//     setResult(null);

//     try {
//       const response = await fetch('http://localhost:8000/api/image-detect', {
//         method: 'POST',
//         body: formData,
//       });

//       if (!response.ok) throw new Error('Server error. Please try again.');

//       const data = await response.json();
//       setResult(data);
//     } catch (err) {
//       setError(err.message || 'Something went wrong!');
//     } finally {
//       setIsLoading(false);
//     }
//   };

//   return (
//     <div className="App">
//       <h1>Image Fake News Detection</h1>
//       <p style={{ fontSize: '1.2rem', marginBottom: '30px' }}>
//         Upload an image suspected of manipulation or misinformation.
//       </p>

//       <input type="file" accept="image/*" onChange={handleFileChange} />
//       <br />

//       {previewURL && (
//         <div style={{ marginTop: '20px' }}>
//           <img
//             src={previewURL}
//             alt="Preview"
//             style={{
//               maxWidth: '80%',
//               maxHeight: '300px',
//               marginBottom: '20px',
//               borderRadius: '12px',
//               boxShadow: '0 0 10px rgba(15, 164, 175, 0.3)',
//             }}
//           />
//         </div>
//       )}

const handleSubmit = async () => {
    if (!selectedImage) {
      setError('Please upload an image first.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file', selectedImage); // ✅ match backend
  
    setIsLoading(true);
    setError('');
    setResult(null);
  
    try {
      const response = await fetch('http://localhost:8000/api/image-detect', {
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
      <h1>Image Fake News Detection</h1>
      <p style={{ fontSize: '1.2rem', marginBottom: '30px' }}>
        Upload an image suspected of manipulation or misinformation.
      </p>

      <input type="file" accept="image/*" onChange={handleFileChange} />
      <br />

      {previewURL && (
        <div style={{ marginTop: '20px' }}>
          <img
            src={previewURL}
            alt="Preview"
            style={{
              maxWidth: '80%',
              maxHeight: '300px',
              marginBottom: '20px',
              borderRadius: '12px',
              boxShadow: '0 0 10px rgba(15, 164, 175, 0.3)',
            }}
          />
        </div>
      )}

      <button onClick={handleSubmit}>
        {isLoading ? 'Analyzing Image...' : 'Detect Fake Image'}
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

export default ImageDetector;