import React from 'react';
import { useNavigate, Link } from 'react-router-dom';
import logo from '../assets/logo.png'; // ✅ Correct import
import './Auth.css'; // reuse the same styles

const Signup = () => {
  const navigate = useNavigate();

  const handleSignup = (e) => {
    e.preventDefault();
    // Add actual signup logic later
    navigate('/home'); // Redirect after successful signup
  };

  return (
    <div className="auth-container">
      <div className="auth-header">
        <img src={logo} alt="App Logo" className="auth-logo" />
        <h1 className="auth-title">Truth Guardian</h1>
          </div>

      <form className="auth-form" onSubmit={handleSignup}>
        <input type="text" placeholder="Full Name" required />
        <input type="email" placeholder="Email" required />
        <input type="password" placeholder="Password" required />
        <input type="password" placeholder="Confirm Password" required />
        <button type="submit">Sign Up</button>
        <p>
          Already have an account? <Link to="/login">Login here</Link>
        </p>
      </form>
    </div>
  );
};

export default Signup;