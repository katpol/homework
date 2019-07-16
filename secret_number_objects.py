import json
import random
import datetime

secret = random.randint(1, 30)
attempts = 0
guess = 0


with open("score.txt", "r") as score_file:
    best_score_list = json.loads(score_file.read())
    print("Top score: " + str(best_score_list))

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        best_score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
        print("Congratulations - you've guessed it!!")

        with open("score.txt", "w") as score_file:
            score_file.write(json.dumps(best_score_list))




    else:
        print("Sorry, your guess wasn't correct, the secret number is not " + str(guess))
