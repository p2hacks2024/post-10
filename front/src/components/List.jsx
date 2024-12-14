import ListItem from './ListItem'
import styles from './List.module.css'
import PropTypes from 'prop-types'

List.propTypes = [{
  sentence: PropTypes.shape({
    score: PropTypes.number.isRequired,
    text: PropTypes.string.isRequired,
    id: PropTypes.number.isRequired,
    likes: PropTypes.number.isRequired,
  }).isRequired,
  onLike: PropTypes.func.isRequired,
}]


export default function List({ sentences, onLike }) {
  return (
    <ul className={styles.list}>
      {sentences.map(sentence => (
        <ListItem key={sentence.id} sentence={sentence} onLike={onLike} />
      ))}
    </ul>
  )
}
