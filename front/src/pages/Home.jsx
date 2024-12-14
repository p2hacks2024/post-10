import { useEffect, useState } from 'react';
import List from '../components/List';
import Loading from '../components/Loading';
import styles from './Home.module.css';
import { fetchMessages, incermentFlush } from '../repository/api';

export default function Home() {
  const [sentences, setSentences] = useState([]);
  const [isRanking, setIsRanking] = useState(false); // 現在のタブ状態

  useEffect(() => {
    fetchMessages().then((data) => setSentences(data));
  }, []);

  const handleLike = (id) => {
    incermentFlush(id);
    setSentences(
      sentences.map((sentence) =>
        sentence.id === id ? { ...sentence, likes: sentence.likes + 1 } : sentence
      )
    );
  };

  // 表示するデータを切り替える
  const displayedSentences = isRanking
    ? [...sentences].sort((a, b) => b.likes - a.likes) // ランキング順
    : sentences; // 新着順

  return (
    <main className={styles.main}>
      {/* タブ部分 */}
      <div className={styles.tabs}>
        <button
          className={`${styles.tab} ${!isRanking ? styles.active : ''}`}
          onClick={() => setIsRanking(false)}
        >
          タイムライン
        </button>
        <button
          className={`${styles.tab} ${isRanking ? styles.active : ''}`}
          onClick={() => setIsRanking(true)}
        >
          ランキング
        </button>
      </div>
      <Loading isLoading={sentences.length === 0} />
      <List sentences={displayedSentences} onLike={handleLike} />
    </main>
  );
}