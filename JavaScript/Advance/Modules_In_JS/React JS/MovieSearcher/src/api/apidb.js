const TMDB_BASE_URL = import.meta.env.VITE_TMDB_BASE_URL;
const TMDB_IMAGE_BASE = import.meta.env.VITE_TMDB_IMAGE_BASE;
const TMDB_AUTH = import.meta.env.VITE_TMDB_AUTH;

const TMDB_HEADERS = {
  method: "GET",
  headers: {
    accept: "application/json",
    Authorization: TMDB_AUTH,
  },
};

const fetchFromAPI = async (url, options) => {
  try {
    const response = await fetch(url, options);
    if (!response.ok) {
      console.error(`${response.status} ${response.statusText} → ${url}`);
      return null;
    }
    const text = await response.text();
    try {
      return JSON.parse(text);
    } catch (parseErr) {
      console.error("Failed to parse JSON:", text);
      return null;
    }
  } catch (err) {
    console.error("Fetch failed:", err);
    return null;
  }
};

const formatTMDbMovies = (movies) => {
  const seenIds = new Set();
  return movies
    .filter(
      (movie) =>
        movie.poster_path && !seenIds.has(movie.id) && seenIds.add(movie.id)
    )
    .map((movie) => ({
      id: movie.id || "",
      title: movie.title || "",
      poster: `${TMDB_IMAGE_BASE}${movie.poster_path}`,
      year: movie.release_date?.split("-")[0] || "",
    }));
};

const formatTMDbSeries = (series) => {
  const seenIds = new Set();
  return series
    .filter(
      (serie) =>
        serie.poster_path && !seenIds.has(serie.id) && seenIds.add(serie.id)
    )
    .map((serie) => ({
      id: serie.id || "",
      title: serie.name || "",
      poster: `${TMDB_IMAGE_BASE}${serie.poster_path}`,
      year: serie.first_air_date?.split("-")[0] || "",
    }));
};

const formatTMDbMoviesForSearch = (movies, max) => {
  const seenIds = new Set();
  return [
    movies
      .filter(
        (movie) =>
          movie.poster_path && !seenIds.has(movie.id) && seenIds.add(movie.id)
      )
      .map((movie) => ({
        id: movie.id || "",
        title: movie.title || "",
        poster: `${TMDB_IMAGE_BASE}${movie.poster_path}`,
        year: movie.release_date?.split("-")[0] || "",
      })),
    max,
  ];
};

export const fetchMovieBySearch = async (query, page = 1) => {
  const url = `${TMDB_BASE_URL}/search/movie?query=${encodeURIComponent(
    query
  )}&include_adult=false&language=en-US&page=${page}`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results
    ? formatTMDbMoviesForSearch(json.results, json.total_pages)
    : [];
};

export const fetchPopularMS = async (page = 1, type = "Movies") => {
  const searchType = type === "Movies" ? "movie" : "tv";
  const url = `${TMDB_BASE_URL}/${searchType}/popular?language=en-US&page=${page}`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  const results = json?.results || [];
  return type === "Movies"
    ? formatTMDbMovies(results)
    : formatTMDbSeries(results);
};

export const fetchTopRatedMS = async (page = 1, type = "Movies") => {
  const searchType = type === "Movies" ? "movie" : "tv";
  const url = `${TMDB_BASE_URL}/${searchType}/top_rated?language=en-US&page=${page}`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  const results = json?.results || [];
  return type === "Movies"
    ? formatTMDbMovies(results)
    : formatTMDbSeries(results);
};

// export const fetchTopRatedMovies = async (page = 1) => {
//   const url = `${TMDB_BASE_URL}/movie/top_rated?language=en-US&page=${page}`;
//   const json = await fetchFromAPI(url, TMDB_HEADERS);
//   return json?.results ? formatTMDbMovies(json.results) : [];
// };

export const fetchUpcomingMovies = async (page = 1) => {
  const url = `${TMDB_BASE_URL}/movie/upcoming?language=en-US&page=${page}`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results ? formatTMDbMovies(json.results) : [];
};
