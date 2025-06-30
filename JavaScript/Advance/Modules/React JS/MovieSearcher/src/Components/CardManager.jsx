import { Suspense, lazy } from "react";
import "./CardManager.css"
const MovieCard = lazy(() => import("./MovieCard"));

export default function CardManager({ movies, id }) {
  return (
    <div id={id}>
      {movies.length > 0 ? (
        <Suspense fallback={Loader}>
          {movies.map((movie) => (
            <MovieCard key={movie.id} movie={movie} />
          ))}
        </Suspense>
      ) : (
        // <Loader />
        ""
      )}
    </div>
  );
}


function Loader() {
    return (
        <div id="loader"></div>
    );
}