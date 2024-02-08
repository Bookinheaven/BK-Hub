from pytube import YouTube
import os
import time

DOWNLOAD_FOLDER = "Downloaded"
songs_list = []
def create_download_folder():
    folder_path = os.path.join(os.path.dirname(__file__), DOWNLOAD_FOLDER)
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        os.mkdir(folder_path)
        print(f"Folder Created: {folder_path}")
    return folder_path

def download_and_convert(song_link, folder_path):
    song = YouTube(url=song_link)
    title = song.title.replace("/", " ")[:100]
    output_filename = f"{title}.m4a"
    output_path = os.path.join(folder_path, output_filename)

    retries = 3
    attempt_counter = 1
    retry_delay = 5

    while retries > 0:
        try:
            if not os.path.exists(output_path):
                print(f"Attempt {attempt_counter} - Phase 1")
                start_time = time.time()

                audio_stream = song.streams.filter(only_audio=True, file_extension='mp4').first()

                if audio_stream:
                    print(f"Downloading {title}...")
                    audio_stream.download(output_path=folder_path, filename=output_filename)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    print(f"Downloaded {title}, folder: {output_path}\nTime taken: {elapsed_time:.2f} seconds")
                    break
                else:
                    print(f"No audio stream found for {title}")
                    break

            else:
                print(f"File '{title}.m4a' already exists. Skipped")
                break

        except Exception as e:
            print(f"An error occurred during download (Attempt {attempt_counter}): {e}")
            retries -= 1
            attempt_counter += 1
            print(f"Retrying... Remaining attempts: {retries}")
            time.sleep(retry_delay)

            if retries == 0:
                print(f"Failed to download {title} after multiple attempts.")
                break
                
def main():
    songs_data = input("Enter the songs url in order with giving spaces: ").split(" ")
    for x in songs_data:
        if x != '' and len(x) > 10:
            songs_list.append(x)
    conform = (input(f"\nNeed to Download: {songs_list}, \nConform (y/N): ")).lower()
    if conform == 'y':
        for song in songs_list:
            try:
                folder_path = create_download_folder()
                download_and_convert(song, folder_path)
            except Exception as e:
                print(f"An error occurred: {e}")
        print("Download process completed.")
    elif conform == 'n':
        print("Conform : No\nExiting!")
if __name__ == "__main__":
    main()