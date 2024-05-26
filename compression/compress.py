import os
from pydub import AudioSegment

def compress_mp3(directory: str, song_name: str, bit_rate: str) -> None:
    # List all files in the directory
    files = os.listdir(directory)

    # Find the song in the list of files
    for file in files:
        if file.startswith(song_name):
            # Construct the full path of the song
            input_file = os.path.join(directory, file)
            
            # Construct the full path of the output file
            output_file = os.path.join(directory, "(Compressed Version: )" + file)

            # Load and compress the song
            # For now, we are going to presume that the song is at most 25 MB
            # Further editing of the code will be implemented to reflect size constraints
            audio = AudioSegment.from_mp3(input_file)
            audio.export(output_file, format="mp3", bitrate=bit_rate)

            # Break out of the loop once the song is found and compressed 
            break
        else:
            print(f"Song '{song_name}' not found in directory '{directory}'")
