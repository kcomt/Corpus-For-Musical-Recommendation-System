

textFile = open("creatingBagOfWords/tokens5.txt", "r", encoding='latin-1')
tokens5 = textFile.read().split(",")

for i in range(len(tokens5)):
    tokens5[i] = tokens5[i].replace(" ", "")
    tokens5[i] = tokens5[i].replace("'", "")
    tokens5[i] = tokens5[i].replace("[", "")
    tokens5[i] = tokens5[i].replace("]", "")

cont = 0
bag = []
for word in tokens5:
    print(cont)
    cont += 1
    if word not in bag:
        bag.append(bag)

textFile = open("creatingBagOfWords/bagOfWords.txt", "w")
n = textFile.write(str(bag))
textFile.close()
