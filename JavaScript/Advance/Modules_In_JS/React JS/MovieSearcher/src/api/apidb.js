const OMDB_API_KEY = import.meta.env.VITE_OMDb_api_key;
const TMDB_BASE_URL = import.meta.env.VITE_TMDB_BASE_URL
const TMDB_IMAGE_BASE = import.meta.env.VITE_TMDB_IMAGE_BASE
const TMDB_AUTH = import.meta.env.VITE_TMDB_AUTH

const TMDB_HEADERS = {
  method: 'GET',
  headers: {
    accept: 'application/json',
    Authorization: TMDB_AUTH
  }
};

const OMDB_HEADERS = {
  method: 'GET',
  headers: {
    accept: 'application/json'
  }
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


const formatOMDbMovies = (movies) => {
  return movies.map(movie => ({
    id: movie.imdbID || "",
    title: movie.Title || "",
    poster: movie.Poster || "",
    year: movie.Year || ""
  }));
};

const formatTMDbMovies = (movies) => {
  const seenIds = new Set();

  return movies
    .filter(movie => movie.poster_path && !seenIds.has(movie.id) && seenIds.add(movie.id))
    .map(movie => ({
      id: movie.id || "",
      title: movie.title || "",
      poster: `${TMDB_IMAGE_BASE}${movie.poster_path}`,
      year: movie.release_date?.split("-")[0] || ""
    }));
};


export const fetchMovieBySearch = async (query) => {
  const url = `${TMDB_BASE_URL}/search/movie?query=${encodeURIComponent(query)}&include_adult=false&language=en-US&page=1`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results ? formatTMDbMovies(json.results) : [];
};

// export const fetchMovieById = async (id) => {
//   const url = `https://www.omdbapi.com/?apikey=${OMDB_API_KEY}&i=${id}&plot=full`;
//   return await fetchFromAPI(url, OMDB_HEADERS);
// };

export const fetchPopularMovies = async () => {
  const url = `${TMDB_BASE_URL}/movie/popular?language=en-US&page=1`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results ? formatTMDbMovies(json.results) : [];
};

export const fetchTopRatedMovies = async () => {
  const url = `${TMDB_BASE_URL}/movie/top_rated?language=en-US&page=1`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results ? formatTMDbMovies(json.results) : [];
};

export const fetchUpcomingMovies = async () => {
  const url = `${TMDB_BASE_URL}/movie/upcoming?language=en-US&page=1`;
  const json = await fetchFromAPI(url, TMDB_HEADERS);
  return json?.results ? formatTMDbMovies(json.results) : [];
};
