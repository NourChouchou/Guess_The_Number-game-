import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Ask the player for their guess
            guess = int(input("Take a guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    guess_the_number()
