#if the user makes a valid chose, the program should print a short message
# the message should include the value that they typed
#if their chose isn't one of the options in the menu, nothing should be printed
#(although you will see their input on the screen)
#modify the program so that the menu is printed again, if they choose an invalid option
#Please choose your option from the list below:
# 1. Lean Python
# 2. Lean Java
# 3. Go Swimming
# 4. Have dinner
# 5. Go to bed
# 0. Exit

print("Please choose from the menu:")
print("0. Exit","\n1. Learn Python", "\n2. Learn Java", "\n3. Go Swimming",
      "\n4. Have dinner", "\n5. Go to bed")
option = int(input())

while option != 0:
    if option == 1:
        print("You have chosen to lean Python")
        break
    elif option == 2:
        print("You have chosen to lean Java")
        break
    elif option == 3:
        print("You have chosen to go swimming")
        break
    elif option == 4:
        print("You have chosen to have dinner")
        break
    elif option == 5:
        print("You have chosen to go to bed")
        break
    else:
        print("Please choose from the menu:")
        print("0. Exit","\n1. Learn Pythin", "\n2. Learn Java", "\n3. Go Swimming", "\n4. Have dinner",
          "\n5. Go to bed")
    option = int(input())
else:
    print("Bye")
#with this you can tell I have Java as my first language LOL



#intructors way of writing this challenge:

# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5\tGo to bed")
# print("0:\tExit")

choice = "-"
while choice != "0":
    if choice in "12345":
        print("You have chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5\tGo to bed")
        print("0:\tExit")

    choice = input()




