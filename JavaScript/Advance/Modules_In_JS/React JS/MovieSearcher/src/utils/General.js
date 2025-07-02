export function isInFavorites(item, list) {
  return Array.isArray(list) && list.some(fav => fav.id === item.id);
}

export function toggleFavorite(item, name, setFavoritesList) {
  const currentList = fetchLocalData(name);
  const inFavs = isInFavorites(item, currentList);
  if (inFavs) {
    removeLocalData(name, item);
  } else {
    saveDataLocally(item, name);
  }
  const updated = fetchLocalData(name);
  setFavoritesList(prev => ({ ...prev, [name]: updated }));
}

const deduplicateMovies = (movies) => {
  const seen = new Set();
  return movies.filter((movie) => {
    if (!movie.id || seen.has(movie.id)) return false;
    seen.add(movie.id);
    return true;
  });
};

function getStorageKey(name) {
  return name === "Movies" ? "favMovies" : name === "Series" ? "favSeries" : null;
}

function saveDataLocally(data, name) {
  const type = getStorageKey(name);
  if (!type) return;

  const prevData = JSON.parse(localStorage.getItem(type)) || [];
  const newData = deduplicateMovies([...prevData, data]);
  localStorage.setItem(type, JSON.stringify(newData));
}

function fetchLocalData(name) {
  const type = getStorageKey(name);
  if (!type) return [];
  return JSON.parse(localStorage.getItem(type)) || [];
}

function removeLocalData(name, removeData) {
  const type = getStorageKey(name);
  if (!type) return false;

  const data = JSON.parse(localStorage.getItem(type)) || [];
  const filteredData = data.filter((x) => x.id !== removeData.id);
  localStorage.setItem(type, JSON.stringify(filteredData));
  return true;
}

export {
  deduplicateMovies,
  saveDataLocally,
  fetchLocalData,
  removeLocalData,
};
