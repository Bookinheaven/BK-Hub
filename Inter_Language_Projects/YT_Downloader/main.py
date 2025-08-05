import eel
import os
import threading
import json
import yt_dlp
import shutil
import re
from tkinter import filedialog, Tk
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
import urllib.request
import zipfile
import tempfile

class MusicDownloader:
    """The Python backend for the music downloader application."""
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()
        self.app_dir = os.path.dirname(os.path.abspath(__file__))
        self.settings_file = os.path.join(self.app_dir, "config.json")
        self.settings = self._load_settings()

        self.ffmpeg_path = os.path.join(self.app_dir, "ffmpeg.exe")
        self.ffprobe_path = os.path.join(self.app_dir, "ffprobe.exe")
        self.download_queue = []
        self.is_playlist = False
        
    def _load_settings(self):
        """Loads user settings from a local configuration file."""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, "r") as f:
                    settings = json.load(f)
            else:
                settings = {
                    "download_folder": os.path.join(os.path.expanduser("~"), "Downloads"),
                    "format": "m4a",
                    "bitrate": "192k",
                }
        except Exception as e:
            print(f"Error loading settings, using defaults: {e}")
            settings = {
                "download_folder": os.path.join(os.path.expanduser("~"), "Downloads"),
                "format": "m4a",
                "bitrate": "192k",
            }
        return settings

    def _save_settings(self, settings):
        """Saves user settings to a local configuration file."""
        try:
            with open(self.settings_file, "w") as f:
                json.dump(settings, f, indent=4)
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    def _download_ffmpeg_if_needed(self):
        """Downloads and extracts FFmpeg binaries if they don't exist."""
        try:
            if os.path.isfile(self.ffmpeg_path) and os.path.isfile(self.ffprobe_path):
                eel.update_status("FFmpeg and FFprobe found. Ready.", "green")
                return {"status": "success", 'value': None}

            def download_in_thread():
                eel.update_status("FFmpeg not found. Downloading and extracting...", "yellow")
                ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
                download_path = os.path.join(self.app_dir, "ffmpeg.zip")
                try:
                    urllib.request.urlretrieve(ffmpeg_url, download_path)
                    eel.update_status("FFmpeg downloaded. Extracting...", "yellow")
                    with zipfile.ZipFile(download_path, 'r') as zip_ref:
                        zip_ref.extractall(self.app_dir)
                    os.remove(download_path)
                    extracted_folder = next(f for f in os.listdir(self.app_dir) if f.startswith('ffmpeg-master-latest'))
                    extracted_bin_path = os.path.join(self.app_dir, extracted_folder, 'bin')
                    if os.path.exists(extracted_bin_path):
                        shutil.copy(os.path.join(extracted_bin_path, 'ffmpeg.exe'), self.ffmpeg_path)
                        shutil.copy(os.path.join(extracted_bin_path, 'ffprobe.exe'), self.ffprobe_path)
                    shutil.rmtree(os.path.join(self.app_dir, extracted_folder))
                    eel.update_status("FFmpeg setup complete!", "green")
                except Exception as e:
                    eel.update_status(f"Error setting up FFmpeg: {e}", "red")
                finally:
                    eel.update_button_state(False)
            
            eel.update_button_state(True)
            threading.Thread(target=download_in_thread, daemon=True).start()
            return {"status": "in_progress", 'value': None}

        except Exception as e:
            eel.update_status(f"Critical error during setup: {e}", "red")
            return {"status": "error", "message": str(e), 'value': None}

    def _sanitize_filename(self, filename):
        """Sanitizes a string to be a valid filename."""
        sanitized = re.sub(r'[\\/:*?"<>|]', '', filename)
        return sanitized

    def _download_single_video(self, url, metadata, save_folder, output_format, bitrate, current_count=1, total_count=1):
        """Downloads a single video and processes its metadata."""
        temp_dir = None
        try:
            eel.update_status(f"Downloading {current_count}/{total_count}: '{metadata['title']}'...", "blue")
            eel.update_progress_bar_visibility(True)
            
            temp_dir = tempfile.mkdtemp()
            filename = f"{self._sanitize_filename(metadata['title'])} - {self._sanitize_filename(metadata['artist'])}"
            out_path = os.path.join(temp_dir, f'{filename}.%(ext)s')

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': out_path,
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio', 'preferredcodec': output_format, 'preferredquality': bitrate[:-1]},
                    {'key': 'EmbedThumbnail'},
                ],
                'ffmpeg_location': self.ffmpeg_path,
                'writethumbnail': True,
                'noplaylist': True,
                'geo_bypass': True,
                'progress_hooks': [self._progress_hook],
                'quiet': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                
                file_path_without_ext = os.path.splitext(ydl.prepare_filename(info_dict))[0]
                final_file_path = f"{file_path_without_ext}.{output_format}"
                thumbnail_path = f"{file_path_without_ext}.webp"
                
                self._add_metadata(final_file_path, thumbnail_path, output_format, metadata)

            final_destination = os.path.join(save_folder, os.path.basename(final_file_path))
            shutil.move(final_file_path, final_destination)
            
            eel.update_status(f"Download of '{metadata['title']}' complete!", "green")
            eel.update_progress_bar_visibility(False)
            
        except yt_dlp.DownloadError as e:
            print(f"DownloadError: {e}")
            eel.update_status(f"Download failed for '{metadata['title']}': {e}", "red")
        except Exception as e:
            print(f"Download Error: {e}")
            eel.update_status(f"Error with '{metadata['title']}': {e}", "red")
        finally:
            if temp_dir and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
            eel.update_progress(0)
            # Call disableUI from the backend after a successful or failed download
            eel.disableUI(False)

    def _download_playlist_thread(self, save_folder, output_format, bitrate):
        """Downloads all videos in the download queue."""
        try:
            total_count = len(self.download_queue)
            for i, video in enumerate(self.download_queue):
                self._download_single_video(
                    url=video['url'], 
                    metadata=video, 
                    save_folder=save_folder, 
                    output_format=output_format, 
                    bitrate=bitrate, 
                    current_count=i + 1, 
                    total_count=total_count
                )
            
            eel.update_status("Playlist download finished!", "green")
        except Exception as e:
            print(f"Playlist download error: {e}")
            eel.update_status(f"An error occurred during playlist download: {e}", "red")
        finally:
            eel.update_button_state(False)
            # Call disableUI from the backend after a playlist download
            eel.disableUI(False)

    def _add_metadata(self, file_path, thumbnail_path, output_format, metadata):
        """Adds or updates metadata to an audio file."""
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            return

        try:
            if output_format == "m4a":
                audio_file = MP4(file_path)
                audio_file["\xa9nam"] = [metadata['title']]
                audio_file["\xa9ART"] = [metadata['artist']]
                audio_file["\xa9alb"] = [metadata['album']]
                if os.path.isfile(thumbnail_path):
                    with open(thumbnail_path, "rb") as img_file:
                        audio_file.tags["covr"] = [MP4Cover(img_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]
                audio_file.save()
            elif output_format == "mp3":
                audio_file = MP3(file_path, ID3=ID3)
                audio_file.tags.add(TIT2(encoding=3, text=metadata['title']))
                audio_file.tags.add(TPE1(encoding=3, text=metadata['artist']))
                audio_file.tags.add(TALB(encoding=3, text=metadata['album']))
                if os.path.isfile(thumbnail_path):
                    with open(thumbnail_path, "rb") as img_file:
                        audio_file.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img_file.read()))
                audio_file.save()
            elif output_format == "flac":
                audio_file = FLAC(file_path)
                audio_file['title'] = metadata['title']
                audio_file['artist'] = metadata['artist']
                audio_file['album'] = metadata['album']
                if os.path.isfile(thumbnail_path):
                    with open(thumbnail_path, "rb") as img_file:
                        picture = Picture()
                        picture.data = img_file.read()
                        picture.mime = "image/jpeg"
                        audio_file.add_picture(picture)
                audio_file.save()
            elif output_format == "wav":
                eel.update_status("WAV files do not support metadata. Skipping.", "yellow")
        
        except Exception as e:
            print(f"Error adding metadata: {e}")
            eel.update_status(f"Error adding metadata: {e}", "red")
        finally:
            pass

    def _progress_hook(self, d):
        """Handles download progress updates and sends them to the UI."""
        if d['status'] == 'downloading':
            try:
                percent_str = d.get('_percent_str', '0.0%')
                cleaned_percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str)
                speed_str = d.get('_speed_str', '0 B/s')
                
                if '%' in cleaned_percent_str:
                    percent = float(cleaned_percent_str.strip('%').strip()) / 100
                    eel.update_progress(percent)
                    eel.update_status(f"Downloading: {cleaned_percent_str} at {speed_str}", "blue")
                else:
                    eel.update_status(f"Downloading: {percent_str} at {speed_str}", "blue")
            except (ValueError, KeyError) as e:
                print(f"Error parsing progress hook data: {e} - Data: {d}")
                eel.update_status("Download in progress...", "blue")
        elif d['status'] == 'finished':
            eel.update_status("Download complete! Adding metadata...", "blue")
            eel.update_progress(1)

