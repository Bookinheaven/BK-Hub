import { Suspense, lazy } from "react";
import "./CardManager.css"
const MovieCard = lazy(() => import("./MovieCard"));

export default function CardManager({ movies }) {
  return (
    <div id="search-results">
      {movies.length > 0 ? (
        <Suspense fallback={loader}>
          {movies.map((movie) => (
            <MovieCard key={movie.imdbID} movie={movie} />
          ))}
        </Suspense>
      ) : (
        <loader></loader>
      )}
    </div>
  );
}


function loader() {
    return (
        <div id="loader"></div>
    );
}