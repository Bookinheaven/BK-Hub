import { useState, useRef } from "react";
import "./App.css";
import cities from "./assets/data/cities.json";
const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
const baseUrl = import.meta.env.VITE_WEATHER_API_BASE;

function getCurrentLocation(setWeather, setCity) {
  let tempcity = "Andhra Pradesh";
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        console.log("Current location:", latitude, longitude);
        fetchWeatherUsingLL(latitude, longitude, setWeather, setCity);
      },
      (error) => {
        console.error("Error getting location:", error.message);
        fetchWeatherUsingName(tempcity, setWeather, setCity);

      }
    );
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
  const loader = document.getElementById('initial-loading-container');
  if (loader) {
    loader.style.display = 'none';
  } else {
    console.error("Loader element not found");
  }
}

const fetchWeatherUsingName = async (city, setWeather, setCity) => {
  if (!city || city.trim() === "" || city === "Search") {
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
    setCity(`${data.name}`);
    console.log("✅ Weather data fetched successfully:", data);
  } catch (error) {
    console.error("❌ Error fetching weather data:", error.message);
    setWeather(null)
  }
};

const fetchWeatherUsingLL = async (lat, long, setWeather, setCity) => {
  try {
    const response = await fetch(
      `${baseUrl}/weather?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) throw new Error("Location not found");
    const data = await response.json();
    setWeather(data);
    setCity(`${data.name}`);
    console.log("Weather data fetched successfully:", data);
  } catch (error) {
    console.error("❌ Error fetching weather data:", error.message);
    setWeather(null);
  }

};

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null); 
  const [isFocused, setIsFocused] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  // const [cityList, setCityList] = useState([]);
  

  return (
    <>
      <div id="initial-loading-container">
          <h1>Hi, I'm Wrap.</h1>
          <p>Turn Me On!</p>
          <button onClick={async () => {
            getCurrentLocation(setWeather, setCity)
            setIsFocused(true);
            }}>
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-power"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
          </button>
        </div>
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
              <button
              id="shuffle-button"
              onClick={() => {
                const randomCity = cities[Math.floor(Math.random() * cities.length)];
                fetchWeatherUsingName(randomCity, setWeather, setCity);
              }}
              >
              <svg viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="M560-160v-80h104L537-367l57-57 126 126v-102h80v240H560Zm-344 0-56-56 504-504H560v-80h240v240h-80v-104L216-160Zm151-377L160-744l56-56 207 207-56 56Z"/></svg>
              </button>
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
                fetchWeatherUsingName(city, setWeather, setCity);
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

        {/* 
        <div id="overlay-box">
        </div>
        */}
        <div id="overlay-maincontainer">
          <div id="recent-container">
              {/* Should add header and recet cities current weather */}
          </div>

          <div id="current-weather-container">
              {weather && (
              <div id="current-weather">
                <h2 id="city-heading">{weather.name}, {weather.sys.country}</h2>
        
                <table>
                  <tbody>
                    <tr>
                      <td><strong>{weather.main.temp} °C</strong></td>
                      <td><img
                        src={`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`}
                        alt="weather icon"
                      />
                      </td>
                    </tr>
                    <tr>
                      <td>Feels Like</td>
                      <td>{weather.main.feels_like} °C</td>
                    </tr>
                    {weather.rain && (
                      <tr>
                        <td>Precipitation</td>
                        <td>{weather.rain ? `${weather.rain['1h']} mm` : '0 mm'}</td>
                      </tr>
                      )
                    }
                    
                    <tr>
                      <td>Wind Speed</td>
                      <td>{weather.wind.speed} m/s</td>
                    </tr>
                    <tr>
                      <td>Visibility</td>
                      <td>{(weather.visibility / 1000).toFixed(1)} km</td>
                    </tr>
                    <tr>
                      <td>Cloudiness</td>
                      <td>{weather.clouds.all}%</td>
                    </tr>
                    <tr>
                      <td>Humidity</td>
                      <td>{weather.main.humidity}%</td>
                    </tr>
                    <tr>
                      <td>Pressure</td>
                      <td>{weather.main.pressure} hPa</td>
                    </tr>
                    <tr>
                      <td>Sun rise</td>
                      <td>{new Date(weather.sys.sunrise * 1000).toLocaleTimeString()}</td>
                    </tr>
                    <tr>
                      <td>Sun set</td>
                      <td>{new Date(weather.sys.sunset * 1000).toLocaleTimeString()}</td>
                    </tr>

                    <tr>
                      <td>Last Updated</td>
                      <td>{new Date(weather.dt * 1000).toLocaleTimeString()}</td>
                    </tr>
                    </tbody>
                  </table>
                {/* <p><strong>🌥️ Weather:</strong> {weather.weather[0].description}</p>
                <p><strong>🗒️ Description:</strong> {weather.weather[0].main}</p> */}
              </div>
            )}
          
          </div>
          
          <div id="forecast-container">
          </div>
          
          <div id="weather-info-container">
            {weather && (
              <div>
                <h3>More Info</h3>
                <ul>
                  <li><strong>Feels Like:</strong> {weather.main.feels_like} °C</li>
                  <li><strong>Min Temp:</strong> {weather.main.temp_min} °C</li>
                  <li><strong>Max Temp:</strong> {weather.main.temp_max} °C</li>
                  <li><strong>Cloudiness:</strong> {weather.clouds.all}%</li>
                  <li><strong>Visibility:</strong> {weather.visibility} m</li>
                </ul>
              </div>
            )}
          </div>  
        
        </div>
      </div>
    </>
  );
}
 

export default App;
