l = ["Alina", "Ceapa", "Apa", "Minge", "ceau", "cevalung"]
c = 0

for n in l:
    if len(n) > 5:
        c += 1
print("In list are " + str(c) + " words with 5 characters.")

str = "o propozitie mai lunga dar nu foartefoarte lunga"

def func(str):
    l = str.split()

    for n in l:
        if len(n) > 5:
            print(n)

func(str)