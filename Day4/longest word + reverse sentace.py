def longest(s):
    a = s.split()
    maxi = len(a[0])
    w = a[0]

    for b in a:
        if len(b) > maxi:
            w = b
            maxi = len(b)
    
    return w, maxi


sentance = "ceva propozitie nu lunga nu scurta"
word, length = longest(sentance)
print("The word: ", word)
print("The length: ", length)

# reverse order of a sentance
a = sentance.split()
a = a[::-1]
a = ' '.join(a)
print(a)


    