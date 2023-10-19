import Head from 'next/head';
import styles from '../styles/Home.module.css';
import gridstyles from '../styles/appgrid.module.css';
import { useState, useEffect } from 'react';

async function getData() {
  const res = await fetch('http://localhost:8000/api/apps')
  // The return value is *not* serialized
  // You can return Date, Map, Set, etc.

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error('Failed to fetch data')
  }

  return res.json()
}

export default function Home() {
  const [data, setData] = useState(null);

  useEffect(() => {
    getData().then(result => {
      setData(result.new_ios);
    });
  }, []);

  var stuff = data
  if (!data) {
    stuff = <div>Loading...</div>; // Render a loading state while the data is being fetched
  }
  else {
    stuff = (
      <div className={gridstyles.appGrid}>
        {data.map(app => (
          <div className={gridstyles.appItem} key={app.id}>
            <a href={app.store_link}>
              <img src={app.icon_url_512} alt={app.name} className={gridstyles.appIcon} />
              <div className={gridstyles.appName}>{app.name}</div>
              {/* You can add a component for the app rating here */}
            </a>
          </div>
        ))}
      </div>
    );
  }


  return (
    <div className='non'>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <div>{stuff}</div>
        <div>hi</div>
        <h1 className={styles.title}>
          to <a href="https://nextjs.org">Next.js!</a>
        </h1>

        <p className={styles.description}>
          Get started by editing <code>pages/index.js</code>
        </p>

        <div className={styles.grid}>
          <a href="https://nextjs.org/docs" className={styles.card}>
            <h3>Documentation &rarr;</h3>
            <p>Find in-depth information about Next.js features and API.</p>
          </a>

          <a href="https://nextjs.org/learn" className={styles.card}>
            <h3>Learn &rarr;</h3>
            <p>Learn about Next.js in an interactive course with quizzes!</p>
          </a>

          <a
            href="https://github.com/vercel/next.js/tree/canary/examples"
            className={styles.card}
          >
            <h3>Examples &rarr;</h3>
            <p>Discover and deploy boilerplate example Next.js projects.</p>
          </a>

          <a
            href="https://vercel.com/import?filter=next.js&utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
          >
            <h3>Deploy &rarr;</h3>
            <p>
              Instantly deploy your Next.js site to a public URL with Vercel.
            </p>
          </a>
        </div>
      </main>

      <footer>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <img src="/vercel.svg" alt="Vercel" className={styles.logo} />
        </a>
      </footer>

    </div>
  );
}

