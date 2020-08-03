import express from 'express';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from '../components/App';

const server = express();
server.use(express.static('dist'));

server.get('/', (req, res) => {
  const initialMarkup = ReactDOMServer.renderToString(<App />);

  res.send(`
    <html>
      <head>
        <title>Sample React App</title>
      </head>      
      <body>
        <header>Header</header>
        <section>
          <nav></nav>        
          <div id="mountNode">${initialMarkup}</div>
        </section>
        <script src="/main.js"></script>
        <footer>Footer</footer>
      </body>
    </html>
  `)
});

server.listen(4242, () => console.log('Server is running...'));