import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import Home from './pages/Home.jsx';
import Splash from './pages/Splash.jsx';

const App = () => {
  const [isSplashVisible, setIsSplashVisible] = useState(true);

  const handleSplashEnd = () => {
    setIsSplashVisible(false);
  };

  return (
    <div>
      {isSplashVisible ? <Splash onEnd={handleSplashEnd} /> : <Home />}
    </div>
  );
};

createRoot(document.getElementById('root')).render(<App />);
