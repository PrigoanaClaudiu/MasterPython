# a given number is positive, negative or 0 
a = int(input("Give us the number: "))
if a == 0:
    print("It's 0")
elif a < 0:
    print("It's negative.")
else:
    print("It's positive.")

# create a loop that prints the first 10 even numbers
i = 1
list = []
while len(list) < 10:
    if i % 2 == 0:
        list.append(i)

    i += 1
print("The fist 10 even numbers are: ", list)

# finds the largest number in a list
list2 = [1, 4, 7, 2, 4, 2]
maxi = list2[0]
for i in range(len(list2)):
    if list2[i] > maxi:
        maxi = list2[i]
print("The maximum is: ", maxi)