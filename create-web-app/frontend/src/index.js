import React from 'react';
import ReactDOM from 'react-dom';
import './index.css'; // Importing global styles
import App from './App'; // Importing the main App component
import reportWebVitals from './reportWebVitals'; // Optional: for measuring performance

// Rendering the App component into the root element
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
