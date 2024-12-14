import { useEffect, useState } from 'react';
import './BubbleAnimation.scss';

const BubbleAnimation = () => {
  const [bubbles, setBubbles] = useState([]);

  useEffect(() => {
    const items = 30; // Number of bubbles
    const newBubbles = [];

    for (let i = 0; i < items; i++) {
      const moveVal = Math.ceil(Math.random() * 50);
      const posVal = Math.ceil(Math.random() * 50);
      const scaleVal = Math.ceil(Math.random() * 10);
      const shakeVal = Math.ceil(Math.random() * 5);

      newBubbles.push({
        move: `move${moveVal}`,
        pos: `pos${posVal}`,
        scale: `scale${scaleVal}`,
        shake: `shake${shakeVal}`
      });
    }

    setBubbles(newBubbles);
  }, []);

  return (
    <div className="field">
      {bubbles.map((bubble, index) => (
        <div key={index} className={`${bubble.move} ${bubble.pos}`}>
          <div className={`${bubble.scale}`}>
            <div className={`item ${bubble.shake}`}></div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default BubbleAnimation;
