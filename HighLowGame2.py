#have the computer guess your number
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please ENTER to start")

guesses = 1
while low != high:
    # print("\tGuessing in the range of {} to {}".format(low, high))
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

else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses ".format(guesses))

# Please think of a number between 1 and 1000
# Please ENTER to start
# My guess is 500. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
# My guess is 250. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
# My guess is 125. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
# My guess is 62. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
# My guess is 93. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
# My guess is 109. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
# My guess is 101. Should I guess higher or lower? Enter h or l, or c if my guess was correct l
# My guess is 97. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
# My guess is 99. Should I guess higher or lower? Enter h or l, or c if my guess was correct h
# You thought of the number 100
# I got it in 10 guesses