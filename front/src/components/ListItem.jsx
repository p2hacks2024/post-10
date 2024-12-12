import { Heart } from 'lucide-react'
import styles from './ListItem.module.css'

export default function ListItem({ sentence, onLike }) {
  return (
    <li className={styles.item}>
      <div className={styles.score}>{sentence.score.toFixed(1)}</div>
      <div className={styles.content}>
        <p>{sentence.text}</p>
        <button className={styles.likeButton} onClick={() => onLike(sentence.id)}>
          <Heart className={styles.heartIcon} />
          <span>{sentence.likes}</span>
        </button>
      </div>
    </li>
  )
}