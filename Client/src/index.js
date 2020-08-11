import React from 'react';
import ReactDOM from 'react-dom';

import App from './components/Content/App';
import './css/core.css';
import './css/css-grid.css';
import 'bootstrap/dist/css/bootstrap.min.css';

ReactDOM.hydrate(
  <App />,
  document.getElementById('mountNode'),
);