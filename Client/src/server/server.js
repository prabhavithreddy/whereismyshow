import express from 'express';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from '../components/Content/App';
import Header from '../components/Header/Header';


const server = express();
server.use(express.static('dist'));
server.use('images', express.static('../images'));

server.get('/', (req, res) => {
  const initialMarkup = ReactDOMServer.renderToString(<App />);
  const headerMarkup = ReactDOMServer.renderToString(<Header />)
  res.send(`
    <html>
      <head>
        <title>SearchMyShow</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
      </head>      
      <body>
        <header>${headerMarkup}</header>
        <section>
          <div id="mountNode">${initialMarkup}</div>
        </section>
        <script src="/main.js"></script>
        <aside>Aside</aside>
        <footer>Footer</footer>
      </body>
    </html>
  `)
});

server.listen(4242, () => console.log('Server is running...'));