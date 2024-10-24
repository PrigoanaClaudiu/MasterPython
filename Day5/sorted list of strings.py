s = ['ceva', 'o', 'sa', 'iasa', 'magnific', 'de']
s1 = sorted(s, key=len)
print(s1)

# v2 - bubble sort

def sortam(s):
    n = len(s)

    for i in range(n):
        for j in range(0, n-i-1):
            if len(s[j]) > len(s[j+1]):
                s[j], s[j+1] = s[j+1], s[j]
    print(s)

sortam(s)