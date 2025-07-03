import {
  fetchPopularMS,
  fetchTopRatedMS,
  fetchUpcomingMovies,
  fetchMovieBySearch,
  fetchSeriesBySearch
} from "../api/apidb";
import { deduplicateMovies } from "./General";

export async function loadPopular(type, page, setData) {
  const data = await fetchPopularMS(page, type);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}

export async function loadTopRated(type, page, setData) {
  const data = await fetchTopRatedMS(page, type);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}

export async function loadUpcoming(page, setData) {
  const data = await fetchUpcomingMovies(page);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}
export async function loadSearchResults(query,pageState,setMovies,setShowNoResults,movieNoResultTimeout, type) {
  if (movieNoResultTimeout.current) {
    clearTimeout(movieNoResultTimeout.current);
    movieNoResultTimeout.current = null;
  }
  
  const data = (type == "Movies")  ? await fetchMovieBySearch(query, pageState) : await fetchSeriesBySearch(query, pageState);
  const [results, totalPages] = data;
  console.log(results)
  pageState[1] = totalPages;
  if (Array.isArray(results) && results.length > 0) {
    const uniqueNew = deduplicateMovies(results);
    setMovies(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setShowNoResults(false);
    pageState[0]++;
  } else {
    if (pageState[0] === 1) {
      movieNoResultTimeout.current = setTimeout(() => {
        setShowNoResults(true);
      }, 3000);
    }
  }
}


