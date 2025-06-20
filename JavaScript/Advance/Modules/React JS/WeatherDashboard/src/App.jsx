import { useState, useRef } from "react";
import "./App.css";
import MapComponent from "./Map/MapComponent.jsx";
import OptionsContainer from "./Header/OptionsContainer.jsx";
import WeatherComponent from "./Map/WeatherCoponent.jsx";
import { fetchWeatherUsingName, getCurrentLocation } from "./utils/FetchWeather.js";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null); 
  const [isFocused, setIsFocused] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [inputValue, setInputValue] = useState("");

  // const [cityList, setCityList] = useState([]);


  return (
    <>
      <div id="initial-loading-container">
          <div id="blinker"><svg viewBox="0 0 32 32"><path fill="none" d="M9.012,2H22.979q-2.787,5.6-5.593,11.194,2.8.014,5.6.009-4.9,8.4-9.794,16.8c-.019-4.192-.009-8.375-.009-12.567-1.391,0-2.782,0-4.1.00973-Z"/></svg></div>
          <p id="ls12"><span id="initial-header-span">Hi, I'm <strong>Wrap</strong>.</span><br/>Power up to get started </p>
          <button id="initial-button" onClick={async () => {
            getCurrentLocation(setWeather, setCity, setInputValue)
            setIsFocused(true);
            }}>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
          </button>
        </div>
      <div id="app-container">
        <div id="map-container">
            <MapComponent city={city} setCity={setCity} setWeather={setWeather} setIsFocused={setIsFocused} setInputValue={setInputValue}/>
          </div>

        <div id="header-container">
          <OptionsContainer setCity={setCity} setWeather={setWeather} setIsFocused={setIsFocused} setInputValue={setInputValue}/>
          <div id="search-box">
            <input
              type="text"
              value={inputValue}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  fetchWeatherUsingName(inputValue, setWeather, setCity, setInputValue);
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
        </div>
        <div id="overlay-maincontainer">
          <div id="recent-container">
              {/* Should add header and recent cities current weather */}
          </div>
          
          <WeatherComponent weather={weather} />
          
          {/* <div id="forecast-container">
          </div> */}
          
        </div>
      </div>
      
    </>
  );
}
 

export default App;
