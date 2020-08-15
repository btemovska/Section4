for i in range(1, 13): #this is for loop
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
    print("*" * 80)
#  No. 1 squared is 1 and cubed is    1
# ********************************************************************************
# No. 2 squared is 4 and cubed is    8
# ********************************************************************************
# No. 3 squared is 9 and cubed is   27
# ********************************************************************************

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back {0} years".format(18 - age)) #this will calc how many years you need


if age <= 18:
    print("Please come back {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

