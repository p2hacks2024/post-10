import { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import './Splash.css';
import BubbleAnimation from '../components/splash/BubbleAnimation';
import MessageFall from '../components/splash/MessageFall';

const Splash = ({ onEnd }) => {
  const [isFlushing, setIsFlushing] = useState(false);

  useEffect(() => {
    setTimeout(() => {
      onReadyToStart();
    }
      , 4000);
  }, []);

  const onReadyToStart = () => {
    const tapInstruction = document.querySelector('.tap-instruction');

    tapInstruction.classList.add('ready');
  }

  const handleTap = () => {
    setIsFlushing(true);
    setTimeout(() => {
      onEnd(); // アニメーション終了後に画面遷移
    }, 2000); // アニメーションの長さに合わせる
  };

  return (
    <div className={`splash-container ${isFlushing ? 'flushing' : ''}`}>
      <BubbleAnimation />
      <MessageFall />
      <div className={`tap-erea ${isFlushing ? 'page-transition' : ''}`} onClick={handleTap}>
        <p className={`tap-instruction ${isFlushing ? 'page-transition' : ''}`}>Tap to Start</p>
      </div>
    </div>
  );
};

Splash.propTypes = {
  onEnd: PropTypes.func.isRequired,
};

export default Splash;
