from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import csv

with open('lyrics.csv', 'r', errors="ignore") as file:
    line = 1
    reader = csv.reader(file)
    songs = []
    idOfSong = 1
    for row in reader:
        if line != 0 and line < 5000:
            if line != 1 and row[29] != "unknown":
                song = []
                songTitle = row[2]
                artist = row[4]
                lyrics = row[30]
                song.append("kcomt")
                song.append(idOfSong)
                song.append(songTitle)
                song.append(artist)
                song.append(lyrics)
                songs.append(song)
                idOfSong += 1
            line += 1
        else:
            break

textFile = open("creatingBagOfWords/songs.txt", "w")
n = textFile.write(str(songs))
textFile.close()
