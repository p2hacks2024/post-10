import ListItem from './ListItem'
import styles from './List.module.css'

export default function List({ sentences, onLike }) {
  return (
    <ul className={styles.list}>
      {sentences.map(sentence => (
        <ListItem key={sentence.id} sentence={sentence} onLike={onLike} />
      ))}
    </ul>
  )
}
