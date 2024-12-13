import React, { useState } from 'react';
import './Splash.css';

const Splash = ({ onEnd }) => {
  const [isFlushing, setIsFlushing] = useState(false);
  const [toiletImage, setToiletImage] = useState('toilet.png'); // 初期トイレ画像

  const handleTap = () => {
    setToiletImage('toilet_anime.png'); // 水が流れる画像に差し替え
    setIsFlushing(true); // 水流アニメーションを開始
    setTimeout(() => {
      onEnd(); // アニメーション終了後に画面遷移
    }, 3000); // アニメーションの長さに合わせる
  };

  return (
    <div className={`splash-container ${isFlushing ? 'flushing' : ''}`}>
      <div className="toilet" onClick={handleTap}>
        <p className="tap-instruction">トイレを流せ！！！</p>
        <img
          src={toiletImage} // 状態によって画像を切り替える
          alt="Toilet"
          className="toilet-image"
        />
      </div>
      {isFlushing && <div className="water-animation"></div>}
    </div>
  );
};

export default Splash;
