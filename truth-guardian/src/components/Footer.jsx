import React from 'react';

const Footer = () => {
  return (
    <footer style={{
      textAlign: 'center',
      padding: '1rem',
      background: '#1f1f1f',
      color: 'white',
      marginTop: '2rem'
    }}>
      &copy; {new Date().getFullYear()} Truth Guardian. All rights reserved.
    </footer>
  );
};

export default Footer;
