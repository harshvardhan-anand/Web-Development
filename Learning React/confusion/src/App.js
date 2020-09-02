import React from 'react';
import logo from './logo.svg';
import './App.css';

// className is used for general class in html. 
// Since we are writing in js file so "class" can confuse js with keyword class.
// elements combine to create a component.

function App() {
  return (
    // these div, headers... are "elements" of react not HTML tags.
    // Technically they are JSX is JavaScript XML. 
    // JSX allows us to write HTML in React
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
