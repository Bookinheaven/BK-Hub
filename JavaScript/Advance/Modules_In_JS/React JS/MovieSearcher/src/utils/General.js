const deduplicateMovies = (movies) => {
  const seen = new Set();
  return movies.filter((movie) => {
    if (!movie.id || seen.has(movie.id)) return false;
    seen.add(movie.id);
    return true;
  });
};


function saveDataLocally(data, name, type) {
  
}

export {deduplicateMovies, saveDataLocally}