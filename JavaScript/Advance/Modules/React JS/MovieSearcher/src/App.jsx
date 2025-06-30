import { useRef, useState, useEffect } from "react";
import { fetchMovieBySearch, fetchPopularMovies, fetchTopRatedMovies } from "./api/apidb.js";
import "./App.css";
import CardManager from "./Components/CardManager.jsx";

function App() {
  const [query, setQuery] = useState("Search");
  const [movies, setMovies] = useState([]);
  const [searching, setSearching] = useState(false)
  const [Popularmovies, setPopularmovies] = useState([]);
  const [TopRatedmovies, setTopRatedmovies] = useState([]);
  const [PagesManager, setPagesManager] = useState([])
  const [isSearchHidden, setIsSearchHidden] = useState(false);
  const [allMoviesData, setAllMoviesData] = useState([]);
  const [showNoResultsSVG, setShowNoResultsSVG] = useState(false);

  const searchContainerRef = useRef(null);
  const timeoutRef = useRef(null);

  const pages = setPagesManager({
    "TV": {
      "Popular": 1,
      "Top Rated": 1,
      "UpComing": 1,  
    },
    "Series": {
       "Popular": 1,
      "Top Rated": 1,
      "Airing": 1,
    },
    "Search": 1
  })

  const fetchMovies = async () => {
    const data = await fetchMovieBySearch(query);
    if (data && data.length > 0) {
      setMovies(data);
      setAllMoviesData([...allMoviesData, ...data]);
    } else {
      setMovies([]);
    }
  };
  const fetchPopular = async () => {
    const data = await fetchPopularMovies();
    if (data) {
      setPopularmovies(data)
      setAllMoviesData([...allMoviesData, ...data]);
    }
  }
  const fetchTopRated = async () => {
    const data = await fetchTopRatedMovies();
    if (data) {
      setTopRatedmovies(data)
      setAllMoviesData([...allMoviesData, ...data]);
    }
  }

  useEffect(() => {
    fetchPopular();
    fetchTopRated()
  }, []);
  const handleBlur = (e) => {
    if (e.target.value === "" || e.target.value === "Search" && !searching) {
      setQuery("Search");
      timeoutRef.current = setTimeout(() => {
        const el = searchContainerRef.current;
        el.classList.remove("slide-in");
        void el.offsetWidth;
        el.classList.add("slide-out");
        setIsSearchHidden(true);
      }, 1000);
    }
  };

  const handleFocus = (e) => {
    if (e.target.value === "Search" && !searching) setQuery("");
    if (timeoutRef.current) clearTimeout(timeoutRef.current);
  };

  useEffect(() => {
    const handleMouseMove = (e) => {
      if (isSearchHidden && e.clientY < 50) {
        const el = searchContainerRef.current;
        el.classList.remove("slide-out");
        void el.offsetWidth;
        el.classList.add("slide-in");
        setIsSearchHidden(false);
      }
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, [isSearchHidden]);

  return (
    <div id="main-section">
      <div id="top-section">
        <div id="info-top" style={{ opacity: isSearchHidden ? 1 : 0 }}>
          <p>Hover top for search bar</p>
        </div>
        <div id="tool-box-items">
          <div id="feature-box">
            <nav id="nav-content">
              <button className="nav-item" id="home-h" aria-label="Home">
                <svg viewBox="0 0 24 24" height="24px">
                  <path
                    fillRule="evenodd"
                    d="M17.8913288,10 L11.8900003,3.99867157 L5.88867192,10 L5.89001465,10 L5.89001465,20 L17.8900146,20 L17.8900146,10 L17.8913288,10 Z M19.8900146,11.9986859 L19.8900146,20 C19.8900146,21.1045695 18.9945841,22 17.8900146,22 L5.89001465,22 C4.78544515,22 3.89001465,21.1045695 3.89001465,20 L3.89001465,11.9986573 L2.41319817,13.4754737 L1,12.0622756 L10.4769858,2.5852898 C11.2573722,1.8049034 12.5226285,1.8049034 13.3030149,2.5852898 L22.7800007,12.0622756 L21.3668025,13.4754737 L19.8900146,11.9986859 Z"
                  />
                </svg>
              </button>
              <button className="nav-item" id="fav-h" aria-label="Favorites">
                <svg
                  fill="#000000"
                  width="24px"
                  height="24px"
                  viewBox="0 0 1000 1000"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path d="M47 43h553q10 0 16.5 7t6.5 16v29q0 9-6.5 16t-16.5 7H47q-10 0-17-7t-7-16V66q0-9 7-16t17-7zm0 139h553q10 0 16.5 7t6.5 17v28q0 10-6.5 16.5T600 257H47q-10 0-17-6.5T23 234v-28q0-10 7-17t17-7zm0 140h359q10 0 17 6.5t7 16.5v28q0 10-7 17t-17 7H47q-10 0-17-7t-7-17v-28q0-10 7-16.5t17-6.5zm0 139h153q10 0 16.5 7t6.5 16v29q0 9-6.5 16t-16.5 7H47q-10 0-17-7t-7-16v-29q0-9 7-16t17-7zm578 386l-151 79q-9 5-19.5 4t-19-7-12.5-16-3-20l29-168q4-19-10-32L317 568q-8-7-10.5-17.5t1-20.5 11.5-17 18-8l169-25q19-2 27-20l76-152q4-10 13-15.5t19.5-5.5 19.5 5.5 14 15.5l75 152q9 18 28 20l168 25q11 1 19 8t11 17 .5 20.5T967 568L845 687q-14 13-10 32l28 168q2 10-2 20t-12.5 16-19 7-20.5-4l-150-79q-17-9-34 0z" />
                </svg>
              </button>
            </nav>
          </div>
          <div
            ref={searchContainerRef}
            id="search-box-container"
            className="slide-in"
          >
            <input
              id="query-box"
              value={query}
              onFocus={handleFocus}
              onBlur={handleBlur}
              onChange={(e) => {
                setQuery(e.target.value)
                 if (e.target.value == ""){
                  setSearching(false)
                } else {
                  setSearching(true)
                }
              }}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  fetchMovies();
                  setShowNoResultsSVG(true);
                } else {
                    setShowNoResultsSVG(false);
                }
              }}
            />
          </div>
        </div>        
      </div>
      
      <div id="focus-area">
        {searching && (
          <div id="search-area">
            {movies.length > 0 ? (
              <>
                <h1 id="search-header"className="header-fields">Search Results</h1>
                <div id="search-results">
                  <CardManager movies={movies} id="search-results" />
                </div>
              </>
            ) : (
              <div id="no-results-found">
                <h1 className="header-fields">Search Results</h1>
                { (showNoResultsSVG && movies.length <= 0) && <svg width="125" height="125" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M21.5 14.75c.41 0 .75.34.75.75s-.34.75-.75.75-.75-.34-.75-.75.34-.75.75-.75m-11 0c.41 0 .75.34.75.75s-.34.75-.75.75-.75-.34-.75-.75.34-.75.75-.75" fill="#263238"/><g fill="none"><g stroke="#455A64"><path d="M21.5 1.5h-17v29h23v-23"/><path d="m21.5 1.5 5.979 6H21.5V4m-7 14.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5m3.25-3c0 .41.34.75.75.75s.75-.34.75-.75-.34-.75-.75-.75-.75.34-.75.75m-9.5 0c0 .41-.34.75-.75.75s-.75-.34-.75-.75.34-.75.75-.75.75.34.75.75"/></g><g stroke="#263238"><path d="M21.5 1.5h-17v29h23v-23"/><path d="m21.5 1.5 5.979 6H21.5V4m-7 14.5c0-.83.67-1.5 1.5-1.5s1.5.67 1.5 1.5m3.25-3c0 .41.34.75.75.75s.75-.34.75-.75-.34-.75-.75-.75-.75.34-.75.75m-9.5 0c0 .41-.34.75-.75.75s-.75-.34-.75-.75.34-.75.75-.75.75.34.75.75"/></g></g></svg>}
              </div>
            )}
          </div>
        )}
 
        <h1 className="header-fields">Popular Movies</h1>
        <div class="extra-space">
          <CardManager movies={Popularmovies} id="extra-space" />
        </div>

         <h1 className="header-fields">Top Rated</h1>
        <div class="extra-space">
          <CardManager movies={TopRatedmovies} id="extra-space" />
        </div>
    

      </div>

      
    </div>
  );
}

export default App;
