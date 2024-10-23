def maxMin(numbers):
    min_val = numbers[0]
    max_val = numbers[0]

    for n in numbers:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
    return min_val, max_val

numbers = [3, 5, 1, 8, 2]
minim, maxim = maxMin(numbers)

print("Smallest number: ", minim)
print("Biggest number: ", maxim)

# another one

minimV = min(numbers)
maximV = max(numbers)
print("Smallest number: ", minimV)
print("Biggest number: ", maximV)
