import "../App.css";
import "./MovieCard.css"
export default function MovieCard({ movie }) {
  return (
    <div className="movie-card">
        {console.log(movie)}
        <div id="fav-icon">
            <button className="fav-btn"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-heart"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>
        </div>
      <img loading="lazy" src={movie.Poster !== "N/A" ? movie.Poster : "/no-image.png"} alt={movie.Title} />
      <div className="movie-title-scroll">
        <h3>{movie.Title} ({movie.Year})</h3>
      </div>
      <p className="movie-type">{movie.Type}</p>
    </div>
  );
}
