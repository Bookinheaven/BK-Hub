import { Suspense, lazy, useRef, Fragment, useCallback } from "react";
import "./CardManager.css";

const MovieCard = lazy(() => import("./MovieCard"));

export default function CardManager({ movies, onEndFetch, type, favoritesList, setFavoritesList }) {
  const observerRef = useRef(null);

  const endRefCallback = useCallback((node) => {
    if (observerRef.current) {
      observerRef.current.disconnect();
    }
    if (node) {
      const observer = new IntersectionObserver(
        (entries) => {
          if (entries[0].isIntersecting) {
            onEndFetch(type);
          }
        },
        { threshold: 0.1 }
      );
      observer.observe(node);
      observerRef.current = observer;
    }
  }, []);

  return (
    <>
      {movies.length > 0 ? (
        <Suspense fallback={<Loader />}>
          {movies.map((movie, index) => (
            <Fragment key={movie.id}>
              {index === movies.length - 10 ? (
                <div ref={endRefCallback} style={{ minHeight: "1px" }}>
                  <MovieCard 
                    movie={movie} 
                    favoritesList={favoritesList}
                    setFavoritesList={setFavoritesList}
                    />
                </div>
              ) : (
                <MovieCard 
                  movie={movie}
                  favoritesList={favoritesList}
                  setFavoritesList={setFavoritesList}
                />
              )}
            </Fragment>
          ))}
        </Suspense>
      ) : (
        ""
        // <Loader />
      )}
    </>
  );
}

function Loader() {
  return <div id="loader"></div>;
}
