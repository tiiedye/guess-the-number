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
tries = 0


def decrease_tries():
    global tries
    tries -= 1


valid_answer = False
print("Player Difficulty:")

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

print("I'm thinking of a number between 1 and 100")
# TESTING PURPOSES
print(number_to_guess)

game_won = False

while tries > 0 and not game_won:
    user_guess = int(input("What number is your guess?: "))

    if user_guess > number_to_guess:
        print(f"{user_guess} is too high")
        decrease_tries()
        print(f"You have {tries} tries left")
    elif user_guess < number_to_guess:
        print(f"{user_guess} is too low")
        decrease_tries()
        print(f"You have {tries} tries left")
    else:
        print("You guessed it! You win!")
        game_won = True

if tries == 0:
    print(f"Sorry, you lost! The number was {number_to_guess}")