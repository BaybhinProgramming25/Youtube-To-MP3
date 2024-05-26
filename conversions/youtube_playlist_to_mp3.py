from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import os

# Define our lock we are going to use 
lock = Lock()

def download_and_convert(url: str) -> None:
    try:
        with lock: 
            yt = YouTube(url)
            video_stream = yt.streams.first()

            # Specify a complete path for the downloaded file
            download_path = os.path.join(os.getcwd(), 'temp.mp4')
            video_stream.download(filename=download_path)

            # Check if the video was downloaded successfully
            if not os.path.exists(download_path):
                print(f"Failed to download video from {url}")
                return
        
            audio = AudioFileClip(download_path)

            # Get the title of the YouTube video and use it as the filename for the MP3 file
            title = yt.title
            # Replace special characters with underscores
            safe_title = "".join(c if c.isalnum() else "_" for c in title)

            # Create the output directory if it doesn't exist
            output_dir = os.path.join(os.getcwd(), 'output')
            os.makedirs(output_dir, exist_ok=True)

            # Save the MP3 file in the output directory
            mp3_filename = os.path.join(output_dir, f"{safe_title}.mp3")
        
            # Write the mp3 file 
            audio.write_audiofile(mp3_filename)

            # Delete the mp4 file 
            os.remove(download_path)
    except Exception as e:
        print(f"Failed to download and convert video from {url} due to error: {e}")

def y_playlist_to_mp3(url: str) -> None:
    playlist = Playlist(url)

    # Get the number of videos in the playlist
    num_videos = len(playlist.video_urls)

    with ThreadPoolExecutor(max_workers=num_videos) as executor:
        executor.map(download_and_convert, playlist.video_urls)
