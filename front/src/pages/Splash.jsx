import { useState } from 'react';
import contents from '../constant/splash_content';
import './Splash.css';
import BubbleAnimation from '../components/BubbleAnimation';

const Splash = ({ onEnd }) => {
  const [isFlushing, setIsFlushing] = useState(false);
  const [toiletImage, setToiletImage] = useState('illustkun.png'); // 初期トイレ画像

  const handleTap = () => {
    setToiletImage('toiletwater.png'); // 水が流れる画像に差し替え
    setIsFlushing(true); // 水流アニメーションを開始
    setTimeout(() => {
      onEnd(); // アニメーション終了後に画面遷移
    }, 3000); // アニメーションの長さに合わせる
  };

  return (
    <div className={`splash-container ${isFlushing ? 'flushing' : ''}`}>
      <BubbleAnimation />
      <div className="toilet" onClick={handleTap}>
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
      </div>
      {isFlushing && <div className="water-animation"></div>}
    </div>
  );
};

export default Splash;
