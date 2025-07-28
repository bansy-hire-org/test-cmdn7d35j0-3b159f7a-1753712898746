import React, { useState, useEffect } from 'react';
import './App.css';

const API_KEY = 'supersecretkey';
const API_URL = 'http://localhost:8000';

function App() {
  const [chargingStations, setChargingStations] = useState([]);
  const [route, setRoute] = useState(null);

  useEffect(() => {
    async function fetchChargingStations() {
      const response = await fetch(`${API_URL}/charging_stations`, {
        headers: { 'api_key': API_KEY },
      });
      const data = await response.json();
      setChargingStations(data);
    }

    fetchChargingStations();
  }, []);

  const handleOptimizeRoute = async () => {
    const response = await fetch(`${API_URL}/optimize_route`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'api_key': API_KEY,
      },
      body: JSON.stringify({ start: 'Depot', end: 'Customer' }),
    });
    const data = await response.json();
    setRoute(data);
  };

  return (
    <div className="App">
      <h1>Charging Stations</h1>
      <ul>
        {chargingStations.map((station) => (
          <li key={station.id}>
            {station.location} - Available: {station.available} / {station.capacity}
          </li>
        ))}
      </ul>
      <button onClick={handleOptimizeRoute}>Optimize Route</button>
      {route && (
        <div>
          <h2>Optimized Route</h2>
          <p>Route: {route.route.join(' -> ')}</p>
          <p>Cost: {route.cost}</p>
        </div>
      )}
    </div>
  );
}

export default App;