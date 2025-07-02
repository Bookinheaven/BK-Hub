import {
  fetchPopularMS,
  fetchTopRatedMS,
  fetchUpcomingMovies,
  fetchMovieBySearch
} from "../api/apidb";
import { deduplicateMovies } from "./General";

export async function loadPopular(type, page, setData, setAllData) {
  const data = await fetchPopularMS(page, type);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setAllData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}

export async function loadTopRated(type, page, setData, setAllData) {
  const data = await fetchTopRatedMS(page, type);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setAllData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}

export async function loadUpcoming(page, setData, setAllData) {
  const data = await fetchUpcomingMovies(page);
  if (Array.isArray(data)) {
    const uniqueNew = deduplicateMovies(data);
    setData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setAllData(prev => deduplicateMovies([...prev, ...uniqueNew]));
    return true;
  }
  return false;
}

export async function loadSearchResults(query, pageState, setMovies, setAllMovies, setShowNoResults) {
  const data = await fetchMovieBySearch(query, pageState);
  pageState[1] = data[1];

  if (Array.isArray(data[0]) && data[0].length > 0 && pageState[0] <= pageState[1]) {
    const uniqueNew = deduplicateMovies(data[0]);
    setMovies(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setAllMovies(prev => deduplicateMovies([...prev, ...uniqueNew]));
    setShowNoResults(false);
    pageState[0]++;
  } else {
    setShowNoResults(true);
    setMovies([]);
  }
}
