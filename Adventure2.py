available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("aren't you glad you got out of there")
#the else on line 9 will not print the message on line 10

#Please choose a direction: down
# Please choose a direction: up
# Please choose a direction: north
# aren't you glad you got out of there
