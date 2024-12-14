import { useState } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import './index.css';
import Home from './pages/Home.jsx';
import Splash from './pages/Splash.jsx';

const App = () => (
  <Router>
    <Routes>
      {/* Splash ページ */}
      <Route
        path="/"
        element={
          <SplashWrapper />
        }
      />
      {/* Home ページ */}
      <Route path="/home" element={<Home />} />
    </Routes>
  </Router>
);

const SplashWrapper = () => {
  const navigate = useNavigate();

  const handleSplashEnd = () => {
    navigate("/home"); // Home ページに遷移
  };

  return <Splash onEnd={handleSplashEnd} />;
};

createRoot(document.getElementById('root')).render(<App />);