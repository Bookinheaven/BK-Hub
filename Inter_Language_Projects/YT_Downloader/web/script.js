function initialize() {
    let currentMetadata = null;
    let localCoverFile = null; 
    let liveDownloads = {};

    eel.expose(update_status);
    eel.expose(update_button_state);
    eel.expose(disableUI); 
    eel.expose(resetUI);
    eel.expose(update_progress); 
    eel.expose(update_progress_bar_visibility);
    eel.expose(addLiveDownloadCard);
    eel.expose(updateLiveProgress);
    eel.expose(finishDownloadCard);
    eel.expose(addDownloadLogEntry);

    function update_status(message, color) {
        const statusMessage = document.getElementById('status-message');
        if (statusMessage) {
            statusMessage.textContent = message;
            statusMessage.className = `status-message status-${color}`;
        } else {
            console.warn("Status message element not found.");
        }
    }

    function update_progress(percent) {
        const progressBar = document.getElementById('progress-bar');
        if (progressBar) {
            progressBar.style.width = `${percent * 100}%`;
        } else {
            console.warn("Progress bar element not found.");
        }
    }

    function update_button_state(state) {
        const downloadButton = document.getElementById('download-button');
        if (downloadButton) {
            downloadButton.disabled = state;
        }
    }

    function update_progress_bar_visibility(visible) {
        const progressBarContainer = document.getElementById('progress-bar-container');
        if (progressBarContainer) {
            if (visible) {
                progressBarContainer.classList.remove('hidden');
            } else {
                progressBarContainer.classList.add('hidden');
            }
        } else {
            console.warn("Progress bar container element not found.");
        }
    }

    function disableUI(state, keep_download_enabled = false, keep_fetch_enabled = false) {
        const urlsInput = document.getElementById('urls-input');
        const browseButton = document.getElementById('browse-button');
        const fetchButton = document.getElementById('fetch-button');
        const downloadButton = document.getElementById('download-button');
        const loaderWrapper = document.getElementById('loader-wrapper');
        const loader = document.querySelector('.loader');

        if (urlsInput) urlsInput.disabled = state;
        if (browseButton) browseButton.disabled = state;
        if (fetchButton) fetchButton.disabled = state;
        if (downloadButton) downloadButton.disabled = state;

        if (state) {
            if (loaderWrapper) loaderWrapper.classList.remove("hidden");
            if (loader) loader.classList.remove("hidden");
            document.body.style.overflow = "hidden";
        } else {
            if (loaderWrapper) loaderWrapper.classList.add("hidden");
            if (loader) loader.classList.add("hidden");
            document.body.style.overflow = "";
        }

        if (!state) {
            if (fetchButton) fetchButton.textContent = "Fetch";
            if (downloadButton) downloadButton.textContent = "Download";
        }

        if (keep_download_enabled && downloadButton) {
            downloadButton.disabled = false;
        }

        if (keep_fetch_enabled && fetchButton) {
            fetchButton.disabled = false;
        }
    }

    function resetUI() {
        currentMetadata = null;
        localCoverFile = null;
        
        document.getElementById('urls-input').value = "";
        document.getElementById('title-input').value = "";
        document.getElementById('artist-input').value = "";
        document.getElementById('album-input').value = "";
        document.getElementById('genre-input').value = "";
        document.getElementById('year-input').value = "";
        document.getElementById('track-input').value = "";
        document.getElementById('thumbnail-preview').src = "";
        document.getElementById('cover-upload').value = null;
        
        document.getElementById('metadata-container').classList.add('hidden');
        document.getElementById('options-group').classList.add('hidden');
        document.getElementById('download-button').classList.add('hidden');
        
        const downloadLogSection = document.getElementById('download-log-section');
        const downloadLogContainer = document.getElementById('download-log-container');
        if (downloadLogSection) downloadLogSection.classList.add('hidden');
        if (downloadLogContainer) downloadLogContainer.innerHTML = "";
        
        const liveDownloadsContainer = document.getElementById('live-downloads-container');
        const downloadCardsContainer = document.getElementById('download-cards-container');
        if (liveDownloadsContainer) liveDownloadsContainer.classList.add('hidden');
        if (downloadCardsContainer) downloadCardsContainer.innerHTML = "";
        liveDownloads = {};

        update_status("Music is freedom, Dude!", "default");
        update_progress_bar_visibility(false);
        update_progress(0);
        
        disableUI(false);
    }
    
    function addLiveDownloadCard(id, metadata) {
        const liveContainer = document.getElementById('live-downloads-container');
        const cardsContainer = document.getElementById('download-cards-container');
        
        if (liveContainer && cardsContainer) {
            liveContainer.classList.remove('hidden');

            const card = document.createElement('div');
            card.classList.add('download-card');
            card.setAttribute('id', `card-${id}`);
            card.innerHTML = `
                <img src="${metadata.thumbnail_url}" alt="Thumbnail" class="card-thumbnail">
                <div class="card-details">
                    <p class="card-title">${metadata.title}</p>
                    <p class="card-artist">${metadata.artist}</p>
                    <div class="card-progress-bar-container">
                        <div class="card-progress-bar" style="width: 0%;"></div>
                    </div>
                </div>
            `;
            cardsContainer.prepend(card);
            liveDownloads[id] = card;
        } else {
            console.warn("Live download container elements not found.");
        }
    }
    
    function updateLiveProgress(id, percent) {
        const card = liveDownloads[id];
        if (card) {
            const progressBar = card.querySelector('.card-progress-bar');
            if (progressBar) {
                progressBar.style.width = `${percent * 100}%`;
            }
        }
    }
    
    function finishDownloadCard(id, metadata, path) {
        const card = liveDownloads[id];
        if (card) {
            const progressBarContainer = card.querySelector('.card-progress-bar-container');
            if (progressBarContainer) {
                progressBarContainer.remove();
            }

            const pathElement = document.createElement('p');
            pathElement.classList.add('card-path');
            pathElement.innerHTML = `Path: <span class="clickable-path" data-path="${path}">${path}</span>`;
            card.querySelector('.card-details').appendChild(pathElement);

            pathElement.querySelector('.clickable-path').addEventListener('click', () => {
                eel.openPathInExplorer(path);
            });
        }
        
        addDownloadLogEntry(metadata, path);
    }

    function addDownloadLogEntry(metadata, path) {
        const logContainer = document.getElementById('download-log-container');
        const logSection = document.getElementById('download-log-section');
        if (logContainer && logSection) {
            logSection.classList.remove('hidden');

            const entry = document.createElement('div');
            entry.classList.add('download-log-entry');
            entry.innerHTML = `
                <img src="${metadata.thumbnail_url}" alt="Thumbnail" class="log-thumbnail">
                <div class="log-details">
                    <p class="log-title">${metadata.title}</p>
                    <p class="log-artist">${metadata.artist}</p>
                    <p class="log-path">Path: <span class="clickable-path" data-path="${path}">${path}</span></p>
                </div>
            `;
            logContainer.prepend(entry);

            entry.querySelector('.clickable-path').addEventListener('click', () => {
                eel.openPathInExplorer(path);
            });
        } else {
            console.warn("Download log elements not found.");
        }
    }
    
    async function fetchVideoMetadata(url) {
        if (!url || url.trim() === "") {
            update_status("Please enter one or more YouTube URLs.", "red");
            return;
        }

        update_status("Fetching video information...", "blue");
        disableUI(true);

        const response = await eel.fetch_metadata(url)();

        if (!response || response.status === "error") {
            update_status(`Error: ${response ? response.message : 'Unknown error.'}`, "red");
            disableUI(false);
        } else {
            currentMetadata = response.value;

            const metadataContainer = document.getElementById('metadata-container');
            const downloadButton = document.getElementById('download-button');
            const optionsGroup = document.querySelector('.options-group');

            if (currentMetadata.type === "playlist") {
                const videoCount = currentMetadata.metadata.length;
                update_status(`Found playlist with ${videoCount} videos. Click Download to start.`, "green");
                if (metadataContainer) metadataContainer.classList.add('hidden');
                if (downloadButton) downloadButton.classList.remove('hidden');
                if (optionsGroup) optionsGroup.classList.remove('hidden');
            } else {
                update_status("Metadata fetched successfully.", "green");
                const metadata = currentMetadata.metadata;
                
                const titleInput = document.getElementById('title-input');
                const artistInput = document.getElementById('artist-input');
                const albumInput = document.getElementById('album-input');
                const genreInput = document.getElementById('genre-input');
                const yearInput = document.getElementById('year-input');
                const trackInput = document.getElementById('track-input');
                const thumbnailPreview = document.getElementById('thumbnail-preview');
                    
                if (titleInput) titleInput.value = metadata.title;
                if (artistInput) artistInput.value = metadata.artist;
                if (albumInput) albumInput.value = metadata.album;
                if (genreInput) genreInput.value = metadata.genre || '';
                if (yearInput) yearInput.value = metadata.year || '';
                if (trackInput) trackInput.value = metadata.track || '';
                if (thumbnailPreview) thumbnailPreview.src = metadata.thumbnail_url;
                
                if (metadataContainer) metadataContainer.classList.remove('hidden');
                if (downloadButton) downloadButton.classList.remove('hidden');
                if (optionsGroup) optionsGroup.classList.remove('hidden');
            }
            disableUI(false, true, true);
        }
    }
    
    async function init() {
        const settings = await eel.get_initial_settings()();
        if (settings && settings.value) {
            document.getElementById('save-folder-input').value = settings.value.download_folder;
            document.getElementById('format-selector').value = settings.value.format;
            document.getElementById('bitrate-selector').value = settings.value.bitrate;
        }
        const setupResult = await eel.start_initial_setup()();
        if (setupResult && setupResult.status === "error") {
            update_status(`Setup Error: ${setupResult.message}`, "red");
        }
    }
    
    function saveCurrentSettings() {
        const settings = {
            download_folder: document.getElementById('save-folder-input').value,
            format: document.getElementById('format-selector').value,
            bitrate: document.getElementById('bitrate-selector').value
        };
        eel.save_settings(settings);
    }
    
    document.getElementById('browse-button').addEventListener('click', async () => {
        const folderPath = await eel.browse_folder()();
        if (folderPath) {
            document.getElementById('save-folder-input').value = folderPath;
        }
    });

    document.getElementById('format-selector').addEventListener('change', saveCurrentSettings);
    document.getElementById('bitrate-selector').addEventListener('change', saveCurrentSettings);
    document.getElementById('save-folder-input').addEventListener('change', saveCurrentSettings);

    document.querySelectorAll('.custom-number-input').forEach(function(wrapper) {
        const input = wrapper.querySelector('input[type="number"]');
        const up = wrapper.querySelector('.arrow.up');
        const down = wrapper.querySelector('.arrow.down');
        up.addEventListener('click', function() {
            input.stepUp();
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });
        down.addEventListener('click', function() {
            input.stepDown();
            input.dispatchEvent(new Event('input', { bubbles: true }));
        });
    });

       const genres = [
            "Pop", "Rock", "Hip-Hop", "Jazz", "Classical", "Electronic", "Country", "Reggae", "Blues", "Metal", "Folk",
            "R&B", "Soul", "Dance", "Indie", "Soundtrack", "Alternative", "Punk", "Disco", "Gospel", "K-Pop", "Latin",
            "Trap", "EDM", "House", "Techno", "Dubstep", "Ambient", "Trance", "Ska", "Grunge", "Emo", "Hardcore",
            "Progressive Rock", "Opera", "Children's Music", "World", "New Age", "Chillout", "Lo-fi", "Synthwave",
            "J-Pop", "Anime", "Holiday", "Christian", "Comedy", "Spoken Word", "Acoustic", "Instrumental", "Bluegrass",
            "Motown", "Swing", "Big Band", "Easy Listening", "Experimental", "Industrial", "Garage", "Shoegaze",
            "Post-Rock", "Reggaeton", "Afrobeat", "Salsa", "Bossa Nova", "Flamenco", "Celtic", "Marching Band",
            "Drum & Bass", "Breakbeat", "Electro", "Funk", "Grime", "Hardstyle", "Krautrock", "Latin Jazz", "Mariachi",
            "Merengue", "Polka", "Samba", "Tango", "Zydeco", "Chiptune", "Vaporwave", "Future Bass", "Glitch Hop",
            "Math Rock", "Noise", "Post-Punk", "Shoegaze", "Soca", "Swing", "Synthpop", "Traditional", "UK Garage"
        ];

        const datalist = document.createElement('datalist');
        datalist.id = "genre-suggestions";
        genres.forEach(genre => {
            const option = document.createElement('option');
            option.value = genre;
            datalist.appendChild(option);
        });
        document.body.appendChild(datalist);
    document.getElementById('fetch-button').addEventListener('click', async () => {
        const urls = document.getElementById('urls-input').value;
        await fetchVideoMetadata(urls);
    });

    document.getElementById('cover-upload').addEventListener('change', (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                localCoverFile = e.target.result.split(',')[1];
                document.getElementById('thumbnail-preview').src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    document.getElementById('download-button').addEventListener('click', async () => {
        const urls = document.getElementById('urls-input').value;
        const saveFolder = document.getElementById('save-folder-input').value;
        const selectedFormat = document.getElementById('format-selector').value;
        const bitrate = document.getElementById('bitrate-selector').value;

        if (!urls || urls.trim() === "") {
            update_status("Error: No URL(s) provided.", "red");
            return;
        }

        let metadata_to_send;
        
        const yearValue = document.getElementById('year-input').value;
        const year = yearValue ? new Date(yearValue).getFullYear().toString() : '';

        if (currentMetadata.type === "video") {
            metadata_to_send = {
                title: document.getElementById('title-input').value,
                artist: document.getElementById('artist-input').value,
                album: document.getElementById('album-input').value,
                genre: document.getElementById('genre-input').value,
                year: year,
                track: document.getElementById('track-input').value,
                cover_data: localCoverFile
            };
        } else {
            metadata_to_send = {
                album: document.getElementById('album-input').value,
                genre: document.getElementById('genre-input').value,
                year: year,
                cover_data: localCoverFile
            };
        }
        
        const liveContainer = document.getElementById('live-downloads-container');
        if (liveContainer) liveContainer.classList.remove('hidden');

        disableUI(true);
        const result = await eel.download_music(urls, metadata_to_send, saveFolder, selectedFormat, bitrate)();

        if (result && result.status === 'error') {
            update_status(`Error: ${result.message}`, "red");
            disableUI(false);
        }
    });
    
    init()
}

document.addEventListener('DOMContentLoaded', initialize);