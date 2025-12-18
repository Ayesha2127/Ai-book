import React from 'react';
import styles from './styles.module.css';

export default function HomepageHero() {
  return (
    <section className={styles.hero}>
      <div className="container text-center">
        <h1 className={styles.heroTitle}>Your AI-Powered Learning Companion</h1>
        <p className={styles.heroSubtitle}>
          Dive into chapters, ask questions, and get instant AI explanations. Learn smarter, not harder.
        </p>
        <div className="mt-6 flex justify-center gap-4 flex-wrap">
          <a href="/docs/Introduction/Foundations-Hardware" className={styles.ctaButton}>Start Reading</a>
          <a href="/docs/Introduction" className={styles.ctaButtonOutline}>Ask AI</a>
        </div>
        {/* Agentic AI Illustration */}
        <img
        src={"/img/agentic_ai.png"}
        alt="Agentic AI Illustration"
        className={styles.heroImage}
/>
      </div>
    </section>
  );
}
