#unique elements from both lists
def unique(s1, s2):
    s3 = []

    for i in range(0, len(s1)):
        if s1[i] not in s3:
            s3.append(s1[i])
    
    for i in range(0, len(s2)):
        if s2[i] not in s3:
            s3.append(s2[i])
    print(s3)

s1 = [1, 2, 9, 4, 2, 6, 3, 1, 5]
s2 = [5, 3, 4, 2, 6, 7, 8, 4]
unique(s1, s2)