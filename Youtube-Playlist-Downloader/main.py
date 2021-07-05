from __future__ import unicode_literals
import youtube_dl
import os
import re

link = input('Enter your link here: ')
dirname = input('Enter the name of the folder you want to store these songs in: ')

os.mkdir(dirname)

ydl_cmd_options = {
    'format': 'bestaudio/best',
    #'playliststart': 185,
    'cookiefile': 'cookies.txt',
    'postprocessors':
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    #'quiet': True,
    'outtmpl': dirname + '/%(title)s.%(ext)s',
}


with youtube_dl.YoutubeDL(ydl_cmd_options) as ydl:
    ydl.download([link])

pat = '[\[\(].+?[\]\)]'
to_remove = set()

os.chdir(os.getcwd() + '/' + dirname)

for file in os.listdir(os.getcwd()):
    og = str(file)
    og = re.sub(pat, "", og)
    og = re.sub(' +.mp3', '.mp3', og)
    os.rename(file, og);


