import csv

corpus = ""
newLines = []
cont = 0
genres = []
genreKey = []
with open('creatingDataSet2/dataSetMusic.csv', 'r', errors="ignore") as file:
    line = 1
    reader = csv.reader(file)
    for row in reader:
        auxLine = []
        if line != 0 and line < 5000:
            if line != 1 and row[29] != "unknown" and row[14] != "unknown":
                auxLine.append(row[2])
                auxLine.append(row[4])
                auxLine.append(row[0])
                auxLine.append(row[17])
                auxLine.append(row[18])
                auxLine.append(row[19])
                auxLine.append(row[20])
                auxLine.append(row[21])
                x = row[14].split(",")
                x[0] = x[0].replace("[u'", "")
                x[0] = x[0].replace("'", "")
                x[0] = x[0].replace("]", "")
                if x[0] not in genres:
                    genres.append(x[0])
                    cont += 1
                    genreKey.append(cont)
                    auxLine.append(cont)
                else:
                    for i in range(len(genres)):
                        if genres[i] == x[0]:
                            auxLine.append(genreKey[i])
                newLines.append(auxLine)
            line += 1
        else:
            break

with open('creatingDataSet2/dataSetRicky.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    writer.writerow(
        ["title", "artist", "date", "energy", "liveness", "tempo", "speechiness", "acousticness", "genre"])
    for line in newLines:
        writer.writerow([line[0], line[1], line[2], line[3],
                         line[4], line[5], line[6], line[7], line[8]])