app = MusicDownloader()

@eel.expose
def get_initial_settings():
    """Returns the initial settings to the frontend."""
    try:
        return {"status": "success", "value": app.settings}
    except Exception as e:
        print(f"Error in get_initial_settings: {e}")
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def save_settings(settings):
    """Saves the provided settings to the config file."""
    try:
        app._save_settings(settings)
        return {"status": "success", 'value': None}
    except Exception as e:
        print(f"Error in save_settings: {e}")
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def browse_folder():
    """Opens a folder selection dialog and returns the selected path."""
    try:
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            app.settings['download_folder'] = folder_selected
            app._save_settings(app.settings)
        return folder_selected if folder_selected else ""
    except Exception as e:
        print(f"Error in browse_folder: {e}")
        return ""

@eel.expose
def fetch_metadata(url):
    """Fetches video metadata and thumbnail for a given YouTube URL or playlist."""
    try:
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            
            if info_dict:
                if 'entries' in info_dict:
                    app.is_playlist = True
                    app.download_queue = []
                    for entry in info_dict['entries']:
                        if entry and entry.get('url'):
                            app.download_queue.append({
                                'title': entry.get('title', 'Unknown Title'),
                                'artist': entry.get('uploader', 'Unknown Artist'),
                                'album': info_dict.get('title', 'Unknown Album'),
                                'thumbnail_url': entry.get('thumbnail', ''),
                                'url': entry.get('url', ''),
                            })
                    return {"status": "success", "value": {"type": "playlist", "metadata": app.download_queue}}
                else:
                    app.is_playlist = False
                    metadata = {
                        'title': info_dict.get('title', 'Unknown Title'),
                        'artist': info_dict.get('uploader', 'Unknown Artist'),
                        'album': info_dict.get('album', 'Unknown Album'),
                        'thumbnail_url': info_dict.get('thumbnail', ''),
                        'url': url,
                    }
                    app.download_queue = [metadata]
                    return {"status": "success", "value": {"type": "video", "metadata": metadata}}
            else:
                return {'status': 'error', 'value': None, 'message': 'Could not fetch video information.'}
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return {'status': 'error', 'value': None, 'message': str(e)}

@eel.expose
def download_music(url, metadata, save_folder, selected_format, bitrate):
    """Starts the download process in a new thread."""
    try:
        if not os.path.exists(save_folder):
            return {"status": "error", "value": None, "message": "Save folder does not exist."}
        
        if app.is_playlist:
            download_thread = threading.Thread(
                target=app._download_playlist_thread,
                args=(save_folder, selected_format, bitrate),
                daemon=True
            )
        else:
            download_thread = threading.Thread(
                target=app._download_single_video,
                args=(app.download_queue[0]['url'], app.download_queue[0], save_folder, selected_format, bitrate),
                daemon=True
            )
        download_thread.start()

        return {"status": "success", "value": None, "message": "Download process started."}
    except Exception as e:
        print(f"Error in download_music: {e}")
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def start_initial_setup():
    """Starts the initial setup tasks like checking for FFmpeg."""
    try:
        return app._download_ffmpeg_if_needed()
    except Exception as e:
        return {"status": "error", "value": None, "message": str(e)}

if __name__ == "__main__":
    eel.init("web")
    try:
        eel.start("index.html", size=(950, 700), mode='edge', host='localhost', block=True)
    except Exception as e:
        print(f"Error starting Eel: {e}")