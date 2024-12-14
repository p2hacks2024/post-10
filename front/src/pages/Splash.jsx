import { useState } from 'react';
import './Splash.css';
import BubbleAnimation from '../components/splash/BubbleAnimation';
import MessageFall from '../components/splash/MessageFall';

const Splash = ({ onEnd }) => {
  const [isFlushing, setIsFlushing] = useState(false);

  const handleTap = () => {
    setIsFlushing(true); // 水流アニメーションを開始
    setTimeout(() => {
      onEnd(); // アニメーション終了後に画面遷移
    }, 3000); // アニメーションの長さに合わせる
  };

  return (
    <div className={`splash-container ${isFlushing ? 'flushing' : ''}`}>
      <BubbleAnimation />
      <MessageFall />
      {/* <div className="toilet" onClick={handleTap}>
        <p className="tap-instruction">Tap to flush!!!</p>
        <div className="toilet-text">
          {contents.map((content, index) => (
            <p
              key={index}
              className="toilet-text-content floating-text"
              style={{
                animationDelay: `${Math.random() * 5}s`,
                left: `${Math.random() * 100}%`
              }}
            >
              {content}
            </p>
          ))}
        </div>
      </div> */}
      {isFlushing && <div className="water-animation"></div>}
    </div>
  );
};

export default Splash;
