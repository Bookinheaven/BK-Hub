import subprocess
import sys

def _update_modules_in_thread():
    """Checks for and updates Python modules in a new thread."""
    try:
        eel.update_status("Checking for module updates...", "yellow")

        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        modules_to_update = ["eel", "yt-dlp", "mutagen", "gevent", "gevent-websocket", "Pillow", "pyinstaller"]
        
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade"] + modules_to_update,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        eel.update_status("Modules updated successfully.", "green")
    except Exception as e:
        _handle_error("Error during module update. Check your internet connection.", e)

import eel
import os
import threading
import json
import yt_dlp
import shutil
import re
import random
import string 

from tkinter import filedialog, Tk
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, TYER, TRCK, APIC
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
import urllib.request
import zipfile
import tempfile
import base64
import traceback
import multiprocessing

if getattr(sys, 'frozen', False):
    app_base_path = os.path.dirname(sys.executable)
else:
    app_base_path = os.path.dirname(os.path.abspath(__file__))

settings_file = os.path.join(app_base_path, "config.json")
ffmpeg_path = os.path.join(app_base_path, "ffmpeg.exe")
ffprobe_path = os.path.join(app_base_path, "ffprobe.exe")
is_playlist = False
settings = {}
live_download_progress = {}

def _handle_error(message, error, is_critical=False):
    """Centralized error handling and reporting."""
    print("--- Python Error ---")
    print(f"Error: {message}")
    print("Traceback:")
    traceback.print_exc()
    print("--------------------")
    if is_critical:
        eel.update_status(f"Critical Error: {message}. See console for details.", "red")
    else:
        eel.update_status(f"Warning: {message}", "yellow")
def _load_settings():
    """Loads user settings from a local configuration file."""
    import os, json
    global settings
    try:
        if os.path.exists(settings_file):
            with open(settings_file, "r") as f:
                settings = json.load(f)
        else:
            download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
            settings = {
                "download_folder": download_folder,
                "cookies": os.path.join(download_folder, "cookies.txt"),
                "format": "m4a",
                "bitrate": "320k",
            }
        print(settings["cookies"])
    except Exception as e:
        _handle_error("Error loading settings, using defaults.", e)
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        settings = {
            "download_folder": download_folder,
            "cookies": os.path.join(download_folder, "cookies.txt"),
            "format": "m4a",
            "bitrate": "320k",
        }


def _save_settings():
    """Saves user settings to a local configuration file."""
    try:
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        _handle_error(f"Error saving settings: {e}", e)

def _sanitize_filename(filename):
    """Sanitizes a string to be a valid filename."""
    sanitized = re.sub(r'[\\/:*?"<>|]', '', filename)
    return sanitized

def _progress_hook_for_live_card(d, download_id):
    """Handles download progress updates for a live card."""
    if d['status'] == 'downloading':
        try:
            percent_str = d.get('_percent_str', '0.0%')
            cleaned_percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str)
            if '%' in cleaned_percent_str:
                percent = float(cleaned_percent_str.strip('%').strip()) / 100
                eel.updateLiveProgress(download_id, percent)
                live_download_progress[download_id] = percent
        except (ValueError, KeyError) as e:
            _handle_error(f"Error parsing progress hook data: {e}", e)
    elif d['status'] == 'finished':
        eel.updateLiveProgress(download_id, 1)

