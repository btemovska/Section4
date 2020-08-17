import random

highest = 10
answer = random.randint(1, highest)  #random is the module, randINT is function
print(answer) #TODO: remove after testing

print("Please guess number 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input()) #giving the user another chance
    if guess == answer:
        print("Well done you guess it")
    else:
        print("Sorry, you have not guessed correctly")

