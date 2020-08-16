answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess HIGHER")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Guess LOWER")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You guessed it right!")

    #if comes first, elif comes second, and else comes last

#USING OPERATORS FOR BETTER CODE AS WE HAVE DUPLICATED LINES ABOVE
if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else: #guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you've guess it")
    else:
        print("Sorry you have not guessed correctly")
else:
    print("You got it the first time")

#Challenge
if guess == answer:
    print("You got it the first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you've guess it")
    else:
        print("Sorry you have not guessed correctly")