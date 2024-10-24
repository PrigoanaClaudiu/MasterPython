def noD(s):
    s1 = list(s)
    s2 = []

    for i in range(0, len(s)):
        if s[i] not in s2:
            s2.append(s[i])
    
    s2 = ''.join(s2)
    return(s2)

string = 'adio duplicate'

s = noD(string)

print(s)