import yt_dlp
import os, sys

def download_url(url):
    base_path = os.path.dirname(__file__)
    ffmpeg_path = os.path.join(base_path, "ffmpeg.exe")
    dest = '.'
    options = {
        'format': 'bestaudio/best',
        'outtmpl': f'{dest}/%(title)s.%(ext)s',
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]}

    with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])



def identify_arg():
    arg = sys.argv[1]

    if arg.startswith('http'):
        return arg      

    elif arg.endswith('.txt'):
        with open(arg, "r", encoding="utf-8") as f:
            links = f.readlines()
            links = [link.strip() for link in links]
        return links


url = identify_arg()    

if type(url) == str:
    download_url(url)

elif type(url) == list:
    for link in url:
         download_url(link)

