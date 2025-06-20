const apiKey = import.meta.env.VITE_WEATHER_API_KEY;
const baseUrl = import.meta.env.VITE_WEATHER_API_BASE;
import { normalizeName } from "./general";

const fetchWeatherUsingName = async (city, setWeather, setCity, setInputValue) => {
  if (!city || city.trim() === "" || city === "Search") {
    setWeather(null);
    return;
  }
      console.log(city)

  try {
    const response = await fetch(
      `${baseUrl}/weather?q=${city}&appid=${apiKey}&units=metric`
    );

    if (!response.ok) throw new Error("City not found");

    const data = await response.json();
    setWeather(data);
    setCity(`${normalizeName(data.name)}`);
    setInputValue(`${normalizeName(data.name)}`);
    console.log("✅ Weather data fetched successfully:", data);
  } catch (error) {
    console.error("❌ Error fetching weather data:", error.message);
    setWeather(null)
  }
};

const fetchWeatherUsingLL = async (lat, long, setWeather, setCity, setInputValue) => {
  try {
    const response = await fetch(
      `${baseUrl}/weather?lat=${lat}&lon=${long}&appid=${apiKey}&units=metric`
    );
    if (!response.ok) throw new Error("Location not found");
    const data = await response.json();
    setWeather(data);
    setCity(`${normalizeName(data.name)}`);
    setInputValue(`${normalizeName(data.name)}`);
    console.log("Weather data fetched successfully:", data);
  } catch (error) {
    console.error("❌ Error fetching weather data:", error.message);
    setWeather(null);
  }

};


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
    console.log("Geolocation is not supported by this browser.");
  }
  const loader = document.getElementById('initial-loading-container');
  if (loader) {
    loader.style.display = 'none';
  } else {
    console.error("Loader element not found");
  }
}

export { fetchWeatherUsingName, fetchWeatherUsingLL, getCurrentLocation };