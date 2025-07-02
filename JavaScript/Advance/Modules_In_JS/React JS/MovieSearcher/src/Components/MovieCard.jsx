import "../App.css";
import "./MovieCard.css"
import { isInFavorites, toggleFavorite } from "../utils/General";

export default function MovieCard({ movie, favoritesList, setFavoritesList}) {

  return (
    <div className="movie-card" id={movie.id}>
        <div id="fav-icon">
          <button
            id={`fav-btn-${movie.id}`}
            className={`fav-btn ${favoritesList && isInFavorites(movie, favoritesList.Movies) ? "isfav" : "isNTfav"}`}
            onClick={() => toggleFavorite(movie, "Movies", setFavoritesList)}
            title={isInFavorites(movie, favoritesList.Movies) ? "Unfavorite" : "Add to Favorites"}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="28"
              height="28"
              viewBox="0 0 24 24"
              fill={isInFavorites(movie, favoritesList.Movies) ? "red" : "none"}
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 
                7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
            </svg>
          </button>
        </div>
      <img loading="lazy" src={movie.poster !== "" ? movie.poster : "/no-image.png"} alt={movie.title} />
      <div id="title-wrapper">
        <h3>{movie.title} ({movie.year})</h3>
      </div>
    </div>
  );
}


