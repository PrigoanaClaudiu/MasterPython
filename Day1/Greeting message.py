def validateUser(userName, userAge):
    if not userName.isalpha():
        return "Eroare"
    
    if not userAge.isnumeric():
        return "Eroare"
    
    return "Hello " + userName + " I know you are " + userAge + " years old."


userName = input("User name: ")
userAge = input("User age: ")

print(validateUser(userName, userAge))