def _add_metadata(file_path, thumbnail_path, output_format, metadata):
    """Adds or updates metadata to an audio file."""
    if not os.path.isfile(file_path):
        _handle_error(f"File not found: {file_path}", FileNotFoundError())
        return

    try:
        common_tags = {
            'title': metadata.get('title', ''),
            'artist': metadata.get('artist', ''),
            'album': metadata.get('album', ''),
            'genre': metadata.get('genre', ''),
            'year': str(metadata.get('year', '')),
            'track': str(metadata.get('track', ''))
        }

        cover_data = None
        if os.path.isfile(thumbnail_path):
            with open(thumbnail_path, "rb") as img_file:
                cover_data = img_file.read()
        
        if output_format == "m4a":
            audio_file = MP4(file_path)
            audio_file["\xa9nam"] = [common_tags['title']]
            audio_file["\xa9ART"] = [common_tags['artist']]
            audio_file["\xa9alb"] = [common_tags['album']]
            audio_file["\xa9gen"] = [common_tags['genre']]
            audio_file["\xa9day"] = [common_tags['year']]
            if common_tags['track'] and common_tags['track'].isdigit():
                audio_file["trkn"] = [(int(common_tags['track']), 0)]
            if cover_data:
                audio_file.tags["covr"] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]
            audio_file.save()
        elif output_format == "mp3":
            audio_file = MP3(file_path, ID3=ID3)
            audio_file.tags.add(TIT2(encoding=3, text=common_tags['title']))
            audio_file.tags.add(TPE1(encoding=3, text=common_tags['artist']))
            audio_file.tags.add(TALB(encoding=3, text=common_tags['album']))
            audio_file.tags.add(TCON(encoding=3, text=common_tags['genre']))
            audio_file.tags.add(TYER(encoding=3, text=common_tags['year']))
            if common_tags['track'] and common_tags['track'].isdigit():
                audio_file.tags.add(TRCK(encoding=3, text=common_tags['track']))
            if cover_data:
                audio_file.tags.add(APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=cover_data))
            audio_file.save()
        elif output_format == "flac":
            audio_file = FLAC(file_path)
            audio_file['title'] = common_tags['title']
            audio_file['artist'] = common_tags['artist']
            audio_file['album'] = common_tags['album']
            audio_file['genre'] = common_tags['genre']
            audio_file['date'] = common_tags['year']
            if common_tags['track'] and common_tags['track'].isdigit():
                audio_file['tracknumber'] = common_tags['track']
            if cover_data:
                picture = Picture()
                picture.data = cover_data
                picture.mime = "image/jpeg"
                audio_file.add_picture(picture)
            audio_file.save()
        elif output_format == "wav":
            eel.update_status("WAV files do not support metadata. Skipping.", "yellow")
    
    except Exception as e:
        _handle_error(f"Error adding metadata: {e}", e)
    finally:
        pass

