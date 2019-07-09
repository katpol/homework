secret = 13
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 50): "))

if guess == secret:
    print("Congratulations - you've guessed it!!")


else:
    print("Sorry, your guess wasn't correct, the secret number is not " +str(guess))