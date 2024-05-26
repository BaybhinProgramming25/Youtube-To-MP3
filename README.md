# Youtube-To-MP3 Converter

The premise of this small project is to convert youtube songs/playlists into mp3. These mp3s will then be stored at any desired location. For more information about the different places where you can store mp3s, scroll down to the __Extra Features__ section. 


# Disclaimers 




# How to run the program 

The best way to run this program is through docker:

```
docker build -t converter-app . 
docker run -it -v /path/to/output/folder:/converter/output converter-app
```

You will now have access to the CLI interface and able to perform various options. 


If you wish to run the program without docker, then ensure you have the following installed: 


# Extra Features 

