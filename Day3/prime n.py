import math

def prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    
    if n > 2:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    
    return True

l = []
for i in range (1, 50):
    if prime(i):
        l.append(i)

print(l)