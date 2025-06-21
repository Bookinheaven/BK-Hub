import { useRef, useEffect, useState } from "react";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
const OpenCageAPIKEY = import.meta.env.VITE_WEATHER_GEOCAGE_KEY;
import { fetchWeatherUsingLL } from "../utils/FetchWeather";
import "./MapComponent.css";

export default function MapComponent({ city, setCity, setWeather, setInputValue }) {
  const mapContainerRef = useRef(null);
  const mapRef = useRef(null);
  const markerRef = useRef(null);

  const [mapReady, setMapReady] = useState(false);

  useEffect(() => {
    mapRef.current = new maplibregl.Map({
      container: mapContainerRef.current,
      style: "/public-assets/toner.json",
      center: [77.5946, 12.9716],
      zoom: 10,
    });

    mapRef.current.on("load", () => {
      setMapReady(true);
    });

    mapRef.current.on("click", (e) => {
      const { lng, lat } = e.lngLat;
      placeMarker([lng, lat]);
      fetchWeatherUsingLL(lat, lng, setWeather, setCity, setInputValue);
    });

    return () => {
      mapRef.current.remove();
    };
  }, []);

    useEffect(() => {
    const searchCity = async () => {
        if (city && mapReady) {
        const coords = await fetchCityCoordinates(city);
        if (coords) {
            placeMarker(coords);
            mapRef.current.flyTo({ center: coords, zoom: 12, speed: 1.4 });
        }
        }
    };
    searchCity();
    }, [city, mapReady]); 


  const placeMarker = ([lng, lat]) => {
    if (markerRef.current) markerRef.current.remove();
    markerRef.current = new maplibregl.Marker({ color: "orange" })
      .setLngLat([lng, lat])
      .addTo(mapRef.current);
  };

  const fetchCityCoordinates = async (cityName) => {
    try {
      const res = await fetch(
        `https://api.opencagedata.com/geocode/v1/json?q=${cityName}&key=${OpenCageAPIKEY}`
      );
      const data = await res.json();
      if (data.results.length > 0) {
        return [
            data.results[0].geometry.lng,
            data.results[0].geometry.lat
        ];
     }
    } catch (e) {
      console.error("❌ Failed to geocode city:", e.message);
    }
    return null;
  };

  return <div ref={mapContainerRef} style={{ width: "100%", height: "100vh" }} />;
}
