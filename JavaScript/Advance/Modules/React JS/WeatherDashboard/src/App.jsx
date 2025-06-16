import { useState } from "react";
import "./App.css";

const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
const baseUrl = import.meta.env.VITE_WEATHER_API_BASE;

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [isFocused, setIsFocused] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  // const [cityList, setCityList] = useState([]);
  
  const fetchWeather = async () => {

    if (!city || city.trim() === "" || city === "Search") {
      console.error("❌ Please enter a valid city name.");
      setWeather(null);
      return;
    }
    try {
      const response = await fetch(
        `${baseUrl}/weather?q=${city}&appid=${apiKey}&units=metric`
      );

      if (!response.ok) throw new Error("City not found");

      const data = await response.json();
      setWeather(data);
      console.log("✅ Weather data fetched successfully:", data);
    } catch (error) {
      console.error("❌ Error fetching weather data:", error.message);
      setWeather(null)
    }
  };

  return (
    <div id="app-container">
      <div id="options-container">
          <button
            id="home-button"
            onClick={() => {
              setCity("");
              setWeather(null);
              setIsFocused(false);
            }}
            >
            <svg viewBox="0 0 24 24">
              <path fill-rule="evenodd" d="M17.8913288,10 L11.8900003,3.99867157 L5.88867192,10 L5.89001465,10 L5.89001465,20 L17.8900146,20 L17.8900146,10 L17.8913288,10 Z M19.8900146,11.9986859 L19.8900146,20 C19.8900146,21.1045695 18.9945841,22 17.8900146,22 L5.89001465,22 C4.78544515,22 3.89001465,21.1045695 3.89001465,20 L3.89001465,11.9986573 L2.41319817,13.4754737 L1,12.0622756 L10.4769858,2.5852898 C11.2573722,1.8049034 12.5226285,1.8049034 13.3030149,2.5852898 L22.7800007,12.0622756 L21.3668025,13.4754737 L19.8900146,11.9986859 Z"/>
            </svg>
            </button>

            <hr></hr>

          {/* <button
            id="city-list-button"
            onClick={() => {
            
            }}
            >
            </button> */}
      </div>
      <div id="search-box">
        <input
          type="text"
          value={city}
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
          onChange={(e) => setCity(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              fetchWeather();
            }
          }}
          style={{
            width: isFocused || city ? '200px' : '0.5rem',
            transition: 'width 0.3s ease',
            borderRadius: '25px',
            border: '1px solid #ccc',
            padding: '0.5rem 2.3rem 0.5rem 1rem',
            paddingLeft: isFocused || city ? '2.3rem' : '0rem',
          }}
        />
      </div>
      <div id="color-mode-box">
        <input
          type="checkbox"
          id="color-mode-button"
          checked={darkMode}
          onChange={() => setDarkMode(!darkMode)}
          style={{
            width: '2rem',
            height: '1rem',
            position: 'relative',
            appearance: 'none',
            backgroundColor: darkMode ? '#333' : '#ccc',
            borderRadius: '1rem',
            cursor: 'pointer',
          }}
        />
        <label
          htmlFor="color-mode-button"
          style={{
            position: 'absolute',
            top: '50%',
            left: darkMode ? '1rem' : '0.2rem',
            transform: 'translateY(-50%)',
            width: '0.8rem',
            height: '0.8rem',
            backgroundColor: '#fff',
            borderRadius: '50%',
            transition: 'left 0.3s ease',
          }}
        ></label>
      </div>


      <div id="overlay-box">
      </div>
      <div id="overlay-maincontainer">
        <div id="recent-container">
          
        </div>

        <div id="current-weather-container">
          
        
        </div>
        
        <div id="forecast-container">
        </div>
        
        <div id="weather-info-container">
        </div>  
      
      </div>
    </div>
  );
}


export default App;
