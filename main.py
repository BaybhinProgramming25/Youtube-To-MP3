from conversions.youtube_playlist_to_mp3 import y_playlist_to_mp3
from conversions.youtube_song_to_mp3 import y_song_to_mp3


if __name__ == "__main__":
   
    while True: 

        print("\nWelcome to the Youtube to MP3 Converter\n")

        print("1) Convert Youtube Song to MP3")
        print("2) Convert Youtube Playlist to MP3\n")

        print("3) Exit")

        print("\nPlease select an option")

        option = input()

        if option == "1":
            print("Please enter the URL of the Youtube Song")
            url = input()
            y_song_to_mp3(url)
        elif option == "2":
            print("Please enter the URL of the Youtube Playlist")
            url = input()
            y_playlist_to_mp3(url)
        elif option == "3":
            break
        else:
            print("Invalid Option. Please put a valid option")
   
    print("Thank you for the Youtube to MP3 Converter!")