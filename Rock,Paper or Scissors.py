import os
os.system('cls')


import random
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
computer_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    if player == computer:
        print("Tie!")
        print(f"Computer picked {computer} ")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
            print(f"Computer picked {computer} ")
            computer_score+=1
        else:
            print("You win!")
            print(f"Computer picked {computer} ")
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
            print(f"Computer picked {computer} ")
            computer_score+=1
        else:
            print("You win!")
            print(f"Computer picked {computer} ")
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!")
            
            computer_score+=1
        else:
            print("You win!")
            print(f"Computer picked {computer} ")
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{computer_score}")
        print(f"Plaer:{player_score}")
        break