if __name__ == "__main__":
   
    while True: 
        print("Welcome to the Spotify & Youtube to MP3 Converter")

        print("1) Convert Youtube Song to MP3")
        print("2) Convert Spotify Song to MP3")
        print("3) Convert Youtube Playlist to MP3")
        print("4) Convert Spotify Playlist to MP3")
        print("5) Exit")

        print("Please select an option")

        option = input()

        if option == "1":
            print("Please enter the URL of the Youtube Song")
            url = input()
        elif option == "2":
            print("Please enter the URL of the Spotify Song")
            url = input()
        elif option == "3":
            print("Please enter the URL of the Youtube Playlist")
            url = input()
        elif option == "4":
            print("Please enter the URL of the Spotify Playlist")
            url = input()
        elif option == "5":
            break
        else:
            print("Invalid Option. Please put a valid option")
   
    print("Thank you for using the Spotify & Youtube to MP3 Converter")