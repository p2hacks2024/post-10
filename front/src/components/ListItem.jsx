import { Droplet } from 'lucide-react'
import styles from './ListItem.module.css'
import EmotionGauge from "./EmotionGauge";
import PropTypes from 'prop-types'

ListItem.propTypes = {
  sentence: PropTypes.shape({
    score: PropTypes.number.isRequired,
    text: PropTypes.string.isRequired,
    id: PropTypes.number.isRequired,
    likes: PropTypes.number.isRequired,
  }).isRequired,
  onLike: PropTypes.func.isRequired,
}

export default function ListItem({ sentence, onLike }) {
  return (
    <li className={styles.item}>
      <EmotionGauge score={sentence.score} />
      <div className={styles.content}>
        <p className={styles.text}>{sentence.text}</p>
        <button
          className={styles.likeButton}
          onClick={() => onLike(sentence.id)}
        >
          <Droplet className={styles.dropletIcon} />
          <span>{sentence.likes}</span>
        </button>
      </div>
    </li>
  );
}


