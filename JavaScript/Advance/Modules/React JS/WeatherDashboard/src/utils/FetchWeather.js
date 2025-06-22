const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
const baseUrl = import.meta.env.VITE_WEATHER_API_BASE;
import { sendWarning, sendError, normalizeName } from "./general";


const fetchWeatherUsingName = async (city, setWeather, setCity, setInputValue) => {
  if (!city || city.trim() === "" || city === "Search") {
    setWeather(null);
    return;
  }
  try {
    const response = await fetch(
      `${baseUrl}/weather?q=${city}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) sendWarning("City not found");
    
    const data = await response.json();
    setWeather(data);
    setCity(`${normalizeName(data.name)}`);
    setInputValue(`${normalizeName(data.name)}`);
  } catch (error) {
    console.error("Error fetching weather data using name:", error.message);
    setWeather(null)
  }
};

const fetchWeatherUsingLL = async (lat, long, setWeather, setCity, setInputValue) => {
  try {
    setWeather(null);
    if (!lat || !long) sendWarning("Location not found");
    if (isNaN(lat) || isNaN(long)) sendWarning("Invalid coordinates");
    const response = await fetch(
      `${baseUrl}/weather?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) sendWarning("Location not found");
    const data = await response.json();
    setWeather(data);
    if (data.name) {
      setCity(`${normalizeName(data.name)}`);
      setInputValue(`${normalizeName(data.name)}`);
    }
  } catch (error) {
    console.error("Error fetching weather data using lat:", error.message);
    setWeather(null);
  }

};

function getForecastUsingLL(lat, long, setForecast) {
  if (!lat || !long) sendWarning("Location not found");
  if (isNaN(lat) || isNaN(long)) sendWarning("Invalid coordinates");
  fetch(
    `${baseUrl}/forecast?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`
  )
    .then((response) => {
      if (!response.ok) sendWarning("Location not found");
      return response.json();
    })
    .then((data) => {
      setForecast(data);
    })
    .catch((error) => {
      console.error("Error fetching forecast data:", error.message);
      setForecast(null);
    });
}


function getCurrentLocation(setWeather, setCity, setInputValue) {
  let tempcity = "Andhra Pradesh";
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        console.log("Current location:", latitude, longitude);
        fetchWeatherUsingLL(latitude, longitude, setWeather, setCity, setInputValue);
      },
      (error) => {
        console.error("Error getting location:", error.message);
        fetchWeatherUsingName(tempcity, setWeather, setCity, setInputValue);

      }
    );
  } else {
    sendError("Geolocation is not supported by this browser.");
  }
  const loader = document.getElementById('initial-loading-container');
  if (loader) {
    loader.style.display = 'none';
  }
}

export { fetchWeatherUsingName, fetchWeatherUsingLL, getCurrentLocation };