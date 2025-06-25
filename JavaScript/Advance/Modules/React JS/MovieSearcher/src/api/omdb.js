

export const fetchMovieBySearch = async (query) => {
    const response = fetch(`https://www.omdbapi.com/?apikey=${API_KEY}&s=${encodeURIComponent(query)}`)
    const data = await response.json()
    return data
}

export const fetchMovieById = async (id) => {
  const response = await fetch(
    `https://www.omdbapi.com/?apikey=${API_KEY}&i=${id}&plot=full`);
  const data = await response.json();
  return data;
};