import { normalizeName } from "../utils/general";  

export default function WeatherComponent({ weather }) {
  return (
    <div id="current-weather-container">
        {weather && (
        <div id="current-weather">
            <h2 id="city-heading">{normalizeName(weather.name)}, {weather.sys.country}</h2>

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
    );
} 