'use client'

import { useState } from 'react'
import List from './components/List'
import styles from './page.module.css'

export default function Home() {
  const [sentences, setSentences] = useState([
    { id: 1, text: "The quick brown fox jumps over the lazy dog.", score: 7.5, likes: 0 },
    { id: 2, text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", score: 6.8, likes: 0 },
    { id: 3, text: "To be or not to be, that is the question.", score: 9.2, likes: 0 },
    { id: 4, text: "All that glitters is not gold.", score: 8.5, likes: 0 },
    { id: 5, text: "A journey of a thousand miles begins with a single step.", score: 7.9, likes: 0 },
  ])

  const handleLike = (id) => {
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
