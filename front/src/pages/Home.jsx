import { useEffect, useState } from 'react'
import List from '../components/List'
import Loading from '../components/Loading'
import styles from './Home.module.css'
import { fetchMessages, incermentFlush } from '../repository/api'

export default function Home() {
  const [sentences, setSentences] = useState([]);
  const [isRanking, setIsRanking] = useState(false); // ランキング表示状態

  useEffect(() => {
    fetchMessages().then(data => setSentences(data));
  }, []);

  const handleLike = (id) => {
    incermentFlush(id);
    setSentences(sentences.map(sentence => 
      sentence.id === id ? { ...sentence, likes: sentence.likes + 1 } : sentence
    ));
  };

  const toggleRanking = () => {
    setIsRanking(!isRanking); // 表示状態を切り替え
  };

  // ソートされたリストを生成
  const displayedSentences = isRanking
    ? [...sentences].sort((a, b) => b.likes - a.likes) // likesで降順ソート
    : sentences;

  return (
    <main className={styles.main}>
      <h1 className={styles.title} onClick={toggleRanking}>
        {isRanking ? 'ランキング' : 'しんちゃく'}
      </h1>
      <Loading isLoading={sentences.length === 0} />
      <List sentences={displayedSentences} onLike={handleLike} />
    </main>
  );
}