def _download_single_video(url, metadata, save_folder, output_format, bitrate, current_count=1, total_count=1, download_id=None):
    """Downloads a single video and processes its metadata."""
    temp_dir = None
    custom_cover_path = None
    final_destination = None
    try:
        if not output_format or not isinstance(output_format, str):
            raise ValueError("Output format is not specified or invalid.")

        eel.update_status(f"Downloading {current_count}/{total_count}: '{metadata['title']}'...", "blue")
        
        temp_dir = tempfile.mkdtemp()
        random_chars = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        filename = f"{_sanitize_filename(metadata['title'])} - {_sanitize_filename(metadata['artist'])} [{random_chars}]"
        out_path = os.path.join(temp_dir, f'{filename}.%(ext)s')
        
        if metadata.get('cover_data'):
            custom_cover_path = os.path.join(temp_dir, f"{filename}_cover.jpg")
            image_data = base64.b64decode(metadata['cover_data'])
            with open(custom_cover_path, 'wb') as f:
                f.write(image_data)
            postprocessors = [{'key': 'FFmpegExtractAudio', 'preferredcodec': output_format.lower(), 'preferredquality': bitrate[:-1]}]
        else:
            postprocessors = [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': output_format.lower(), 'preferredquality': bitrate[:-1]},
                {'key': 'EmbedThumbnail'},
            ]

        if output_format.lower() in ["wav"]:
            postprocessors = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav'}]
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': out_path,
            'postprocessors': postprocessors,
            'ffmpeg_location': ffmpeg_path,
            'writethumbnail': not metadata.get('cover_data'),
            'noplaylist': True,
            'geo_bypass': True,
            'progress_hooks': [lambda d: _progress_hook_for_live_card(d, download_id)],
            'quiet': True,
            'youtube_include_dash_manifest': False,
            'youtube_include_hls_manifest': False,
            'allow_sabr': True,
        }
        cookie_path = settings.get("cookies")
        if cookie_path and os.path.exists(cookie_path) and os.path.getsize(cookie_path) > 0:
            ydl_opts["cookiefile"] = cookie_path
        else:
            ydl_opts["cookiesfrombrowser"] = ("edge",)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)

            if not info_dict:
                raise Exception("Could not retrieve video info.")

            base_name_downloaded = os.path.join(temp_dir, ydl.prepare_filename(info_dict).split('.')[0])
            
            possible_files = [f for f in os.listdir(temp_dir) if f.startswith(filename)]
            final_file_path = next((os.path.join(temp_dir, f) for f in possible_files if f.endswith(output_format.lower())), None)
            
            if not final_file_path and possible_files:
                final_file_path = os.path.join(temp_dir, possible_files[0])
            if not final_file_path or not os.path.exists(final_file_path):
                raise FileNotFoundError("Downloaded file not found after conversion.")
            
            if custom_cover_path and os.path.exists(custom_cover_path):
                thumbnail_path = custom_cover_path
            else:
                thumbnail_path = f"{base_name_downloaded}.webp"
            
            if output_format.lower() in ["mp3", "m4a", "flac"]:
                _add_metadata(final_file_path, thumbnail_path, output_format.lower(), metadata)
            elif output_format.lower() == "wav":
                eel.update_status("WAV files do not support metadata. Skipping.", "yellow")

        final_destination = os.path.join(save_folder, os.path.basename(final_file_path))
        shutil.move(final_file_path, final_destination)
        
        eel.update_status(f"Download of '{metadata['title']}' complete!", "green")
        
        eel.finishDownloadCard(download_id, metadata, final_destination)
        
    except (yt_dlp.DownloadError, ValueError, FileNotFoundError, Exception) as e:
        _handle_error(f"Download Error for '{metadata.get('title', 'video')}'", e)
        eel.update_status(f"Error with '{metadata.get('title', 'video')}': {e}", "red")
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir, ignore_errors=True)
        if current_count == total_count:
            eel.resetUI()

