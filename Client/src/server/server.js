import express from 'express';
import React from 'react';
import ReactDOMServer from 'react-dom/server';
import App from '../components/Content/App';


const server = express();
server.use(express.static('dist'));
server.use('images', express.static('../images'));

server.get('/', (req, res) => {
  const initialMarkup = ReactDOMServer.renderToString(<App />);
  res.send(`
    <!doctype html>
    <html lang="en">
      <head>
        <title>SearchMyShow</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      </head>      
      <body id="mountNode">
        ${initialMarkup}
        <script src="/main.js"></script>
      </body>
    </html>
  `)
});

server.listen(4242, () => console.log('Server is running...'));