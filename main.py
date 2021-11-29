#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)

print("Player Difficulty:")
tries = 0
valid_answer = False
while not valid_answer:
    player_difficulty = input("Would you like to play on Hard [H], or Normal [N]?: ").lower()

    if player_difficulty == "h":
        tries = 5
        valid_answer = True
    elif player_difficulty == "n":
        tries = 10
        valid_answer = True
    else:
        print("Invalid option, please enter N or H")

number_to_guess = random.randint(1, 101)

