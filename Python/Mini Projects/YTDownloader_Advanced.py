import tkinter
import customtkinter
import subprocess
import threading
import os
import yt_dlp
import json
import random,string


class Music_Downloader(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Youtube Song Downloader")
        self.geometry("720x480")
        self.minsize(720, 480)
        self.ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
        self.ffprobe_path = os.path.join(os.path.dirname(__file__), "ffprobe.exe")
        self.maxsize(1080, 720)
        self.config_appearance()

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

    def download_and_extract_ffmpeg(self):
        import urllib, zipfile, shutil
        """Downloads and extracts the FFmpeg binaries, keeping only ffmpeg.exe and ffprobe.exe."""
        if not os.path.isfile(self.ffmpeg_path) or not os.path.isfile(self.ffprobe_path):
            print("ffmpeg or ffprobe not found. Downloading and extracting...")
            ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
            download_path = os.path.join(os.path.dirname(__file__), "ffmpeg.zip")

            urllib.request.urlretrieve(ffmpeg_url, download_path)
            with zipfile.ZipFile(download_path, 'r') as zip_ref:
                zip_ref.extractall(os.path.dirname(__file__))
            os.remove(download_path)
            print("Temporary zip file removed.")
            extracted_folder = next(f for f in os.listdir(os.path.dirname(__file__)) if f.startswith('ffmpeg-master-latest'))
            extracted_path = os.path.join(os.path.dirname(__file__), extracted_folder, 'bin')
            if os.path.exists(extracted_path):
                for file in os.listdir(extracted_path):
                    if file == 'ffmpeg.exe':
                        shutil.copy(os.path.join(extracted_path, file), self.ffmpeg_path)
                    elif file == 'ffprobe.exe':
                        shutil.copy(os.path.join(extracted_path, file), self.ffprobe_path)
            shutil.rmtree(os.path.join(os.path.dirname(__file__), extracted_folder))
            print("Extracted folder and unnecessary files removed.")

    def config_appearance(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

    def create_widgets(self):
        PreFrame = customtkinter.CTkFrame(self)
        PreFrame.pack(fill=customtkinter.BOTH, expand=True, padx=10, pady=10)

        # Title Label
        self.title_label = customtkinter.CTkLabel(master=PreFrame, text="Insert A Youtube Link")
        self.title_label.pack(padx=10, pady=10)

        # URL Entry
        self.url_link = tkinter.StringVar()
        self.link = customtkinter.CTkEntry(master=PreFrame, width=350, height=40, textvariable=self.url_link)
        # self.url_link.set("https://music.youtube.com/watch?v=9Gduk7Zjem4&si=wQabnj2bqQsJciMF")
        self.link.pack()
        self.link.bind("<Control-a>", self.select_all_text)

        # Format Selector
        self.format_label = customtkinter.CTkLabel(master=PreFrame, text="Select Download Format")
        self.format_label.pack(padx=10, pady=10)
        self.format_selector = customtkinter.CTkComboBox(master=PreFrame, values=["mp3", "m4a", 'flac', 'wav'], width=200)
        self.format_selector.set("m4a")
        self.format_selector.pack(padx=10, pady=10)

        # Folder Path Entry
        self.path_label = customtkinter.CTkLabel(master=PreFrame, text="Download Folder Path")
        self.path_label.pack(padx=10, pady=10)
        self.folder_path = tkinter.StringVar()
        self.folder_path.set("C:/Users/burnk/Downloads/test")
        self.folder_entry = customtkinter.CTkEntry(master=PreFrame, width=350, height=40, textvariable=self.folder_path)
        self.folder_entry.pack(padx=10, pady=10)

        # Status and Progress
        self.finished = customtkinter.CTkLabel(master=PreFrame, text="")
        self.finished.pack()
        # Download Button
        self.download = customtkinter.CTkButton(master=PreFrame, text="Download", command=self.downloadstart)
        self.download.pack(padx=10, pady=20)

        self.mainloop()

    def downloadstart(self):
        # Start download in a new thread
        download_thread = threading.Thread(target=self.run_download)
        download_thread.daemon = True  # Ensure thread exits when the app closes
        download_thread.start()

    def run_download(self):
        try:
            ytlink = self.link.get()
            download_format = self.format_selector.get().lower()
            download_path = self.folder_path.get()
            self.url_link.set("")
            self.update_status(" ", "white")
            self.download.configure(state=tkinter.DISABLED)
            self.yt_download(folder_path=download_path, link=ytlink, output_format= download_format)
            self.update_status(f"Download Completed", "green")
        except Exception as e:
            print(e)
            self.update_status(f"Download Error: {str(e)}", "red")
        self.download.configure(state=tkinter.NORMAL)


    def update_status(self, message, color):
        self.finished.configure(text=message, text_color=color)

    def remove_file(self, path):
        try:
            if os.path.exists(path):
                os.remove(path)
        except Exception as e:
            self.logger.error(f"Error removing file: {path}, {str(e)}")

    def add_metadata(self, input_file):
        """
        Adds or updates metadata to an audio file only if the new value is different.

        :param input_file: Path to the input audio file.
        :return: JSON response with success or error details.
        """
        from mutagen.mp4 import MP4
        from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK, APIC
        from mutagen.flac import FLAC
        from mutagen.mp3 import MP3
        from mutagen.mp4 import MP4Cover
        from mutagen.flac import Picture

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
        """
        Prints the download progress during the video download.
        """
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0.0%')
            speed = d.get('_speed_str', '0 B/s')
            filename = d.get('filename', 'Unknown File')
            print(f"Downloading: {percent} at {speed}, File: {filename}")
        elif d['status'] == 'finished':
            filename = d.get('filename', 'Unknown File')
            print(f"Download complete: {filename}")
            # print(json.dumps(d, indent=4))

    def yt_download(self, folder_path, link, quality="best", output_format="m4a", audio_only=True, playlist=True, format_id=None):
        """
        Downloads audio/video from a YouTube link, converts to a specified format, adds metadata.

        :param folder_path: Folder to save the downloaded file.
        :param link: YouTube link.
        :param quality: Download quality: 'best', 'average', 'worst'.
        :param output_format: The desired audio format (e.g., 'mp3', 'm4a', 'flac', 'wav').
        :param audio_only: Boolean indicating whether to download audio only (True) or full video (False).
        :param playlist: Download playlist: True or False.
        :param format_id: Download using format_id
        """
        self.SaveFolder = folder_path

        def sanitize_filename(filename):
            """Replace invalid characters in filenames with safe alternatives."""
            import re
            invalid_characters = r'[<>:"/\\|?*\x00-\x1F]'
            sanitized = re.sub(invalid_characters, '_', filename)
            return sanitized.strip()

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
        try:
            if not link:
                return json.dumps({"error": "No YouTube link provided"})

            def get_format(quality, audio_only):
                return {
                    "best": 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
                    "average": 'bestaudio[abr<=128k]/best[height<=720]' if audio_only else 'best[height<=720]',
                    "worst": 'worstaudio/worst' if audio_only else 'worstvideo/worst',
                }.get(quality, 'bestaudio/best')

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
                'format': format_id if format_id else get_format(quality, audio_only),
                'outtmpl': out_path,
                'verbose': True,
                'noplaylist': not playlist,
                'extractaudio': audio_only,
                'writethumbnail': True,
                'audioformat': output_format if audio_only else None,
                'merge_output_format': output_format if not audio_only else None,
                'ffmpeg_location': self.ffmpeg_path,
                'progress_hooks': [self.progress_hook],
                'writesubtitles': True,
                'subtitleslangs': ['en'],
                'embedsubtitles': True,
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': output_format if audio_only else 'mp3',
                        'preferredquality': '192',
                    },
                    {
                        'key': 'FFmpegMetadata',
                    },
                    {
                        'key': 'EmbedThumbnail',
                    },
                ],
                'geo_bypass': True,
                'retries': 10,
                'socket_timeout': 30,
                'subtitlesformat': 'best'
            }
            os.environ['PYTHONIOENCODING'] = 'utf-8'
            if output_format == "wav":
                ydl_opts['writethumbnail'] = False

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(link, download=True)
                original_filename = ydl.prepare_filename(info_dict)
                sanitized_filename = sanitize_filename(os.path.basename(original_filename))
                sanitized_file_path = os.path.join(folder_path, sanitized_filename)

                if sanitized_filename != os.path.basename(original_filename):
                    os.rename(original_filename, sanitized_file_path)

                self.filePath = os.path.abspath(sanitized_file_path)
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

                output_file = os.path.splitext(sanitized_file_path)[0] + f".{output_format}"
                add_metadata_response = self.add_metadata(output_file)
                for sanitize_filename in os.listdir(folder_path):
                    if sanitize_filename.endswith(".vtt"):
                        os.remove(os.path.join(folder_path, sanitize_filename))
                return add_metadata_response

        except Exception as e:
            return json.dumps({"error": f"Download Error: {e}"})

    def select_all_text(self, event):
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')

if __name__ == "__main__":
    Music_Downloader().build()
