secret_number = 5
attempts = 3
attempt_count = 0

while attempt_count < attempts:
    guess = int(input("Guess the secret number between 1 and 10.You have 3 tries: "))
    attempt_count += 1

    if guess == secret_number:
        print("Congratulations! You've guessed the secret number.")
        break
    elif guess != secret_number and attempt_count < attempts:
        print("Try again!")
    else:
        print("Exhausted number of attempts.You lose!")
     