import React from "react";
import { Heart, HeartCrack } from "lucide-react";
import PropTypes from "prop-types";
import "./EmotionGauge.css";

export default function EmotionGauge({ score, size = 60 }) {
  // スコアを0～100の割合に変換
  const percentage = Math.min(Math.max((score / 10) * 100, 0), 100);

  return (
    <div
      className="emotion-gauge"
      style={{ width: `${size}px`, height: `${size * 2}px` }}
    >
      {/* 上のHeartアイコン */}
      <Heart
        className="icon heart-icon"
        style={{ fontSize: `${size * 0.6}px` }}
      />
      {/* ゲージ部分 */}
      <div
        className="gauge"
        style={{
          width: `${size * 0.4}px`,
          height: `${size}px`,
        }}
      >
        {/* 赤い部分 */}
        <div
          className="gauge-red"
          style={{
            height: `${100 - percentage}%`,
          }}
        ></div>
        {/* 青い部分 */}
        <div
          className="gauge-blue"
          style={{
            height: `${percentage}%`,
          }}
        ></div>
        {/* 境界線 */}
        <div
          className="gauge-divider"
          style={{
            bottom: `${percentage}%`,
          }}
        ></div>
      </div>
      {/* 下のHeartCrackアイコン */}
      <HeartCrack
        className="icon heart-crack-icon"
        style={{ fontSize: `${size * 0.6}px` }}
      />
    </div>
  );
}

EmotionGauge.propTypes = {
  score: PropTypes.number.isRequired, // スコア (0～10)
  size: PropTypes.number, // サイズ (デフォルト: 50)
};
