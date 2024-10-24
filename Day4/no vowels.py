def noV(l):
    l1 = []

    v = ['a', 'e', 'i', 'o', 'u']

    for i in range(0, len(l)):
        if l[i] not in v:
            l1.append(l[i])

    new = ''.join(l1)
    return new

l = "vocale"
print(noV(l))