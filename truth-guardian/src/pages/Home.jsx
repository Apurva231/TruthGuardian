import React from 'react';
import Hero from '../components/Hero';
import './Home.css';
import { useNavigate } from 'react-router-dom';
const Home = () => {
    const navigate = useNavigate();
  return (
    <>
      <Hero />
      <section className="stats">
        <h2>Trusted by Thousands</h2>
        <div className="stat-grid">
          <div>
            <h3>10K+</h3>
            <p>Fake News Articles Analyzed</p>
          </div>
          <div>
            <h3>95%</h3>
            <p>Detection Accuracy</p>
          </div>
          <div>
            <h3>500+</h3>
            <p>Daily Active Users</p>
          </div>
        </div>
      </section>

      <section className="how-it-works">
        <h2>How It Works</h2>
        <ol>
          <li>Paste or upload your content</li>
          <li>AI scans for misinformation using NLP + ML</li>
          <li>Instant report with credibility score</li>
        </ol>
      </section>

      <section className="features">
        <h2>What Truth Guardian Offers</h2>
        <div className="features-grid">
          <div>
            <h4>Text Analysis</h4>
            <p>Paste any text and detect potential fake news or bias.</p>
          </div>
          <div>
            <h4>Image Forensics</h4>
            <p>Upload an image and uncover AI-generated or deepfake content.</p>
          </div>
          <div>
            <h4>Voice Verification</h4>
            <p>Analyze audio clips for manipulation or fake narration.</p>
          </div>
          <div>
            <h4>Fact-Check Dashboard</h4>
            <p>Live statistics, sources, and detection breakdown in real-time.</p>
          </div>
        </div>
      </section>

      <section className="testimonials">
        <h2>What Users Say</h2>
        <div className="testimonial-grid">
          <blockquote>
            "Truth Guardian saved my research project by identifying a fake source in seconds!"
            <cite>– Aarav T., Journalist</cite>
          </blockquote>
          <blockquote>
            "Finally, a tool that gives me peace of mind before sharing news on WhatsApp."
            <cite>– Shruti M., College Student</cite>
          </blockquote>
        </div>
      </section>

      <section className="cta">
        <h2>Ready to Uncover the Truth?</h2>
        <p>Use Truth Guardian now to verify content before it goes viral.</p>
        <button onClick={() => navigate('/text')}>Start Detecting</button>
      </section>
    </>
  );
};

export default Home;