from __future__ import unicode_literals
import youtube_dl
import os
import re
import sys

link = input('Enter your link here: ')
dirname = input('Enter the name of the folder you want to store these songs in: ')

os.mkdir(dirname)

ydl_cmd_options = {
    'format': 'bestaudio/best',
    #'playliststart': 170,
    'cookiefile': 'cookies.txt',
    'ignoreerrors': True,
    'postprocessors':
    [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    #'quiet': True,
    'outtmpl': dirname + '/%(title)s.%(ext)s',
}

print("downloading your video(s), please wait...")
sys.stdout = open('debug.txt', 'w')
sys.stderr = sys.stdout
with youtube_dl.YoutubeDL(ydl_cmd_options) as ydl:
    ydl.download([link])
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
print("done!")

pat = '[\[\(].+?[\]\)]'

os.chdir(os.getcwd() + '/' + dirname)

for file in os.listdir(os.getcwd()):
    og = str(file)
    og = re.sub(pat, "", og)
    og = re.sub(' +.mp3', '.mp3', og)
    os.rename(file, og);


