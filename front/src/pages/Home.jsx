import { useEffect, useState } from 'react'
import List from '../components/List'
import styles from './Home.module.css'
import { fetchMessages, incermentFlush } from '../repository/api'

export default function Home() {
  const [sentences, setSentences] = useState([])

  useEffect(() => {
    fetchMessages().then(data => setSentences(data))
  }, [])

  const handleLike = (id) => {
    incermentFlush(id);
    setSentences(sentences.map(sentence => 
        sentence.id === id ? { ...sentence, likes: sentence.likes + 1 } : sentence
      ))
  }

  return (
    <main className={styles.main}>
      <h1 className={styles.title}>Sentence Rater</h1>
      <List sentences={sentences} onLike={handleLike} />
    </main>
  )
}
