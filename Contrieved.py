numbers = [1,45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The numbers are unaccetable")
        break
else:
    print("All those number are fine")

