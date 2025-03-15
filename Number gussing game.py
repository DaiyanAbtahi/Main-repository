import os
import random


def get_user_guess(low, high):
    """Prompt the user for a valid number within the range."""
    while True:
        try:
            guess = int(input(f"🔢 Enter a number between {low} and {high}: "))
            if low <= guess <= high:
                return guess
            else:
                print(f" Please enter a number within the range {low}-{high}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_game():
    while True:
        os.system('cls')
        print("Let's play a number guessing game!")

        low, high = 1, 100
        number_to_guess = random.randint(low, high)
        attempts = 0

        while True:
            guess = get_user_guess(low, high)
            attempts += 1
            if guess < number_to_guess:
                print("⬇️ Too low! Try again.")
            elif guess > number_to_guess:
                print("⬆️ Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it right in {attempts} attempts. ")
                break
        
        play_again = input(" Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! See you next time.")
            break


if __name__ == "__main__":
    play_game()
