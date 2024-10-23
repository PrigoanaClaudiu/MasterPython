def vowles(string):
    vowles = ['a', 'e', 'i', 'o', 'u']

    n = 0

    for s in string:
        if s in vowles:
            n += 1

    return n

string = "exemple of string"

print(vowles(string))