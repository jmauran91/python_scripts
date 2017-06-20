## script for taking files out of downloads and into music
## and then from music into iTunes / WinAmp


import shutil
import os
import eyeD3
import glob
import ZipFile
tag = eyeD3.Tag()

## create zipfile object of the downloaded album and get a tracklist

downloads = glob.glob('/Users/johnmauran/Downloads/*')
music_zip = max(downloads, key=os.path.getctime)
music_folder = zipfile.ZipFile(music_zip)
trax = music_folder.namelist()

## get the Artist and Album as strings

tag.link(trax[0])
artist = tag.getArtist()
album = tag.getAlbum()

## make a place for the album to go

newpath = f"/Users/johnmauran/Music/{artist}/{album}"
if not os.path.exists(newpath):
    os.makedirs(newpath)

## extract the contents of the album and
## and place them in the folder under Music

os.chdir(newpath)
music_folder.extractall()
music_folder.close()

## and add them to iTunes as well

iTunesPath = f"/Users/johnmauran/Music/iTunes/iTunes Media/Automatically Add to iTunes.localized/{artist}/{album}"
if not os.path.exists(iTunesPath)
    os.makedirs(iTunesPath)
shutil.copytree( newpath, iTunesPath)
