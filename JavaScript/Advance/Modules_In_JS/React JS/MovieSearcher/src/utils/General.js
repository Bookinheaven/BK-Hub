const deduplicateMovies = (movies) => {
  const seen = new Set();
  return movies.filter((movie) => {
    if (!movie.id || seen.has(movie.id)) return false;
    seen.add(movie.id);
    return true;
  });
};


export {deduplicateMovies}