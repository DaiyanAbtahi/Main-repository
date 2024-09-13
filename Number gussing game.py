import os
os.system('cls')
import random

print("Let's play a game ")

high = 100
low = 1

while True:
    try:
        guess = int(input(f"enter a number between {low} - {high} : "))
        break
    except:
        print('please enter a number')
        break



num = random.randint(low,high)

while num!= guess:
    if guess < num:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > num:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")