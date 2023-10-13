secret_number = 8

while True:
    guessed_number = int(input("Guess a number between 1 and 10: "))
    if guessed_number != secret_number:
        print("Guess again!")

    elif guessed_number == secret_number:
        print("You guessed the right number")
        break