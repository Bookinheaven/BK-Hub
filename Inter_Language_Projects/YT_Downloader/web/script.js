// A defensive check to prevent a crash if 'value' is unexpectedly missing.
// This is not the root cause, but it makes the app more resilient.
// The root cause is likely a malformed message coming from the backend.
function initialize() {
    let currentMetadata = null;

    async function init() {
        const settings = await eel.get_initial_settings()();
        console.log(settings)
        if (settings && settings.value) { // Added a check for settings and settings.value
            document.getElementById('save-folder-input').value = settings.value.download_folder;
            document.getElementById('format-selector').value = settings.value.format;
            document.getElementById('bitrate-selector').value = settings.value.bitrate;
        }

        const setupResult = await eel.start_initial_setup()();
        if (setupResult && setupResult.status === "error") {
            update_status(`Setup Error: ${setupResult.message}`, "red");
        }
    }

    init();

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

    document.getElementById('fetch-button').addEventListener('click', async () => {
        const url = document.getElementById('url-input').value;
        if (!url) {
            update_status("Please enter a YouTube URL.", "red");
            return;
        }

        update_status("Fetching video information...", "blue");
        disableUI(true);

        const response = await eel.fetch_metadata(url)();

        if (!response || response.status === "error") { // Added a check for response
            update_status(`Error: ${response ? response.message : 'Unknown error.'}`, "red");
            disableUI(false);
        } else {
            currentMetadata = response.value;
            console.log(currentMetadata)
            if (currentMetadata.type === "playlist") {
                const videoCount = currentMetadata.metadata.length;
                update_status(`Found playlist with ${videoCount} videos. Click Download to start.`, "green");
                document.getElementById('metadata-container').classList.add('hidden');
                document.getElementById('download-button').classList.remove('hidden'); // Show download button for playlist
                document.getElementsByClassName('options-group')[0].classList.remove('hidden');
            } else {
                update_status("Metadata fetched successfully.", "green");
                const metadata = currentMetadata.metadata;
                document.getElementById('title-input').value = metadata.title;
                document.getElementById('artist-input').value = metadata.artist;
                document.getElementById('album-input').value = metadata.album;
                document.getElementById('thumbnail-preview').src = metadata.thumbnail_url;
                document.getElementById('metadata-container').classList.remove('hidden');
                document.getElementById('download-button').classList.remove('hidden');
                document.getElementsByClassName('options-group')[0].classList.remove('hidden');
            }

            document.getElementById('download-button').disabled = false;
            disableUI(false, true);
        }
    });

    document.getElementById('download-button').addEventListener('click', async () => {
        const url = document.getElementById('url-input').value;
        const saveFolder = document.getElementById('save-folder-input').value;
        const selectedFormat = document.getElementById('format-selector').value;
        const bitrate = document.getElementById('bitrate-selector').value;

        let metadata_to_send;
        if (currentMetadata.type === "video") {
            metadata_to_send = {
                title: document.getElementById('title-input').value,
                artist: document.getElementById('artist-input').value,
                album: document.getElementById('album-input').value
            };
        } else {
            metadata_to_send = currentMetadata.metadata[0];
        }

        disableUI(true);
        const result = await eel.download_music(url, metadata_to_send, saveFolder, selectedFormat, bitrate)();

        if (result && result.status === 'error') { // Added a check for result
            update_status(`Error: ${result.message}`, "red");
            disableUI(false);
        }
    });

    eel.expose(update_status);
    eel.expose(update_progress);
    eel.expose(update_button_state);
    eel.expose(update_progress_bar_visibility);
    eel.expose(disableUI);

    function update_status(message, color) {
        const statusMessage = document.getElementById('status-message');
        statusMessage.textContent = message;
        statusMessage.className = `status-message status-${color}`;
    }

    function update_progress(percent) {
        const progressBar = document.getElementById('progress-bar');
        progressBar.style.width = `${percent * 100}%`;
    }

    function update_button_state(state) {
        const downloadButton = document.getElementById('download-button');
        downloadButton.disabled = state;
    }

    function update_progress_bar_visibility(visible) {
        const progressBarContainer = document.getElementById('progress-bar-container');
        if (visible) {
            progressBarContainer.classList.remove('hidden');
        } else {
            progressBarContainer.classList.add('hidden');
        }
    }

    function disableUI(state, keep_download_enabled = false, keep_fetch_enabled = false) {
        document.getElementById('url-input').disabled = state;
        document.getElementById('browse-button').disabled = state;

        const fetchButton = document.getElementById('fetch-button');
        const loaderWrapper = document.getElementById('loader-wrapper');
        const loader = document.getElementsByClassName('loader')[0];
        const downloadButton = document.getElementById('download-button');

        fetchButton.disabled = state;
        downloadButton.disabled = state;

        if (state) {
            loaderWrapper.classList.remove("hidden");
            loader.classList.remove("hidden");
            document.body.style.overflow = "hidden";
        } else {
            loaderWrapper.classList.add("hidden");
            loader.classList.add("hidden");
            document.body.style.overflow = "";
        }
        if (!state) {
            fetchButton.textContent = "Fetch";
            downloadButton.textContent = "Download";
        }

        if (!keep_download_enabled) {
            downloadButton.disabled = state;
        }

        if (!keep_fetch_enabled) {
            fetchButton.disabled = state;
        }
    }
}
document.addEventListener('DOMContentLoaded', initialize);