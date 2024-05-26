# Youtube-To-MP3 Converter

The premise of this small project is to convert youtube songs/playlists into mp3. These mp3s will then appear in the __output__ folder of the project, where it then can be downloaded and used.  


# Disclaimer 


It is __highly recommended__ to use a virtual environment to isolate the project and its dependencies. Here's how you can setup a virtual environment:


```
python3 -m venv env 
source env/bin/activate
```

# Installation 

Note that if you wish to run the program through docker, then you would need to download docker on your system. 

Go to the scripts directory and run the docker script

```
chmod +x docker-install.sh
./docker-install.sh
```


# How to run the program 


1) To run the program normally 


```
pip install -r requirements.txt
python main.py
```


2) Run the program through docker 

```
docker build -t converter-app . 
docker run -it -v /path/to/output/folder:/converter/output converter-app
```

You will now have access to the CLI interface and able to perform any of the listed options. 
