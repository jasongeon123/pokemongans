import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})
  useEffect(()=>{
    axios.get('http://localhost:5000/flask/hello').then(response => {
      setGetMessage(response);
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <form action = "/action_page.php">
          <select name = "types" id = "types">
            <option value="bug">Bug</option>
            <option value="dark">Dark</option>
            <option value="dark">Dragon</option>
            <option value="dark">Electric</option>
            <option value="dark">Fairy</option>
            <option value="dark">Fighting</option>
            <option value="dark">Fire</option>
            <option value="dark">Flying</option>
            <option value="dark">Ghost</option>
            <option value="dark">Grass</option>
            <option value="dark">Ground</option>
            <option value="dark">Ice</option>
            <option value="dark">Normal</option>
            <option value="dark">Poison</option>
            <option value="dark">Psychic</option>
            <option value="dark">Rock</option>
            <option value="dark">Steel</option>
            <option value="dark">Water</option>
          </select>
          <select name = "types" id = "types">
            <option value="bug">Bug</option>
            <option value="dark">Dark</option>
            <option value="dark">Dragon</option>
            <option value="dark">Electric</option>
            <option value="dark">Fairy</option>
            <option value="dark">Fighting</option>
            <option value="dark">Fire</option>
            <option value="dark">Flying</option>
            <option value="dark">Ghost</option>
            <option value="dark">Grass</option>
            <option value="dark">Ground</option>
            <option value="dark">Ice</option>
            <option value="dark">Normal</option>
            <option value="dark">Poison</option>
            <option value="dark">Psychic</option>
            <option value="dark">Rock</option>
            <option value="dark">Steel</option>
            <option value="dark">Water</option>
          </select>
          <input type="submit" value="Submit"></input>
        </form>
      </header>
        <div>{getMessage.status === 200 ? 
          <h3>{getMessage.data.message}</h3>
          :
          <h3>LOADING</h3>}</div>
    </div>
  );
}

export default App;
