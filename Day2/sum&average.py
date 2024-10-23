def sumAndAverage(list):
    s = 0
    for n in list:
        s = s + n
    return s, s/len(list)

list = [1, 6, 4, 7, 4, 5, 3]

sum, average = sumAndAverage(list)
print("The sum is: ", sum)
print("The average is: ", round(average, 3))