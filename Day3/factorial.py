def fact(n):
    if n == 0:
        return 1
    a = 1
    for i in range(1, n):
        a = a * i
    
    return a * n

n = int(input("The number is: "))
print("Factorial: ", fact(n))