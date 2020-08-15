answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess HIGHER")
elif guess > answer:
    print("Guess LOWER")
else:
    print("You guessed it right!")


    #if comes first, elif comes second, and else comes last