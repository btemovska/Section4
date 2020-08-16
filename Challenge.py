name = input("Please enter your NAME: ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to club 18-30 holiday {} ".format(name))
else:
    print("You are not allowed to enter")