def _download_playlist_thread(save_folder, output_format, bitrate, playlist_url, metadata, url_list=None, default_album_name=None):
    """Downloads all videos from a given playlist URL or a pre-defined list of URLs."""
    try:
        if not url_list:
            ydl_opts_meta = {'quiet': True, 'extract_flat': True}
            cookie_path = settings.get("cookies")
            if cookie_path and os.path.exists(cookie_path) and os.path.getsize(cookie_path) > 0:
                ydl_opts_meta["cookiefile"] = cookie_path
            else:
                ydl_opts_meta["cookiesfrombrowser"] = ("edge",)

            with yt_dlp.YoutubeDL(ydl_opts_meta) as ydl_meta:
                playlist_info = ydl_meta.extract_info(playlist_url, download=False)
            
            if not playlist_info or 'entries' not in playlist_info:
                raise Exception("Could not retrieve playlist information.")
            
            urls = [entry.get('url') for entry in playlist_info['entries'] if entry.get('url')]
            album_name = _sanitize_filename(playlist_info.get('title', 'Playlist Download'))
        else:
            urls = url_list
            album_name = _sanitize_filename(default_album_name or 'Batch Download')

        total_count = len(urls)
        
        if not album_name:
            album_name = 'Playlist Download'
        playlist_folder = os.path.join(save_folder, album_name)
        
        try:
            os.makedirs(playlist_folder, exist_ok=True)
        except OSError as e:
            _handle_error(f"Error creating directory: {e}", e)
            eel.update_status(f"Error: Could not create folder at '{playlist_folder}'. Check permissions.", "red")
            eel.resetUI()
            return
        
        for i, url in enumerate(urls):
            try:
                download_id = f"dl_{i}_{album_name.replace(' ', '')}"
                cookie_path = settings.get("cookies")
                ydl_opts = {'quite': True}
                if cookie_path and os.path.exists(cookie_path) and os.path.getsize(cookie_path) > 0:
                    ydl_opts["cookiefile"] = cookie_path
                else:
                    ydl_opts["cookiesfrombrowser"] = ("edge",)

                with yt_dlp.YoutubeDL(ydl_opts) as ydl_video:
                    video_info = ydl_video.extract_info(url, download=False)
                
                video_metadata = {
                    'title': video_info.get('title', 'Unknown Title'),
                    'artist': ", ".join(video_info.get('artists', []) or [video_info.get('uploader', 'Unknown Artist')]),
                    'album': album_name,
                    'genre': video_info.get('genre', ''),
                    'year': (video_info.get('release_date') or '')[:4],
                    'track': str(i + 1),
                    'cover_data': metadata.get('cover_data'),
                    'thumbnail_url': video_info.get('thumbnail', '')
                }

                eel.addLiveDownloadCard(download_id, video_metadata)

                _download_single_video(
                    url=url, 
                    metadata=video_metadata, 
                    save_folder=playlist_folder, 
                    output_format=output_format, 
                    bitrate=bitrate, 
                    current_count=i + 1, 
                    total_count=total_count,
                    download_id=download_id
                )
            except Exception as e:
                _handle_error(f"Error processing video {url}: {e}", e)
                eel.update_status(f"Error with video {i+1}: {e}", "red")
        
        eel.update_status("Playlist/Batch download finished!", "green")
    except Exception as e:
        _handle_error(f"Playlist/Batch download error: {e}", e)
        eel.update_status(f"An error occurred during download: {e}", "red")
    finally:
        eel.update_button_state(False)
        eel.resetUI()

def _download_ffmpeg_if_needed():
    """Downloads and extracts FFmpeg binaries if they don't exist."""
    global ffmpeg_path, ffprobe_path
    
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
        ffmpeg_path = os.path.join(exe_dir, "ffmpeg.exe")
        ffprobe_path = os.path.join(exe_dir, "ffprobe.exe")
    else:
        ffmpeg_path = os.path.join(app_base_path, "ffmpeg.exe")
        ffprobe_path = os.path.join(app_base_path, "ffprobe.exe")

    try:
        if os.path.isfile(ffmpeg_path) and os.path.isfile(ffprobe_path):
            eel.update_status("App is ready to use.", "green")
            return {"status": "success", 'value': None}

        def download_in_thread():
            eel.update_status("FFmpeg not found. Downloading and extracting...", "yellow")
            ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
            download_path = os.path.join(app_base_path, "ffmpeg.zip")
            try:
                urllib.request.urlretrieve(ffmpeg_url, download_path)
                eel.update_status("FFmpeg downloaded. Extracting...", "yellow")
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(app_base_path)
                os.remove(download_path)
                extracted_folder = next(f for f in os.listdir(app_base_path) if f.startswith('ffmpeg-master-latest'))
                extracted_bin_path = os.path.join(app_base_path, extracted_folder, 'bin')
                if os.path.exists(extracted_bin_path):
                    shutil.copy(os.path.join(extracted_bin_path, 'ffmpeg.exe'), ffmpeg_path)
                    shutil.copy(os.path.join(extracted_bin_path, 'ffprobe.exe'), ffprobe_path)
                shutil.rmtree(os.path.join(app_base_path, extracted_folder))
                eel.update_status("Setup completed!", "green")
            except Exception as e:
                _handle_error(f"Error setting up FFmpeg: {e}", e)
                eel.update_status(f"Error setting up FFmpeg: {e}", "red")
            finally:
                eel.update_button_state(False)
        
        eel.update_button_state(True)
        threading.Thread(target=download_in_thread, daemon=True).start()
        return {"status": "in_progress", 'value': None}

    except Exception as e:
        _handle_error(f"Critical error during setup: {e}", e, is_critical=True)
        return {"status": "error", "message": str(e), 'value': None}
    
