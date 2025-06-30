import cities from "../assets/data/cities.json";
import { fetchWeatherUsingName } from "../utils/FetchWeather.js";
import "./OptionsContainer.css";

export default function OptionsContainer({ setCity, setWeather, setIsFocused, setInputValue, setForecast}) {
    return (
        <div id="options-container">
              <button
                id="home-button"
                onClick={() => {
                  setCity("");
                  setWeather(null);
                  setIsFocused(false);
                  setInputValue("");
                  setForecast(null)
                }}
                >
                <svg viewBox="0 0 24 24">
                  <path fillRule="evenodd" d="M17.8913288,10 L11.8900003,3.99867157 L5.88867192,10 L5.89001465,10 L5.89001465,20 L17.8900146,20 L17.8900146,10 L17.8913288,10 Z M19.8900146,11.9986859 L19.8900146,20 C19.8900146,21.1045695 18.9945841,22 17.8900146,22 L5.89001465,22 C4.78544515,22 3.89001465,21.1045695 3.89001465,20 L3.89001465,11.9986573 L2.41319817,13.4754737 L1,12.0622756 L10.4769858,2.5852898 C11.2573722,1.8049034 12.5226285,1.8049034 13.3030149,2.5852898 L22.7800007,12.0622756 L21.3668025,13.4754737 L19.8900146,11.9986859 Z"/>
                </svg>
                </button>

                <hr></hr>
                <button
                id="shuffle-button"
                onClick={() => {
                  const randomCity = cities[Math.floor(Math.random() * cities.length)];
                  fetchWeatherUsingName(randomCity, setWeather, setCity, setInputValue);
                   const weatherContainer = document.getElementById("current-weather-container");
                  if (weatherContainer) {
                    weatherContainer.classList.remove("hidden");
                  }
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
    );
}