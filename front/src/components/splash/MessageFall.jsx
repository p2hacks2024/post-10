import { useEffect } from 'react';
import './MessageFall.css';
import { miniMessages } from '../../constant/splash_content'; 

const MessageFall = () => {

    useEffect(() => {
        const messageContainer = document.querySelector('.message-container');
        const messages = document.querySelectorAll('.message');

        messages.forEach(message => {
            const random = Math.random() * 100;
            const duration = Math.random() * 20 + 5;
            const delay = Math.random() * 50;
            const size = Math.random() * 1 + 0.5;

            message.style.left = `${random - 50}%` ;
            message.style.animationDuration = `${duration}s`;
            message.style.animationDelay = `${delay}s`;
            message.style.fontSize = `${size}rem`;
        });

        messageContainer.style.opacity = 1;
    }, []);
    
    return (
        <div className="message-container">
        {miniMessages.map((message, index) => (
            <p
            key={index}
            className="message"
            >
            {message}
            </p>
        ))}
        </div>
    );
};

export default MessageFall;