@eel.expose
def get_initial_settings():
    """Returns the initial settings to the frontend."""
    try:
        _load_settings()
        return {"status": "success", "value": settings}
    except Exception as e:
        _handle_error(f"Error in get_initial_settings: {e}", e)
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def save_settings(new_settings):
    """Saves the provided settings to the config file."""
    try:
        global settings
        settings.update(new_settings)
        _save_settings()
        return {"status": "success", 'value': None}
    except Exception as e:
        _handle_error(f"Error in save_settings: {e}", e)
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def browse_folder():
    """Opens a folder selection dialog and returns the selected path."""
    try:
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            global settings
            settings['download_folder'] = folder_selected
            _save_settings()
        return folder_selected if folder_selected else ""
    except Exception as e:
        _handle_error(f"Error in browse_folder: {e}", e)
        return ""

@eel.expose
def fetch_metadata(url_input):
    """Fetches video metadata and thumbnail for a given YouTube URL or playlist."""
    global is_playlist, download_queue
    
    urls = [u.strip() for u in url_input.split('\n') if u.strip()]
    if not urls:
        return {'status': 'error', 'value': None, 'message': 'URL is empty or invalid.'}
    
    is_batch_download = len(urls) > 1
    url = urls[0]

    try:
        if not isinstance(url, str) or not url.strip():
            return {'status': 'error', 'value': None, 'message': 'URL is empty or invalid.'}
        if not (re.match(r'^https?://(www\.)?(youtube\.com|youtu\.be|music\.youtube\.com)/', url)):
            return {'status': 'error', 'value': None, 'message': 'URL must be from YouTube or YouTube Music.'}

        ydl_opts = {'quiet': True, 'extract_flat': True,'geo_bypass': True,}
        cookie_path = settings.get("cookies")
        if cookie_path and os.path.exists(cookie_path) and os.path.getsize(cookie_path) > 0:
            ydl_opts["cookiefile"] = cookie_path
        else:
            ydl_opts["cookiesfrombrowser"] = ("edge",)


        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            
            if info_dict:
                if 'entries' in info_dict and not is_batch_download:
                    is_playlist = True
                    download_queue = []
                    for entry in info_dict['entries']:
                        if entry and entry.get('url'):
                            download_queue.append({
                                'title': entry.get('title', 'Unknown Title'),
                                'artist': ", ".join(entry.get('artists', []) or [entry.get('uploader', 'Unknown Artist')]),
                                'album': info_dict.get('title', 'Unknown Album'),
                                'thumbnail_url': entry.get('thumbnail', ''),
                                'url': entry.get('url', ''),
                            })
                    return {"status": "success", "value": {"type": "playlist", "metadata": download_queue}}
                
                elif is_batch_download:
                    is_playlist = False
                    download_queue = [{'url': u} for u in urls]
                    return {"status": "success", "value": {"type": "batch", "metadata": download_queue}}
                
                else:
                    is_playlist = False
                    metadata = {
                        'title': info_dict.get('title', 'Unknown Title'),
                        'artist': ", ".join(info_dict.get('artists', []) or [info_dict.get('uploader', 'Unknown Artist')]),
                        'album': info_dict.get('album', 'Unknown Album'),
                        'thumbnail_url': info_dict.get('thumbnail', ''),
                        'url': url,
                        'year': (info_dict.get('release_date') or '')[:4],
                    }
                    download_queue = [metadata]
                    return {"status": "success", "value": {"type": "video", "metadata": metadata}}
            else:
                return {'status': 'error', 'value': None, 'message': 'Could not fetch video information.'}
    except Exception as e:
        _handle_error(f"Error fetching metadata: {e}", e)
        return {'status': 'error', 'value': None, 'message': str(e)}

