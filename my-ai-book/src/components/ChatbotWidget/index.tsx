import React, {useMemo, useState} from 'react';
import {useLocation} from '@docusaurus/router';

import styles from './styles.module.css';

type ChatMessage = {
  from: 'user' | 'bot';
  text: string;
};

export default function ChatbotWidget(): JSX.Element {
  const [isOpen, setIsOpen] = useState(false);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const location = useLocation();

  const currentTopic = useMemo(() => {
    // Derive a simple "chapter title" from the URL path
    const path = location.pathname;
    if (path.startsWith('/docs/')) {
      const parts = path.split('/').filter(Boolean);
      const last = parts[parts.length - 1] ?? 'this chapter';
      return last.replace(/[-_]/g, ' ');
    }
    if (path === '/' || path.startsWith('/blog')) {
      return 'the AI textbook';
    }
    return 'this page';
  }, [location.pathname]);

  const placeholderText = `Ask me about ${currentTopic}…`;

  const toggleOpen = () => setIsOpen((prev) => !prev);

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userText = input.trim();
    setInput('');
    setMessages((prev) => [...prev, {from: 'user', text: userText}]);
    setIsLoading(true);

    try {
      const res = await fetch('http://127.0.0.1:8000/api/rag/query', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: userText}),
      });

      if (!res.ok) {
        throw new Error(`Backend error: ${res.status}`);
      }

      const data = await res.json();
      const answer: string = data.answer ?? 'No answer returned from backend.';

      setMessages((prev) => [...prev, {from: 'bot', text: answer}]);
    } catch (err: unknown) {
      const msg =
        err instanceof Error ? err.message : 'Unknown error contacting backend.';
      setMessages((prev) => [
        ...prev,
        {
          from: 'bot',
          text: `Error talking to backend: ${msg}`,
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown: React.KeyboardEventHandler<HTMLInputElement> = (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      void sendMessage();
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      {isOpen && (
        <div className={styles.chatPanel}>
          <div className={styles.chatHeader}>
            <span>Textbook Chatbot</span>
            <button
              type="button"
              className={styles.closeButton}
              onClick={toggleOpen}>
              ✕
            </button>
          </div>
          <div className={styles.chatMessages}>
            {messages.length === 0 ? (
              <div className={styles.placeholder}>
                Ask a question about the textbook content.
              </div>
            ) : (
              messages.map((m, idx) => (
                <div
                  key={idx}
                  className={
                    m.from === 'user'
                      ? styles.messageUser
                      : styles.messageBot
                  }>
                  {m.text}
                </div>
              ))
            )}
          </div>
          <div className={styles.chatInputRow}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              className={styles.chatInput}
              placeholder={placeholderText}
              disabled={isLoading}
            />
            <button
              type="button"
              className={styles.sendButton}
              onClick={() => void sendMessage()}
              disabled={isLoading || !input.trim()}>
              {isLoading ? '...' : 'Send'}
            </button>
          </div>
        </div>
      )}

      <button
        type="button"
        className={styles.fab}
        onClick={toggleOpen}
        aria-label="Open chatbot">
        💬
      </button>
    </div>
  );
}

