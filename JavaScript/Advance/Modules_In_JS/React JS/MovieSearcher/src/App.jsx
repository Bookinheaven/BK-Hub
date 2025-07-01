import { useRef, useState, useEffect } from "react";
import {
  fetchMovieBySearch,
  fetchPopularMS,
  fetchTopRatedMS,
  fetchUpcomingMovies,
} from "./api/apidb.js";
import "./App.css";
import CardManager from "./Components/CardManager.jsx";
import { deduplicateMovies } from "./utils/General.js";
import browserSvg from './assets/browser.svg';

function App() {
  const [query, setQuery] = useState("Search");
  const [movies, setMovies] = useState([]);

  const [Popularmovies, setPopularmovies] = useState([]);
  const [PopularSeries, setPopularSeries] = useState([]);
  const [TopRatedMovies, setTopRatedMovies] = useState([]);
  const [TopRatedSeries, setTopRatedSeries] = useState([]);
  const [UpcomingMovies, setUpcomingMovies] = useState([]);

  const [PagesManager, setPagesManager] = useState({});
  const [allMoviesData, setAllMoviesData] = useState([]);
  const [favoritesList, setFavoritesList] = useState({});

  const [showNoResultsSVG, setShowNoResultsSVG] = useState(false);
  const [prevSearch, setPrevSearch] = useState("");
  const [isSearchHidden, setIsSearchHidden] = useState(false);
  const [searching, setSearching] = useState(false);

  const [inFavs, setInFavs] = useState(false)
  
  const searchContainerRef = useRef(null);
  const timeoutRef = useRef(null);
  const favRef = useRef(null);

  const pages = {
    Series: {
      Popular: 1,
      "Top Rated": 1,
      Airing: 1,
    },
    Movies: {
      Popular: 1,
      "Top Rated": 1,
      UpComing: 1,
    },
    Search: [1, 1],
  };

  const debounceRef = useRef(null);

  const handleInput = (e) => {
    setQuery(e.target.value);
    if (e.target.value.trim() === "") {
      setSearching(false);
      setShowNoResultsSVG(false);
    } else {
      setSearching(true);
    }
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      fetchMovies();
    }, 500);
  };

  useEffect(() => {
    if (searching) {
      document.body.classList.add("no-scroll");
    } else {
      document.body.classList.remove("no-scroll");
    }
  }, [searching]);

    useEffect(() => {
    if (inFavs) {
      document.body.classList.add("no-scroll");
      document.getElementById("home-h").style.backgroundColor = "transparent"
      document.getElementById("fav-h").style.backgroundColor = "rgba(240, 248, 255, 0.192)"

    } else {
      document.body.classList.remove("no-scroll");
      document.getElementById("home-h").style.backgroundColor = "rgba(240, 248, 255, 0.192)"
      document.getElementById("fav-h").style.backgroundColor = "transparent"

    }
  }, [inFavs]);

  const fetchMovies = async () => {
    if (query !== prevSearch) {
      setPrevSearch(query);
      pages.Search[0] = 1;
      setMovies([]);
    }
    const data = await fetchMovieBySearch(query, pages.Search);
    pages.Search[1] = data[1];
    if (
      Array.isArray(data[0]) &&
      data[0].length > 0 &&
      pages.Search[0] <= pages.Search[1]
    ) {
      setShowNoResultsSVG(false);
      const uniqueNew = deduplicateMovies(data[0]);
      setMovies((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      setAllMoviesData((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      pages.Search[0]++;
    } else if (movies.length == 0) {
      setShowNoResultsSVG(true);
      setMovies([]);
    }
  };
  const fetchPopular = async (type) => {
    const data = await fetchPopularMS(pages[type]["Popular"], type);
    if (data && Array.isArray(data)) {
      const uniqueNew = deduplicateMovies(data);
      if (type == "Movies") {
        setPopularmovies((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      } else {
        setPopularSeries((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      }
      setAllMoviesData((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      pages[type]["Popular"]++;
    }
  };
  
  const fetchTopRated = async (type) => {
    const data = await fetchTopRatedMS(pages[type]["Top Rated"], type);
    if (data && Array.isArray(data)) {
      const uniqueNew = deduplicateMovies(data);
      if (type == "Movies") {
        setTopRatedMovies((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      } else {
        setTopRatedSeries((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      }
      setAllMoviesData((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      pages[type]["Top Rated"]++;
    }
  };

  const fetchUpcoming = async () => {
    const data = await fetchUpcomingMovies(pages.Movies.UpComing);
    if (data && Array.isArray(data)) {
      const uniqueNew = deduplicateMovies(data);
      setUpcomingMovies((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      setAllMoviesData((prev) => deduplicateMovies([...prev, ...uniqueNew]));
      pages.Movies.UpComing++;
    }
  };

  useEffect(() => {
    fetchPopular("Movies");
    fetchPopular("Series");
    fetchTopRated("Movies");
    fetchTopRated("Series");
    fetchUpcoming();
  }, []);

  const handleBlur = (e) => {
    if (e.target.value === "" || (e.target.value === "Search" && !searching)) {
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

  function toggleFavPage() {
    const favArea = document.getElementById("fav-area");

    if (inFavs) {
      favArea.classList.remove("show");
      favArea.classList.add("hide");
      setInFavs(false);
    } else {
      favArea.classList.remove("hide");
      favArea.classList.add("show");
      setInFavs(true);
    }
  }
  function onClickForHome() {
    document.getElementById("fav-area").classList.remove("show")
    document.getElementById("fav-area").classList.add("hide")
    setInFavs(false)
  }

  return (
    <div id="main-section">
      <div id="top-section">
        <div id="info-top" style={{ opacity: isSearchHidden ? 1 : 0 }}>
          <p>Hover top for search bar</p>
        </div>
        <div id="tool-box-items">
          <div id="feature-box">
            <nav id="nav-content">
              <button className="nav-item" id="home-h" aria-label="Home" onClick={onClickForHome} >
                <svg viewBox="0 0 24 24" height="24px">
                  <path
                    fillRule="evenodd"
                    d="M17.8913288,10 L11.8900003,3.99867157 L5.88867192,10 L5.89001465,10 L5.89001465,20 L17.8900146,20 L17.8900146,10 L17.8913288,10 Z M19.8900146,11.9986859 L19.8900146,20 C19.8900146,21.1045695 18.9945841,22 17.8900146,22 L5.89001465,22 C4.78544515,22 3.89001465,21.1045695 3.89001465,20 L3.89001465,11.9986573 L2.41319817,13.4754737 L1,12.0622756 L10.4769858,2.5852898 C11.2573722,1.8049034 12.5226285,1.8049034 13.3030149,2.5852898 L22.7800007,12.0622756 L21.3668025,13.4754737 L19.8900146,11.9986859 Z"
                  />
                </svg>
              </button>
              <button className="nav-item" id="fav-h" aria-label="Favorites" onClick={toggleFavPage}>
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
              onChange={handleInput}
              autoComplete="off"
            />
          </div>
        </div>
      </div>
      
      <div id="fav-area" ref={favRef} className="hide">
        <h1 className="header-fields">Favorites</h1>
        
      </div>
      <div id="focus-area">
        {searching && (
          <>
            <div className="backdrop" />
            <div id="search-area">
              <h1 id="search-header" className="header-fields">
                Search Results
              </h1>

              {movies.length > 0 ? (
                <>
                  <h1 className="header-fields" style={{margin:0}}>Movies</h1><br></br>
                  <div className="search-results">
                    <CardManager
                      movies={movies}
                      id="search-results"
                      onEndFetch={fetchMovies}
                    />
                  </div>
                </>

              ) : showNoResultsSVG ? (
                <>
                  {console.log("Rendering: No Results Found block")}
                  <div id="no-results-found">
                    <h2 className="header-fields" style={{fontSize: "2rem"}}>Sorry I couldn't find "{query}" movie/series in the database. Please try something else.</h2>
                      <img src={browserSvg} alt="Not Found" />
                  </div>
                </>
              ) : (
                  <dir id="loader"></dir>
              )}
            </div>
          </>
        )}
        <h1 className="header-fields" style={{ fontSize: "3.5rem" }}>
          Movies
        </h1>

        <h1 className="header-fields">Popular Movies</h1>
        <div className="extra-space">
          <CardManager
            movies={Popularmovies}
            id="extra-space"
            onEndFetch={fetchPopular}
            type={"Movies"}
          />
        </div>

        <h1 className="header-fields">Top Rated Movies</h1>
        <div className="extra-space">
          <CardManager
            movies={TopRatedMovies}
            id="extra-space"
            onEndFetch={fetchTopRated}
            type={"Movies"}
          />
        </div>

        <h1 className="header-fields">Upcoming Movies</h1>
        <div className="extra-space">
          <CardManager
            movies={UpcomingMovies}
            id="extra-space"
            onEndFetch={fetchUpcoming}
          />
        </div>

        <h1 className="header-fields" style={{ fontSize: "3.5rem" }}>
          Series
        </h1>
        <h1 className="header-fields">Popular Series</h1>
        <div className="extra-space">
          <CardManager
            movies={PopularSeries}
            id="extra-space"
            onEndFetch={fetchPopular}
            type={"Series"}
          />
        </div>
        <h1 className="header-fields">Top Rated Series</h1>
        <div className="extra-space">
          <CardManager
            movies={TopRatedSeries}
            id="extra-space"
            onEndFetch={fetchTopRated}
            type={"Series"}
          />
        </div>

        <footer id="footer">
            <p className="footer-text">© 2025 BookInHeaven. All rights reserved.</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