@eel.expose
def download_music(url_input, metadata, save_folder, selected_format, bitrate):
    """Starts the download process based on the input type (single, playlist, or batch)."""
    try:
        urls = [u.strip() for u in url_input.split('\n') if u.strip()]
        if not urls:
            return {'status': 'error', 'value': None, 'message': 'URL is empty or invalid.'}

        if not os.path.exists(save_folder):
            return {"status": "error", "value": None, "message": "Save folder does not exist."}

        supported_formats = [
            "m4a", "mp3", "flac", "wav", "aac", "alac", "opus", "vorbis", "webm"
        ]
        if selected_format not in supported_formats:
            return {"status": "error", "value": None, "message": f"Unsupported format: {selected_format}"}

        if not isinstance(bitrate, str) or not re.match(r'^\d+k$', bitrate):
            return {"status": "error", "value": None, "message": "Bitrate must be in the format '192k', '320k', etc."}
        
        is_playlist_url = False
        if len(urls) == 1:
            try:
                with yt_dlp.YoutubeDL({'quiet': True, 'extract_flat': True}) as ydl:
                    info = ydl.extract_info(urls[0], download=False)
                    if 'entries' in info:
                        is_playlist_url = True
            except Exception as e:
                _handle_error(f"Error checking URL type: {e}", e)

        if is_playlist_url:
            thread = threading.Thread(
                target=_download_playlist_thread,
                args=(save_folder, selected_format, bitrate, urls[0], metadata),
                daemon=True
            )
            thread.start()
        elif len(urls) > 1:
            thread = threading.Thread(
                target=_download_playlist_thread,
                args=(save_folder, selected_format, bitrate, None, metadata, urls, "Batch Download"),
                daemon=True
            )
            thread.start()
        else:
            download_id = f"dl_{_sanitize_filename(metadata.get('title', 'video'))}"
            eel.addLiveDownloadCard(download_id, metadata)
            thread = threading.Thread(
                target=_download_single_video,
                args=(urls[0], metadata, save_folder, selected_format, bitrate, 1, 1, download_id),
                daemon=True
            )
            thread.start()
            
        return {"status": "success", "value": None, "message": "Download process started."}
    except Exception as e:
        _handle_error(f"Error in download_music: {e}", e)
        return {"status": "error", "value": None, "message": str(e)}
    
@eel.expose
def start_initial_setup():
    """Starts the initial setup tasks like checking for FFmpeg."""
    try:
        return _download_ffmpeg_if_needed()
    except Exception as e:
        _handle_error(f"Error starting initial setup: {e}", e, is_critical=True)
        return {"status": "error", "value": None, "message": str(e)}

@eel.expose
def openPathInExplorer(path):
    """Opens a given file path in the system's default file explorer."""
    print(f"Attempting to open path: {path}")
    try:
        if os.name == 'nt':
            os.startfile(path)
        elif os.uname().sysname == 'Darwin':
            subprocess.Popen(['open', path])
        else:
            subprocess.Popen(['xdg-open', path])
        
        return {"status": "success", "message": f"Successfully opened {path}"}
    except Exception as e:
        _handle_error(f"Could not open path: {path}", e)
        return {"status": "error", "message": f"Could not open path: {e}"}

if __name__ == "__main__":
    multiprocessing.freeze_support()
    threading.Thread(target=_update_modules_in_thread, daemon=True).start()
    _load_settings()
    eel.init("web")

    window_width = 950
    window_height = 700

    root = Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    try:
        eel.start("index.html", size=(window_width, window_height), position=(x, y), host='localhost', block=True)
    except Exception as e:
        print(f"Error starting Eel: {e}")