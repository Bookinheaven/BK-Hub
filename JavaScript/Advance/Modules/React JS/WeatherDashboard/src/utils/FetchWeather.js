const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
const baseUrl = import.meta.env.VITE_WEATHER_API_BASE;
import { sendWarning, sendError, normalizeName } from "./general";

const fetchWeatherUsingName = async (city, setWeather, setCity, setInputValue, setForecast) => {
  if (!city || city.trim() === "" || city === "Search") {
    setWeather(null);
    return;
  }
  try {
    const response = await fetch(
      `${baseUrl}/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) {
      sendWarning("City not found");
      setWeather(null);
      return;
    }
    const data = await response.json();
    setWeather(data);
    setCity(normalizeName(data.name));
    getForecastUsingName(normalizeName(data.name), setForecast);
    setInputValue(normalizeName(data.name));
  } catch (error) {
    setWeather(null);
    console.error("Error fetching weather data using name:", error);
  }
};

const fetchWeatherUsingLL = async (lat, long, setWeather, setCity, setInputValue, setForecast) => {
  try {
    setWeather(null);
    if (!lat || !long) {
      sendWarning("Location not found");
      setWeather(null);
      return;
    }
    if (isNaN(lat) || isNaN(long)) {
      sendWarning("Invalid coordinates");
      setWeather(null);
      return;
    }
    const response = await fetch(
      `${baseUrl}/weather?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) {
      sendWarning("Location not found");
      setWeather(null);
      return;
    }
    const data = await response.json();
    setWeather(data);
    getForecastUsingName(normalizeName(data.name), setForecast);
    if (data.name) {
      setCity(normalizeName(data.name));
      setInputValue(normalizeName(data.name));
    }
  } catch (error) {
    setWeather(null);
    console.error("Error fetching weather data using lat:", error);
  }
};

function getForecastUsingName(city, setForecast) {
  if (!city || city.trim() === "" || city === "Search") {
    setForecast(null);
    return;
  }
  fetch(`${baseUrl}/forecast?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`)
    .then((response) => {
      if (!response.ok) {
        sendWarning("City not found");
        setForecast(null);
        throw new Error("City not found");
      }
      return response.json();
    })
    .then((data) => {
      setForecast(data);
    })
    .catch((error) => {
      setForecast(null);
      console.error("Error fetching forecast data using name:", error);
    });
}

function getCurrentLocation(setWeather, setCity, setInputValue, setForecast) {
  const tempcity = "Andhra Pradesh";
  if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        fetchWeatherUsingLL(latitude, longitude, setWeather, setCity, setInputValue, setForecast);
      },
      (error) => {
        sendWarning("Unable to retrieve your location. Showing default city.");
        fetchWeatherUsingName(tempcity, setWeather, setCity, setInputValue, setForecast);
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