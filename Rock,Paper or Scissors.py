import os
import random


def get_player_choice():
    """Get a valid choice from the player."""
    choices = ["Rock", "Paper", "Scissors"]
    while True:
        player = input("🪨 Rock, 📄 Paper, ✂️ Scissors? (or type 'End' to quit): ").capitalize()
        if player in choices or player == "End":
            return player
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")


def play_round(player_choice, computer_choice):
    """Play a single round and determine the result."""
    if player_choice == computer_choice:
        return "Tie", "It's a tie! "
    
    winning_combos = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    
    if winning_combos[player_choice] == computer_choice:
        return "Win", f" You win! Computer picked {computer_choice}"
    else:
        return "Lose", f" You lose! Computer picked {computer_choice}"


def play_game():
    os.system("cls")
    print("🎮 Let's play Rock, Paper, Scissors! 🪨📄✂️")

    computer_score = 0
    player_score = 0

    while True:
        player_choice = get_player_choice()
        if player_choice == "End":
            break
        
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result, message = play_round(player_choice, computer_choice)

        print(message)
        
        if result == "Win":
            player_score += 1
        elif result == "Lose":
            computer_score += 1

        print(f"📊 Scores → You: {player_score} | CPU: {computer_score}")
        
        play_again = input(" Play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    
    print(" Final Scores:")
    print(f" Player: {player_score}")
    print(f" Computer: {computer_score}")
    print(" Thanks for playing! See you next time.")


if __name__ == "__main__":
    play_game()
