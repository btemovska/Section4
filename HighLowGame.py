#have the computer guess your number
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start")

guesses = 1
while True:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less then the guess
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses !".format(guesses))
        break
    else:
        print("Please enter h, l, or c")

    guesses = guesses + 1

# Please think of a number between 1 and 1000
# Please ENTER to start
    # Guessing in the range of 1 to 1000
# My guess is 500. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
    # Guessing in the range of 1 to 499
# My guess is 250. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
    # Guessing in the range of 251 to 499
# My guess is 375. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
    # Guessing in the range of 376 to 499
# My guess is 437. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
    # Guessing in the range of 438 to 499
# My guess is 468. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
    # Guessing in the range of 438 to 467
# My guess is 452. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
    # Guessing in the range of 438 to 451
# My guess is 444. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
    # Guessing in the range of 445 to 451
# My guess is 448. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
    # Guessing in the range of 449 to 451
# My guess is 450. Should I guess higher or lower? Enter h or l, or c if my guess was correct c
# I got it in 9 guesses !
