import React from 'react';
import { useNavigate } from 'react-router-dom'; 
import './Hero.css';

const Hero = () => {
    const navigate = useNavigate();
  return (
    <div className="hero">
      <h1>Truth Guardian</h1>
      <p>Uncover the truth behind the content you consume.</p>
      <button onClick={() => navigate('/tools')}>Get Started</button>
    </div>
  );
};

export default Hero;