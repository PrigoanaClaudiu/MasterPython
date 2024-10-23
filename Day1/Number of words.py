def numberOfWords(sentance):    # verificam daca caracterul pe care suntem e litera si daca cel din spate e spatiu
    if sentance:
        n = 1   # incepem de la 1 daca sentance nu e gol
        for i in range(1, len(sentance)):
            if sentance[i].isalpha() and sentance[i-1] == " ":
                n += 1
    else:
        n = 0   # daca e gol nu sunt cuvinte
    return n


sentance = input("Sentance: ")
print("Number of words: ", numberOfWords(sentance))


# V2
def numOfWords(sentance):
    n = 0
    s = sentance.split() # impartim in cuvinte

    for w in s:
        if w:
            n += 1
    return n

print("Number of words V2: ", numOfWords(sentance))