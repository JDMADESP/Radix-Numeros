import React, { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Form from './Form.jsx'
import axios from 'axios'

///npm run dev for Vite React front end
///flask run for Flask backend

function App() {


  //Loads the website, sets up the tree
  const fetchAPI = async() => {
    const response = await axios.get("http://127.0.0.1:5000");
    console.log(response.data);
  };
  useEffect(() => {
    fetchAPI()
  }, [])
  return (
    <>
      <div className="TitleAndForm">
        <header className="Title">
          <h1>React Search Tree</h1>
        </header>
        <Form />
      </div>
    </>
  )
}

export default App
