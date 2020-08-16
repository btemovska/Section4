parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter in parrot:
    print("{} as in {}".format(letter, parrot))
else:
    print("I don't need that letter")
#note this is case sensitive
