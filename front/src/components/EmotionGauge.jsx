import React from "react";
import { Heart, HeartCrack } from "lucide-react";
import PropTypes from "prop-types";
import "./EmotionGauge.css";

export default function EmotionGauge({ score }) {
    // スコアを 0～100 の割合に変換
    const percentage = Math.min(Math.max((score / 10) * 100, 0), 100);
  
    return (
      <div className="gauge-container">
        {/* 上のHeartアイコン */}
        <Heart className="icon heart-icon" />
        {/* ゲージ部分 */}
        <div className="gauge">
          {/* 赤の部分 */}
          <div
            className="gauge-red"
            style={{
              height: `${100 - percentage}%`,
            }}
          ></div>
          {/* 青の部分 */}
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
        <HeartCrack className="icon heart-crack-icon" />
      </div>
    );
  }
  
  EmotionGauge.propTypes = {
    score: PropTypes.number.isRequired, // スコア (0～10)
  };