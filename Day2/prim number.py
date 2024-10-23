import math

def isPrime(n): # prim are dvz doar pe 1 si pe el insusi
    if n < 2:   # daca-i mai mic ca 2 nu se poate 
        return False
    if n == 2:  # daca-i 2 e ok
        return True

    for i in range(2, int(math.sqrt(n)) + 1):   #mergem de la 2 pana la radicalu numarului + 1
        if n % i == 0:  # daca gasim un numar care e dvz cu n atunci nu poate fi prim 
            return False

    return True
    
a = int(input("Number: "))
print(isPrime(a))