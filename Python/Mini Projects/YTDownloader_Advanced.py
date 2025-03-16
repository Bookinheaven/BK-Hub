import tkinter
import customtkinter
import subprocess
import threading
import os
import yt_dlp
import json
import random
import string
from mutagen.mp4 import MP4, MP4Cover
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, APIC
from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
import urllib.request
import zipfile
import shutil
from tkinter import filedialog

class Music_Downloader(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Music Downloader")
        self.geometry("720x580")
        self.minsize(720, 580)
        self.maxsize(1080, 720)
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        self.ffprobe_path = os.path.join(os.path.dirname(__file__), "ffprobe.exe")
        self.config_appearance()
        self.load_settings() 
        self.create_widgets()
        self.fetched_metadata = []
        self.fetched_images = []
        self.filePath = None
        self.fileName = None
        self.fileExt = None
        self.SaveFolder = None
        self.thumbnailPath = None
        self.metaData = None
        self.ydl_instance = None
        self.download_and_extract_ffmpeg()

    def load_settings(self):
        """Loads user settings from a local configuration file."""
        self.settings_file = os.path.join(os.path.dirname(__file__), "config.json")
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                self.settings = json.load(f)
        else:
            self.settings = {
                "download_folder": os.path.join(os.path.expanduser("~"), "Downloads"),
                "format": "m4a",
                "bitrate": "192k",
                "remember_settings": True,
            }

    def save_settings(self):
        """Saves user settings to a local configuration file."""
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)

    def download_and_extract_ffmpeg(self):
        """Downloads and extracts FFmpeg binaries if they don't already exist."""
        if not os.path.isfile(self.ffmpeg_path) or not os.path.isfile(self.ffprobe_path):
            print("FFmpeg or FFprobe not found. Downloading and extracting...")
            ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
            download_path = os.path.join(os.path.dirname(__file__), "ffmpeg.zip")

            try:
                urllib.request.urlretrieve(ffmpeg_url, download_path)
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(os.path.dirname(__file__))
                os.remove(download_path)
                print("Temporary zip file removed.")

                extracted_folder = next(
                    f for f in os.listdir(os.path.dirname(__file__)) if f.startswith('ffmpeg-master-latest')
                )
                extracted_path = os.path.join(os.path.dirname(__file__), extracted_folder, 'bin')
                if os.path.exists(extracted_path):
                    for file in os.listdir(extracted_path):
                        if file == 'ffmpeg.exe':
                            shutil.copy(os.path.join(extracted_path, file), self.ffmpeg_path)
                        elif file == 'ffprobe.exe':
                            shutil.copy(os.path.join(extracted_path, file), self.ffprobe_path)
                shutil.rmtree(os.path.join(os.path.dirname(__file__), extracted_folder))
                print("Extracted folder and unnecessary files removed.")
            except Exception as e:
                print(f"Error downloading or extracting FFmpeg: {e}")

    def config_appearance(self):
        """Configures the appearance of the application."""
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

    def create_widgets(self):
        """Creates and arranges the GUI widgets."""
        PreFrame = customtkinter.CTkFrame(self)
        PreFrame.pack(fill=customtkinter.BOTH, expand=True, padx=10, pady=10)

        self.title_label = customtkinter.CTkLabel(master=PreFrame, text="YouTube Music Downloader", font=("Arial", 20, "bold"))
        self.title_label.pack(padx=10, pady=(10, 20))

        self.url_link = tkinter.StringVar()
        self.link = customtkinter.CTkEntry(master=PreFrame, width=400, height=40, textvariable=self.url_link, placeholder_text="Enter YouTube URL")
        self.link.pack(padx=10, pady=10)
        self.link.bind("<Control-a>", self.select_all_text)

        self.format_label = customtkinter.CTkLabel(master=PreFrame, text="Select Download Format", font=("Arial", 14))
        self.format_label.pack(padx=10, pady=(10, 5))
        self.format_selector = customtkinter.CTkComboBox(master=PreFrame, values=["mp3", "m4a", "flac", "wav"], width=200)
        self.format_selector.set(self.settings.get("format", "m4a"))
        self.format_selector.pack(padx=10, pady=5)

        self.bitrate_label = customtkinter.CTkLabel(master=PreFrame, text="Select Bitrate", font=("Arial", 14))
        self.bitrate_label.pack(padx=10, pady=(10, 5))
        self.bitrate_selector = customtkinter.CTkComboBox(master=PreFrame, values=["128k", "192k", "256k", "320k"], width=200)
        self.bitrate_selector.set(self.settings.get("bitrate", "192k"))
        self.bitrate_selector.pack(padx=10, pady=5)

        self.folder_frame = customtkinter.CTkFrame(master=PreFrame)
        self.folder_frame.pack(padx=10, pady=(10, 5), fill=tkinter.X)

        self.folder_path = tkinter.StringVar()
        self.folder_path.set(self.settings.get("download_folder", os.path.join(os.path.expanduser("~"), "Downloads")))
        self.folder_entry = customtkinter.CTkEntry(master=self.folder_frame, width=300, height=40, textvariable=self.folder_path)
        self.folder_entry.pack(side=tkinter.LEFT, padx=(0, 10))

        self.browse_button = customtkinter.CTkButton(master=self.folder_frame, text="Browse", width=80, command=self.browse_folder)
        self.browse_button.pack(side=tkinter.LEFT)

        self.remember_settings = tkinter.BooleanVar(value=self.settings.get("remember_settings", True))
        self.remember_checkbox = customtkinter.CTkCheckBox(master=PreFrame, text="Remember Settings", variable=self.remember_settings)
        self.remember_checkbox.pack(padx=10, pady=(10, 20))

        self.finished = customtkinter.CTkLabel(master=PreFrame, text="", font=("Arial", 12))
        self.finished.pack(padx=10, pady=(10, 20))

        self.download = customtkinter.CTkButton(master=PreFrame, text="Download", command=self.download_start, width=200, height=40)
        self.download.pack(padx=10, pady=(10, 20))

    def browse_folder(self):
        """Opens a folder selection dialog and updates the folder path."""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def download_start(self):
        """Starts the download process in a separate thread."""
        if self.remember_settings.get():
            self.settings["download_folder"] = self.folder_path.get()
            self.settings["format"] = self.format_selector.get()
            self.settings["bitrate"] = self.bitrate_selector.get()
            self.settings["remember_settings"] = self.remember_settings.get()
            self.save_settings()

        download_thread = threading.Thread(target=self.run_download)
        download_thread.daemon = True
        download_thread.start()

    def run_download(self):
        """Handles the download process."""
        try:
            ytlink = self.link.get()
            download_format = self.format_selector.get().lower()
            download_path = self.folder_path.get()
            bitrate = self.bitrate_selector.get()
            self.url_link.set("")
            self.update_status("Starting download...", "white")
            self.download.configure(state=tkinter.DISABLED)
            self.yt_download(folder_path=download_path, link=ytlink, output_format=download_format, bitrate=bitrate)
            self.update_status("Download completed!", "green")
        except Exception as e:
            self.update_status(f"Download error: {str(e)}", "red")
        finally:
            self.download.configure(state=tkinter.NORMAL)

    def update_status(self, message, color):
        """Updates the status label with a message and color."""
        self.finished.configure(text=message, text_color=color)

    def yt_download(self, folder_path, link, output_format="m4a", bitrate="192k", audio_only=True, playlist=True):
        """Downloads and processes the YouTube audio."""
        try:
            if not link:
                raise ValueError("No YouTube link provided")
            def generate_custom_suffix():
                letters = ''.join(random.choices(string.ascii_letters, k=4))
                numbers = ''.join(random.choices(string.digits, k=3))
                tail_letters = ''.join(random.choices(string.ascii_letters, k=4))
                return letters + numbers + tail_letters

            custom_suffix = generate_custom_suffix()
            out_path = os.path.join(
                folder_path,
                f'%(title)s [{custom_suffix}].%(ext)s'
            )

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': out_path,
                'verbose': True,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': output_format,
                        'preferredquality': bitrate[:-1],
                    },
                    {
                        'key': 'FFmpegMetadata',
                    },
                    {
                        'key': 'EmbedThumbnail',
                    },
                ],
                'ffmpeg_location': self.ffmpeg_path,
                'writethumbnail': True,
                'geo_bypass': True,
                'progress_hooks': [self.progress_hook],
            }
            def get_audio_file_info(input_file):
                try:
                    command = [
                        self.ffprobe_path, '-v', 'error', '-show_entries', 'stream', '-of', 'json', input_file
                    ]
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    file_info = json.loads(result.stdout)
                    audio_info = {}
                    for stream in file_info['streams']:
                        if stream['codec_type'] == 'audio':
                            audio_info = {
                                'codec': stream.get('codec_name', ''),
                                'sample_rate': stream.get('sample_rate', ''),
                                'channels': stream.get('channels', ''),
                                'channel_layout': stream.get('channel_layout', ''),
                                'bitrate': stream.get('bit_rate', ''),
                                'language': stream.get('tags', {}).get('language', '')
                            }

                    return audio_info

                except subprocess.CalledProcessError as e:
                    return {'error': 'Error extracting audio info', 'message': str(e)}
                except Exception as e:
                    return {'error': 'Error', 'message': str(e)}

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                self.filePath = ydl.prepare_filename(info_dict)
                self.fileExt = os.path.splitext(self.filePath)[1]
                self.fileName = os.path.splitext(os.path.basename(self.filePath))[0]

                audio_info = get_audio_file_info(self.filePath)
                self.metaData = {
                    'title': info_dict.get('title', 'Unknown Title'),
                    'ext': info_dict.get('ext', ''),
                    'artist': info_dict.get('uploader', ''),
                    'year': info_dict.get('release_year', audio_info.get('year', "")),
                    'album': info_dict.get('album', ''),
                    'track': info_dict.get('track', ''),
                    'genre': info_dict.get('genre', ''),
                    'description': info_dict.get('description', ''),
                    'duration': str(info_dict.get('duration', '')),
                    'language': info_dict.get('language', audio_info.get('language', '')),
                    'codec': audio_info.get('codec', ''),
                    'sample_rate': audio_info.get('sample_rate', 0),
                    'channels': audio_info.get('channels', 0),
                    'channel_layout': audio_info.get('channel_layout', ''),
                    'bitrate': audio_info.get('bitrate', 0),
                }
                self.add_metadata(self.filePath)
                self.update_status("Metadata added successfully!", "blue")

        except Exception as e:
            self.update_status(f"Error during download: {str(e)}", "red")

    def add_metadata(self, input_file):
        """
        Adds or updates metadata to an audio file only if the new value is different.

        :param input_file: Path to the input audio file.
        :return: JSON response with success or error details.
        """
        if not os.path.isfile(input_file):
            return json.dumps({"error": f"The file '{input_file}' does not exist."})

        try:
            file_extension = os.path.splitext(input_file)[1].lower()
            thumbnail_path = self.thumbnailPath

            def update_metadata(audio_file, key, value, tag):
                if value and key.lower() not in audio_file and value != audio_file.get(tag, ""):
                    audio_file[tag] = value

            required = ["duration", "artist", "title", "thumbnail", "composer", "format", "album", "genre", "language"]
            mp4_tags_map = {
                "title": "\xa9nam",
                "artist": "\xa9ART",
                "album": "\xa9alb",
                "genre": "\xa9gen",
                "composer": "\xa9wrt",
                "language": "ldes",
                "duration": None,
                "format": None,
                "thumbnail": None
            }
            if file_extension == ".m4a":
                try:
                    audio_file = MP4(input_file)
                    for key, value in self.metaData.items():
                        if key.lower() in mp4_tags_map and mp4_tags_map[key.lower()]:
                            update_metadata(audio_file, key, value, mp4_tags_map[key.lower()])

                    if thumbnail_path and os.path.isfile(thumbnail_path):
                        with open(thumbnail_path, "rb") as img_file:
                            audio_file.tags["covr"] = [MP4Cover(img_file.read(), imageformat=MP4Cover.FORMAT_JPEG)]
                        self.remove_file(thumbnail_path)

                    audio_file.save()
                    return json.dumps({"status": "Metadata added", "output_file": input_file})

                except Exception as e:
                    return json.dumps({"error": f"Error updating M4A metadata: {str(e)}"})

            elif file_extension == ".mp3":
                try:
                    audio_file = MP3(input_file, ID3=ID3)
                    for key, value in self.metaData.items():
                        if key.lower() == "title":
                            audio_file.tags.add(TIT2(encoding=3, text=value))
                        elif key.lower() == "artist":
                            audio_file.tags.add(TPE1(encoding=3, text=value))
                        elif key.lower() == "album":
                            audio_file.tags.add(TALB(encoding=3, text=value))
                        elif key.lower() == "track_number":
                            audio_file.tags.add(TRCK(encoding=3, text=value))
                    if thumbnail_path and os.path.isfile(thumbnail_path):
                        with open(thumbnail_path, "rb") as img_file:
                            audio_file.tags.add(
                                APIC(encoding=3, mime='image/jpeg', type=3, desc='Cover', data=img_file.read())
                            )
                        self.remove_file(thumbnail_path)

                    audio_file.save()
                    return json.dumps({"status": "Metadata added", "output_file": input_file})

                except Exception as e:
                    return json.dumps({"error": f"Error with MP3 metadata: {str(e)}"})

            elif file_extension == ".flac":
                try:
                    audio_file = FLAC(input_file)
                    for key, value in self.metaData.items():
                        if key.lower() in required:
                            update_metadata(audio_file, key, value, key.lower())

                    if thumbnail_path and os.path.isfile(thumbnail_path):
                        with open(thumbnail_path, "rb") as img_file:
                            picture_data = img_file.read()
                            picture = Picture()
                            picture.data = picture_data
                            picture.mime = "image/jpeg"
                            picture.type = 3
                            picture.desc = "Cover"
                            audio_file.add_picture(picture)
                        self.remove_file(thumbnail_path)

                    audio_file.save()
                    return json.dumps({"status": "Metadata added", "output_file": input_file})

                except Exception as e:
                    return json.dumps({"error": f"Error updating FLAC metadata: {str(e)}"})

            elif file_extension == ".wav":
                try:
                    if not os.path.exists(input_file):
                        return json.dumps({"error": "File not found", "file": input_file})
                    base_name, ext = os.path.splitext(input_file)
                    temp_output_file = base_name + "_temp" + ext

                    metadata_args = []
                    for key, value in self.metaData.items():
                        metadata_args += ["-metadata", f"{key}={value}"]

                    command = [
                        "ffmpeg",
                        "-i", input_file,
                        *metadata_args,
                        "-c:a", "copy",
                        temp_output_file,
                    ]

                    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=False)

                    if result.returncode == 0:
                        os.replace(temp_output_file, input_file)
                        return json.dumps({"status": "Metadata added", "output_file": input_file})
                    else:
                        if os.path.exists(temp_output_file):
                            self.remove_file(temp_output_file)
                        return json.dumps({
                            "error": "Failed to add metadata",
                            "details": result.stderr
                        })
                except Exception as e:
                    return json.dumps({"error": f"Exception: {str(e)}"})

            elif file_extension == ".aac":
                return json.dumps({"status": "Metadata is not supported", "output_file": input_file})
            else:
                return json.dumps({"error": "Unsupported file type."})

        except Exception as e:
            return json.dumps({"error": f"An error occurred: {str(e)}"})

    def progress_hook(self, d):
        """Handles download progress updates."""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0.0%')
            speed = d.get('_speed_str', '0 B/s')
            self.update_status(f"Downloading: {percent} at {speed}", "white")
        elif d['status'] == 'finished':
            self.update_status("Download complete! Adding metadata...", "blue")

    def select_all_text(self, event):
        """Selects all text in the entry widget."""
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')


if __name__ == "__main__":
    app = Music_Downloader()
    app.mainloop()