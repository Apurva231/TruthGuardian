// src/pages/About.jsx
import React from 'react';
import './About.css';
const About = () => {
  return (
    <div className="App">
      <h1>About Truth Guardian</h1>
      <p style={{ fontSize: '1.2rem', maxWidth: '850px', margin: '0 auto 40px' }}>
        Truth Guardian is a next-gen platform designed to combat the rise of misinformation, deepfakes, and fake news. We harness the power of AI and machine learning to detect and prevent the spread of false content across digital platforms.
      </p>

      {/* Mission */}
      <div className="result-card">
        <h2>🎯 Our Mission</h2>
        <p>
          To create a safer, more informed digital world by empowering users with real-time verification tools for content accuracy and authenticity.
        </p>
      </div>

      {/* Vision */}
      <div className="result-card">
        <h2>🔭 Our Vision</h2>
        <p>
          A future where trust is restored in digital media, where truth prevails over manipulation, and where AI supports transparency in communication.
        </p>
      </div>

      {/* What Makes Us Unique */}
      <div className="result-card">
        <h2>✨ What Makes Us Unique</h2>
        <ul>
        <strong> Multi-modal analysis: Text, Image, Video & Document verification</strong><br></br>
        <strong>  Transparent reporting with source referencing</strong> <br></br>
        <strong> Real-time AI-driven credibility scoring</strong> <br></br>
        <strong> User-first design with accessibility and privacy in mind</strong> <br></br>
        </ul>
      </div>

      {/* Our Team */}
      <div className="result-card">
        <h2>👩‍💻 Meet Our Team</h2>
        <ul>
          <strong>Apurva Amrutkar</strong><br></br>
         <strong>Shafaq Ali</strong> <br></br>
         <strong>Shristi Rajpoot</strong> <br></br>
          <strong>Lakshmi Priya</strong> 
          {/* Add more if needed */}
        </ul>
      </div>

      {/* Footer */}
      <p style={{ marginTop: '60px', fontSize: '0.9rem', color: '#70bfc8' }}>
        Built with dedication to truth, transparency, and trust.
      </p>
    </div>
  );
};

export default About;