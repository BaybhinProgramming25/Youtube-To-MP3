from pytube import YouTube
from moviepy.editor import AudioFileClip

import os

def y_song_to_mp3(url: str) -> None:
    
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
    safe_title = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()

    # Create the output directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Save the MP3 file in the output directory
    mp3_filename = os.path.join(output_dir, f"{safe_title}.mp3")
    audio.write_audiofile(mp3_filename)

    # Delete the mp4 file 
    os.remove(download_path)