import { useState, useEffect } from "react";
import "./App.css";
import MapComponent from "./Map/MapComponent.jsx";
import OptionsContainer from "./Header/OptionsContainer.jsx";
import WeatherComponent from "./Map/WeatherComponent.jsx";
import { fetchWeatherUsingName, getCurrentLocation } from "./utils/FetchWeather.js";
import NetworkStatus from "./assets/NetworkComponent/NetworkStatus.jsx";

function App() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null); 
  const [isFocused, setIsFocused] = useState(false);
  const [darkMode, setDarkMode] = useState(false);
  const [inputValue, setInputValue] = useState("");
  const [recentCities, setRecentCities] = useState([]);
  const [forecast, setForecast] = useState([]); 
  const [cityList, setCityList] = useState([]);
  let groupedForecasts;
  
  try {
    groupedForecasts = forecast.list?.reduce((acc, item) => {
    const date = new Date(item.dt_txt).toDateString();
    if (!acc[date]) acc[date] = [];
    acc[date].push(item);
    return acc;
  }, {}) || {};

  } catch (errr){
    console.log(errr)
  }
  function getOrdinalSuffix(n) {
    if (n >= 11 && n <= 13) return 'th';
    switch (n % 10) {
      case 1: return 'st';
      case 2: return 'nd';
      case 3: return 'rd';
      default: return 'th';
    }
  }
  useEffect(() => {
    if (city && !inputValue) {
      fetchWeatherUsingName(city, setWeather, setCity, setInputValue, setForecast);
    }
  }, [city]);
  useEffect(() => {
    document.body.className = darkMode ? "dark-mode" : "";
  }, [darkMode]);

  useEffect(() => {
    const stored = localStorage.getItem("recentCities");
    if (stored) setRecentCities(JSON.parse(stored));
  }, []);

  useEffect(() => {
    if (recentCities.length > 0) {
      const lastFive = recentCities.slice(0, 5);
      localStorage.setItem("recentCities", JSON.stringify(lastFive));
      if (recentCities.length > 5) {
        setRecentCities(lastFive);
      }
      console.log("Recent cities updated:", lastFive);
    }
  }, [recentCities]);

  return (
    <>
      <NetworkStatus />
      <div id="initial-loading-container">
        <div id="blinker">
          <svg viewBox="0 0 32 32">
            <path fill="none" d="M9.012,2H22.979q-2.787,5.6-5.593,11.194,2.8.014,5.6.009-4.9,8.4-9.794,16.8c-.019-4.192-.009-8.375-.009-12.567-1.391,0-2.782,0-4.1.00973-Z"/>
          </svg>
        </div>
        <p id="ls12">
          <span id="initial-header-span">Hi, I'm <strong>Wrap</strong>.</span><br/>Power up to get started
        </p>
        <button id="initial-button" onClick={async () => {
          getCurrentLocation(setWeather, setCity, setInputValue, setForecast);
          setIsFocused(true);
        }}>
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
        </button>
      </div>
      <div id="app-container">
        <div id="map-container">
          <MapComponent city={city} setCity={setCity} setWeather={setWeather} setIsFocused={setIsFocused} setInputValue={setInputValue} setForecast={setForecast}/>
        </div>
        <div id="header-container">
          <OptionsContainer setCity={setCity} setWeather={setWeather} setIsFocused={setIsFocused} setInputValue={setInputValue} setForecast={setForecast}/>
          <div id="search-box">
            <input
              type="text"
              value={inputValue}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  fetchWeatherUsingName(inputValue, setWeather, setCity, setInputValue, setForecast);
                  if (inputValue && !recentCities.includes(inputValue)) {
                    setRecentCities([inputValue, ...recentCities].slice(0, 5));
                  }
                  // stopped her, need to add recent cities functionality even for map clicks
                }
              }}
              style={{
                width: isFocused || city ? '18rem' : '0.4rem',
                transition: 'width 0.3s ease',
                borderRadius: '25px',
                backgroundColor:  isFocused ? '#fff' : '#333',
                color:  isFocused ? '#333' : '#fff',
                border: '1px solid #ccc',
                padding: '0.5rem 2.3rem 0.5rem 1rem',
                paddingLeft: isFocused || city ? '2.3rem' : '0rem',
              }}
            />
          </div>
        </div>
        <div id="overlay-maincontainer">
          <div id="recent-container">
            {/* Should add header and recent cities current weather */}
          </div>
          <WeatherComponent weather={weather} />
     
            {forecast && forecast.list && (() => {
              return (
                <div id="forecast-container"  onWheel={(e) => {
                  const container = e.currentTarget;
                  container.scrollLeft += e.deltaY * 3.5; 
                }}>
                   <div id="forecast-header">
                    <h2>5-Day Forecast</h2>
                  </div>
                    {groupedForecasts && Object.entries(groupedForecasts).map(([date, items]) => (
                      <div key={date} className="forecast-column">
                      <div className="forecast-date-header">
                        {new Date(date).getDate()}
                        <sup>{getOrdinalSuffix(new Date(date).getDate())}</sup>
                      </div>
                      <div className="forecast-card-row">
                        {items.map((item) => (
                          <div key={item.dt} className="forecast-card">
                            <div className="forecast-temp">{Math.round(item.main.temp)}°C</div>
                            <div className="forecast-icon">
                              <img
                                src={`https://openweathermap.org/img/wn/${item.weather[0].icon}@2x.png`}
                                alt={item.weather[0].description}
                                title={item.weather[0].description}
                                style={{ width: 40, height: 40 }}
                              />
                            </div>
                            <div className="forecast-time">
                              {new Date(item.dt_txt).toLocaleTimeString([], {
                                hour: '2-digit',
                                minute: '2-digit',
                                hour12: false
                              }
                              )}

                            </div>
                            
                          </div>
                          
                        ))}

                      </div>
                    </div>

                    ))}
                  </div>
              );
            })()}

        </div>
      </div>
    </>
  );
}

export default App;
