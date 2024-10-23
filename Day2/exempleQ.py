# storing a person name, age and average test score
person = dict(name="Clau", age=21, avgScore=6.7)

print("Hello " + person["name"] + " , you are " + str(person["age"]) + " years old and your score is " + str(person["avgScore"]))


# list of fruits and acces them by index
fruits = ["banana", "apple", "orange"]
for i in range (0, len(fruits)):
    print(fruits[i])