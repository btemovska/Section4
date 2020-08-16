age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:  #both conditions need to be true
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:  #Either of these conditions need to be true
    print("Enjoy your free time")
else:
    print("Have a good day at work")
