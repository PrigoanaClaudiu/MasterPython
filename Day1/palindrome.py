# reversed() return iterator 

def pali(text):
    if text == text[::-1]:
        return True
    else:
        return False
    
text = input("Give an example for palindrome: ")
print(pali(text))