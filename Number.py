import random

secret_number = random.randint(1, 100)

tries = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 100): "))

    tries += 1

    if guess == secret_number:
        print("Congratulations! You guessed the number in", tries, "tries.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
