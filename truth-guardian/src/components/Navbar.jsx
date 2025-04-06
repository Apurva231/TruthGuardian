import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../assets/logo.png'; // ✅ Make sure this path is correct
import './Navbar.css';

const Navbar = () => {
  
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <img src={logo} alt="Logo" className="navbar-logo" />
        <h2 className="logo-text">Truth Guardian</h2>
      </div>
      <ul>
        <li><Link to="/home">Home</Link></li>
        <li><Link to="/text">Text Detector</Link></li>
        <li><Link to="/image">Image Detector</Link></li>
        <li><Link to="/audio">Audio Detector</Link></li>
        <li><Link to="/insights">Insights</Link></li>
        <li><Link to="/tools">Tools</Link></li>
        <li><Link to="/about">About</Link></li>
        <li><Link to="/logout" style={{ color: "red" }}>Logout</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;