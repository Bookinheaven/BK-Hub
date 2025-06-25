import { useState } from "react";
import {fetchMovieBySearch, fetchMovieById} from "./api/omdb.js"

function App() {
  const [query, setQuery] = useState("");
  const [movies, setMovies] = useState([]);

  const fetchMovies = async () => {
    let data = fetchMovieBySearch(query)
    if (data) {
      setMovies(data);
    } else {
      setMovies([]);
    }
  };

  return (
    <>
        <div id="search-box-container">
            <input id="query-box"/>
        </div>
    </>
  );
}

export default App;
