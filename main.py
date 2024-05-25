from conversions.youtube_playlist_to_mp3 import y_playlist_to_mp3
from conversions.youtube_song_to_mp3 import y_song_to_mp3

if __name__ == "__main__":
   
    while True: 

        print("\nWelcome to the Youtube to MP3 Converter\n")

        print("1) Convert Youtube Song to MP3")
        print("2) Convert Youtube Playlist to MP3\n")

        print("3) Compress songs to (at most) 25 MB\n")

        print("4) Send song to google drive")
        print("5) Send song to discord")
        print("6) Send playlist to google drive")
        print("7) Send playlist to discord\n")

        print("8) Exit")

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
            print("Select a song to compress to 25 MB")
            song_name = input()
        elif option == "4":
            print("Select a song to send to google drive")
            song_name = input()
        elif option == "5":
            print("Select a song to send to discord")
            song_name = input()
        elif option == "6":
            print("Select a playlist to send to google drive")
            playlist_name = input()
        elif option == "7":
            print("Select a playlist to send to discord")
            playlist_name = input()
        elif option == "8":
            break
        else:
            print("Invalid Option. Please put a valid option")
   
    print("Thank you for using the Spotify & Youtube to MP3 Converter")