import { motion } from 'framer-motion';
import  "./WaveFooter.module.css";

const WaveAnimation = ({ color = '#3b82f6', height = 100, speed = 1 }) => {
    return (
      <div className="wave-container">
        <svg
          className="wave-svg"
          height={height}
          viewBox="0 0 1440 100"
          preserveAspectRatio="none"
        >
          <motion.path
            fill={color}
            d="M0,50 C150,20 300,80 450,50 C600,20 750,80 900,50 C1050,20 1200,80 1440,50 V100 H0 V50 Z"
            animate={{
              d: [
                "M0,50 C150,20 300,80 450,50 C600,20 750,80 900,50 C1050,20 1200,80 1440,50 V100 H0 V50 Z",
                "M0,50 C150,80 300,20 450,50 C600,80 750,20 900,50 C1050,80 1200,20 1440,50 V100 H0 V50 Z",
              ],
            }}
            transition={{
              repeat: Infinity,
              repeatType: "reverse",
              duration: 5 / speed,
              ease: "easeInOut",
            }}
          />
        </svg>
      </div>
    );
};
  
export default WaveAnimation;
  
    