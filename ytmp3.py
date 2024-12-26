from pytubefix import YouTube

try:
    url = input("Enter Youtube URL here: ")

    yt = YouTube(url)

    stream = yt.streams.get_audio_only()
    stream.download(output_path="/home/str4t_/Music/PyTube/")
except Exception as e:
    print(e)
