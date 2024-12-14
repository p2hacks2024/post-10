import React, { useState } from "react";
import PropTypes from "prop-types";
import { Droplet } from "lucide-react";
import EmotionGauge from "./EmotionGauge";
import styles from "./ListItem.module.css";

ListItem.propTypes = {
  sentence: PropTypes.shape({
    score: PropTypes.number.isRequired,
    text: PropTypes.string.isRequired,
    id: PropTypes.number.isRequired,
    likes: PropTypes.number.isRequired,
  }).isRequired,
  onLike: PropTypes.func.isRequired,
};

export default function ListItem({ sentence, onLike }) {
  const [isWaving, setIsWaving] = useState(false);

  const handleLike = (id) => {
    setIsWaving(true); // 波打つアニメーションを開始
    setTimeout(() => setIsWaving(false), 500); // アニメーション終了後リセット
    onLike(id);
  };

  return (
    <li className={styles.item}>
      <EmotionGauge score={sentence.score} />
      <div className={styles.content}>
        <p className={styles.text}>{sentence.text}</p>
        <button
          className={`${styles.likeButton} ${isWaving ? styles.waving : ""}`}
          onClick={() => handleLike(sentence.id)}
        >
          <Droplet className={styles.dropletIcon} />
          <span>{sentence.likes}</span>
        </button>
      </div>
    </li>
  );
}

