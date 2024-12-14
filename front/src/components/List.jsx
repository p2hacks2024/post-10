import ListItem from './ListItem'
import styles from './List.module.css'
<<<<<<< HEAD
=======
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

>>>>>>> 07e3838a930f7bf302c94caca5fc9f129c7a654e

export default function List({ sentences, onLike }) {
  return (
    <ul className={styles.list}>
      {sentences.map(sentence => (
        <ListItem key={sentence.id} sentence={sentence} onLike={onLike} />
      ))}
    </ul>
  )
}
