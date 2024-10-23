def pangram(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    word = word.lower()
    
    for l in alphabet:
        if l not in word:
            return False
    
    return True

word = "abcdefghijklmnopqrstuvwxyzaaaa"

if pangram(word):
    print("Pangram")
else:
    print("Not pangram")
