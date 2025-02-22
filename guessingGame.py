from random import randint

def guessing_game():
    x = randint(1, 50)
    attempts = 0

    while attempts < 3:
        try:
            n = int(input("Guess a number (1-50): "))

            if n == x:
                print("You guessed it right!")
                return True

            print("Wrong guess, try again.")
            attempts += 1

        except ValueError:
            print("Invalid input, enter a number.")

    print(f"You lost! The correct number was {x}.")
    return False
