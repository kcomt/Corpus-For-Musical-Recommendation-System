from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import csv


#url = "https://www.lyrics.com/artist/Dokken/4110"
#r = requests.get(url)
#soup = BeautifulSoup(r.text, "html.parser")
#albums = soup.find_all('h3', {"class": "artist-album-label"})
# for i in albums:
#    print(i.text)

with open('lyrics.csv', 'r', errors="ignore") as file:
    line = 1
    reader = csv.reader(file)
    songs = []
    for row in reader:
        if line != 0 and line < 5000:
            if line != 1 and row[29] != "unknown":
                song = []
                songTitle = row[2]
                artist = row[4]
                lyrics = row[30]
                song.append(songTitle)
                song.append(artist)
                song.append(lyrics)
                songs.append(song)
            line += 1
        else:
            break

print(len(songs))
textFile = open("lyrics.txt", "w")
n = textFile.write(str(songs))
textFile.close()
