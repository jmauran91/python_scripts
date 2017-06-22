## script for taking files out of downloads and into music
## and then from music into iTunes / WinAmp


import shutil
import os
from eyed3 import id3
import glob
import zipfile
import stat
import rarfile
import unrar
import patoolib


## create zipfile object of the downloaded album and get a tracklist

rarfile.UNRAR_TOOL=r'C:\Users\John\AppData\Local\Programs\Python\Python36-32\UnRAR.exe'
tag = id3.Tag()

downloads = glob.glob("C:\\Users\\John\\Downloads\\*")
music_zip = max(downloads, key=os.path.getctime)
if os.path.splitext(music_zip)[-1] == '.zip':
    music_folder = zipfile.ZipFile(music_zip)
elif os.path.splitext(music_zip)[-1] == '.rar':
    music_folder = rarfile.RarFile(music_zip)
temporary_album_folder = r'C:\\Users\\John\\Downloads\\temporary_album_folder'
if not os.path.exists(temporary_album_folder):
    os.makedirs(temporary_album_folder)


## extract the rar / zip into a temporary folder
os.chdir(temporary_album_folder)
music_folder.extractall()
music_folder.close()
print(temporary_album_folder)

## check if the rar / zip is an album folder or just the contents of the album
## then get the artist and album from the first track
temp_list = os.listdir(temporary_album_folder)
if os.path.isdir(temp_list[0]):
    new_temp_list = os.listdir(temp_list[0])
    song = new_temp_list[0]
    pathhelp = temp_list[0]
else:
    song = temp_list[0]
    pathhelp = temporary_album_folder
songpath_help = os.path.join(pathhelp, song)
songpath = os.path.join(r'C:\Users\John\Downloads\temporary_album_folder', songpath_help)
tag.parse(songpath)
print(tag.artist)
print(tag.album_artist)
print(tag.album)
if not tag.artist:
    artist = tag.album_artist
else:
    artist = tag.artist
album = tag.album

## make the destination paths for the album
newpath = f"C:/Users/John/Music/Music/{artist}/{album}"
if not os.path.exists(newpath):
    os.makedirs(newpath)

iTunesPath = f"C:/Users/John/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized/{artist}/{album}"
if not os.path.exists( iTunesPath):
    os.makedirs( iTunesPath )


## this is the script for: if the rar / zip contains an album folder
if os.path.isdir(temp_list[0]):
    path_helper = os.path.join(temporary_album_folder, temp_list[0])
    for file in new_temp_list:
        full_file = os.path.join(path_helper, file)
        if (os.path.isfile(full_file)):
            shutil.copy(full_file, newpath)
            shutil.copy(full_file, iTunesPath)

## this is the script for: if the rar / zip contains just the contents of the album
else:
    for file in temp_list:
        full_file = os.path.join( temporary_album_folder, file)
        if (os.path.isfile(full_file)):
            shutil.copy(full_file, newpath)
            shutil.copy(full_file, iTunesPath)


## deletes the temporary work folder
os.chdir("C:\\Users\\John\\Downloads")
shutil.rmtree(     temporary_album_folder)
