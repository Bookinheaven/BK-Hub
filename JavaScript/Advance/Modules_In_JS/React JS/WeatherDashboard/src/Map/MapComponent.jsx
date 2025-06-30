import { useRef, useEffect, useCallback } from "react";
import maplibregl from "maplibre-gl";
import "maplibre-gl/dist/maplibre-gl.css";
const OpenCageAPIKEY = import.meta.env.VITE_WEATHER_GEOCAGE_KEY;
import { fetchWeatherUsingLL } from "../utils/FetchWeather";
import "./MapComponent.css";

export default function MapComponent({ city, setCity, setWeather, setInputValue, setForecast }) {
  const mapContainerRef = useRef(null);
  const mapRef = useRef(null);
  const markerRef = useRef(null);
  const mapReadyRef = useRef(false);

  const placeMarker = useCallback(([lng, lat]) => {
    if (markerRef.current) markerRef.current.remove();
    markerRef.current = new maplibregl.Marker({ color: "orange" })
      .setLngLat([lng, lat])
      .addTo(mapRef.current);
  }, []);

  const fetchCityCoordinates = useCallback(async (cityName) => {
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
  }, []);

  // Initialize map
  useEffect(() => {
    mapRef.current = new maplibregl.Map({
      container: mapContainerRef.current,
      style: "/public-assets/toner.json",
      center: [77.5946, 12.9716],
      zoom: 10,
      minZoom: 2,
      maxZoom: 18,
      pitchWithRotate: false,
      dragRotate: false,
      pitch: 0,
      bearing: 0,
    });

    const onLoad = () => {
      mapReadyRef.current = true;
    };

    mapRef.current.on("load", onLoad);

    const onClick = (e) => {
      const { lng, lat } = e.lngLat;
      placeMarker([lng, lat]);
      setWeather(null);
      fetchWeatherUsingLL(lat, lng, setWeather, setCity, setInputValue, setForecast);
    };

    mapRef.current.on("click", onClick);

    return () => {
      mapRef.current.off("load", onLoad);
      mapRef.current.off("click", onClick);
      mapRef.current.remove();
    };
  }, [placeMarker, setWeather, setCity, setInputValue, setForecast]);

  useEffect(() => {
    if (!city || !mapReadyRef.current) return;
    fetchCityCoordinates(city).then((coords) => {
      if (!coords) return;
      const [lng, lat] = coords;
      const marker = markerRef.current;
      if (
        !marker ||
        marker.getLngLat().lng !== lng ||
        marker.getLngLat().lat !== lat
      ) {
        placeMarker(coords);
        mapRef.current.flyTo({ center: coords, zoom: 12, speed: 1.4 });
      }
    });
  }, [city, fetchCityCoordinates, placeMarker]);

  return <div ref={mapContainerRef} style={{ width: "100%", height: "100vh" }} />;
}
