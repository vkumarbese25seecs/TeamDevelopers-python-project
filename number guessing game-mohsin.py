import random

def mohsin_guess_game():
    print("Welcome to the Number Guessing Game!")

    while True:  # Loop to allow replay
        number = random.randint(1, 50)
        attempts = 0

        print("\nI have selected a number between 1 and 50. Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess > number:
                print("Too high! Try again.")
            elif guess < number:
                print("Too low! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                break

        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()

        if play_again not in ("yes", "y"):
            print("Thank you for playing! Goodbye!")
            break


# Run the function
mohsin_guess_game()
