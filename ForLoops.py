parrot = "Norwegian Blue"
for character in parrot:
    print(character) #each letter is on its own row


number = "9,223;372:036 854,775:807"
separators = ""

for char in number: #first character is 9
    if not char.isnumeric(): #then it comes down here to check if it is a number
        separators = separators + char #this gets executed when the character is not numeric

print(separators)  #,;: ,:

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values]) #[9, 223, 372, 36, 854, 775, 807]


#calculate the sum
num = input("Please enter a series of numbers using separators")
sep = ""

for char in num:
    if not char.isnumeric():
        sep = sep + char
values = "".join(char if char not in sep else " " for char in num).split()
print(sum([int(val) for val in values]))

#challenge
#write a program that prints out the capital letters in the string
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char)