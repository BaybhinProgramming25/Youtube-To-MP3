from conversions.spotify_playlist_to_mp3 import s_playlist_to_mp3
from conversions.spotify_song_to_mp3 import s_song_to_mp3
from conversions.youtube_playlist_to_mp3 import y_playlist_to_mp3
from conversions.youtube_song_to_mp3 import y_song_to_mp3

if __name__ == "__main__":
   
    while True: 

        print("\nWelcome to the Spotify & Youtube to MP3 Converter")

        print("1) Convert Youtube Song to MP3")
        print("2) Convert Youtube Playlist to MP3")
        print("3) Convert Spotify Song to MP3")
        print("4) Convert Spotify Playlist to MP3\n")

        print("6) Compress songs to (at most) 25 MB")
        print("7) Send songs to google drive")
        print("8) Send songs to discord\n")


        print("9) Exit")

        print("Please select an option")

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
            print("Please enter the URL of the Spotify Song")
            url = input()
            s_song_to_mp3(url)
        elif option == "4":
            print("Please enter the URL of the Spotify Playlist")
            url = input()
            s_playlist_to_mp3(url)
        elif option == "9":
            break
        else:
            print("Invalid Option. Please put a valid option")
   
    print("Thank you for using the Spotify & Youtube to MP3 Converter")