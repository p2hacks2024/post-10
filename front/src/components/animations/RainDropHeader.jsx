import React from 'react';
import { motion } from 'framer-motion';

const RainDropHeader = ({ height = 200 }) => {
  const raindrops = Array.from({ length: 20 }, (_, i) => ({
    id: i,
    x: Math.random() * 100,
    delay: Math.random() * 2,
    duration: 1 + Math.random() * 2
  }));

  return (
    <div style={{ height, overflow: 'hidden', position: 'relative', background: 'linear-gradient(180deg, #4a90e2 0%, #5ca0ea 100%)' }}>
      <svg width="100%" height={height} style={{ position: 'absolute', top: 0, left: 0 }}>
        {raindrops.map((drop) => (
          <React.Fragment key={drop.id}>
            <motion.circle
              cx={`${drop.x}%`}
              cy="0"
              r="2"
              fill="#ffffff"
              initial={{ y: -10 }}
              animate={{ y: height }}
              transition={{
                duration: drop.duration,
                repeat: Infinity,
                delay: drop.delay,
                ease: 'linear'
              }}
            />
            <motion.circle
              cx={`${drop.x}%`}
              cy={height}
              r="0"
              stroke="#ffffff"
              strokeWidth="1"
              fill="none"
              initial={{ r: 0 }}
              animate={{ r: 20, opacity: [1, 0] }}
              transition={{
                duration: 1,
                repeat: Infinity,
                delay: drop.delay + drop.duration,
                ease: 'easeOut'
              }}
            />
          </React.Fragment>
        ))}
      </svg>
      <div style={{ position: 'relative', zIndex: 1, height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <h1 style={{ color: 'white', fontSize: '2rem', textShadow: '2px 2px 4px rgba(0,0,0,0.5)' }}></h1>
      </div>
    </div>
  );
};

export default RainDropHeader;