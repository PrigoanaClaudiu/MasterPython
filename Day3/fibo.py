def fibo(a):
    l = []
    if a <= 0:
        return l
    elif a == 1:
        l.append(1)
    elif a >= 2:
        l.append(1)
        l.append(1)

    if a > 2:
        for i in range(2, a):
            l.append(l[i-2] + l[i-1])

    return l

a = int(input("Give the number for fibo: "))
print(fibo(a))
