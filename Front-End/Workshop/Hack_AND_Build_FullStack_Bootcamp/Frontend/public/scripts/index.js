document.addEventListener("DOMContentLoaded", async () => {
    const suggestionDiv = document.getElementById("suggestions_inner_div");
    const newReleaseDiv = document.getElementById("new-releases_inner_div");

    async function getResponse(url) {
        try {
            const response = await fetch(url);
            if (response.ok) {
                return await response.json();
            } else {
                console.error("Data not found:", await response.text());
                return { Data: [] };
            }
        } catch (err) {
            console.error("Error in data fetch", err);
            return { Data: [] };
        }
    }

    const recData = await getResponse("/movie/data/recommendations/");
    const segData = await getResponse("/movie/data/suggestions/");

    function setMovieSliders(list, parentDiv) {
        parentDiv.innerHTML = ""; 
        list.Data.forEach(movie => {
            try {
                let newDiv = document.createElement("div");
                let image = document.createElement("img");
                let title = document.createElement("p");
                let onHover = document.createElement("div")

                image.style.width = "100%";
                image.style.height = "200px";
                title.textContent = movie.Title || "Unknown";
                title.style.color = "#fff";
                title.style.fontSize = "14px";
                title.style.textAlign = "center";
                title.style.marginTop = "5px";
                let downloadingImage = new Image();
                downloadingImage.onload = function () {
                    image.src = this.src;
                    newDiv.appendChild(image);
                    newDiv.appendChild(title);
                    newDiv.addEventListener("mouseover", ()=> {
                        onHover
                    })
                    newDiv.style.display = "inline-block";
                    newDiv.style.width = "150px";
                    newDiv.style.height = "min-content";
                    newDiv.style.margin = "10px";
                    newDiv.style.textAlign = "center";
                    // onHover.style.backgroundColor = "red"
                    // onHover.style.zIndex = "999";
                    // onHover.style.width = "100%";
                    // onHover.style.height = "auto";
                    
                    // onHover.style.position = "absolute";

                    newDiv.appendChild(onHover)
                    parentDiv.appendChild(newDiv);
                };
                downloadingImage.src = movie.Poster;

                
            } catch (err) {
                console.error("Image error for:", movie.Title, err);
            }
        });
    }

    setMovieSliders(recData, newReleaseDiv);
    setMovieSliders(segData, suggestionDiv);
});
