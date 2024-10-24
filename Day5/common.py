def comm(s1, s2):
    s3 = []

    for i in range(0, len(s1)):
        if s1[i] in s2:
            s3.append(s1[i])
        
    return s3

def dupl(s):
    s2 = []

    for i in range(0, len(s)):
        if s[i] not in s2:
            s2.append(s[i])

    return s2

s1 = [1, 4, 6, 0, 2, 5, 9, 2]
s2 = [9, 3, 6, 2, 1]

print("Coomon numbers: ", comm(s1, s2))
print("Common numbers without duplicates: ", dupl(comm(s1,s2)))
