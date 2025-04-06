import { useNavigate, Link } from 'react-router-dom';
import { useState } from 'react';
import logo from '../assets/logo.png'; // Your logo path

import './Auth.css'; // Assuming you're using a shared CSS file

const Login = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();

    // Basic auth logic placeholder
    if (email && password) {
      localStorage.setItem('isAuthenticated', 'true');
      navigate('/home');
    } else {
      alert('Please enter both email and password.');
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        <img src={logo} alt="App Logo" className="auth-logo" />
        <h2>Truth Guardian</h2>
        <form className="auth-form" onSubmit={handleLogin}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Login</button>
          <p>
            Don't have an account? <Link to="/signup">Signup here</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default Login;