import { normalizeName } from "../utils/general";
import { Tooltip as ReactTooltip } from "react-tooltip";
import "./WeatherComponent.css";

function handleClose() {
  const weatherContainer = document.getElementById("current-weather-container");
  if (weatherContainer) {
    weatherContainer.classList.add("hidden");
  }
}
export default function WeatherComponent({ weather }) {
  const regionNames = new Intl.DisplayNames(["en"], { type: "region" });

  return (
    <div id="current-weather-container" className={weather ? "" : "hidden"}>
        <button id="close-btn-mobile" onClick={handleClose}>✖</button>
      {weather && (
        <div id="current-weather">
          <h2 id="city-heading">
            {weather.name && weather.sys
              ? `${normalizeName(weather.name)}, ${regionNames.of(weather.sys.country)}`
              : ""}
          </h2>

          <div id="main-weather-row">
            <p id="temp-value">
              <strong>
                {weather.main?.temp !== undefined
                  ? `${weather.main.temp.toFixed(1)} °C`
                  : ""}{" "}
                <br />
              </strong>
              <span id="weather-description">
                {weather.weather?.[0]?.description || ""}
              </span>
            </p>

            {weather.weather?.[0] && (
              <div
                id="weather-icon"
                data-tooltip-id="weather-icon-data"
                data-tooltip-content={weather.weather[0].main}
              >
                <img
                  src={`https://openweathermap.org/img/wn/${weather.weather[0].icon}@2x.png`}
                  alt="weather icon"
                />
                <ReactTooltip id="weather-icon-data" place="bottom" />
              </div>
            )}
          </div>

          <table id="weather-table">
            <tbody>
              <tr className="other-weather-row">
                <td>Feels Like</td>
                <td>
                  {weather.main?.feels_like !== undefined
                    ? `${weather.main.feels_like.toFixed(1)} °C`
                    : ""}
                </td>
              </tr>

              {weather.rain && (
                <tr className="other-weather-row">
                  <td>Precipitation</td>
                  <td>
                    {weather.rain["1h"] !== undefined
                      ? `${weather.rain["1h"].toFixed(2)} mm`
                      : "0.00 mm"}
                  </td>
                </tr>
              )}

              <tr className="other-weather-row">
                <td>Wind Speed</td>
                <td>
                  {weather.wind?.speed !== undefined
                    ? `${weather.wind.speed.toFixed(2)} m/s`
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Visibility</td>
                <td>
                  {weather.visibility !== undefined
                    ? `${(weather.visibility / 1000).toFixed(2)} km`
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Cloudiness</td>
                <td>
                  {weather.clouds?.all !== undefined
                    ? `${typeof weather.clouds.all === "number" && weather.clouds.all.toFixed
                        ? weather.clouds.all.toFixed(2)
                        : weather.clouds.all
                      }%`
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Humidity</td>
                <td>
                  {weather.main?.humidity !== undefined
                    ? `${typeof weather.main.humidity === "number" && weather.main.humidity.toFixed
                        ? weather.main.humidity.toFixed(2)
                        : weather.main.humidity
                      }%`
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Pressure</td>
                <td>
                  {weather.main?.pressure !== undefined
                    ? `${typeof weather.main.pressure === "number" && weather.main.pressure.toFixed
                        ? weather.main.pressure.toFixed(2)
                        : weather.main.pressure
                      } hPa`
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Sun rise</td>
                <td>
                  {weather.sys?.sunrise
                    ? new Date(weather.sys.sunrise * 1000).toLocaleTimeString()
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Sun set</td>
                <td>
                  {weather.sys?.sunset
                    ? new Date(weather.sys.sunset * 1000).toLocaleTimeString()
                    : ""}
                </td>
              </tr>

              <tr className="other-weather-row">
                <td>Last Updated</td>
                <td>
                  {weather.dt
                    ? new Date(weather.dt * 1000).toLocaleTimeString()
                    : ""}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
