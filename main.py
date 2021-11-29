# Number Guessing Game

import random
from art import logo

print(logo)
HARD_TRIES = 5
NORMAL_TRIES = 10


def decrease_tries(turns):
    return turns - 1


def set_difficulty(difficulty):
    if difficulty == "h":
        return HARD_TRIES
    elif difficulty == "n":
        return NORMAL_TRIES
    else:
        print("Invalid option, please enter N or H")
        return 0


print("Player Difficulty:")
tries = 0
while tries == 0:
    player_difficulty = input("Would you like to play on Hard [H], or Normal [N]?: ").lower()
    tries = set_difficulty(player_difficulty)

number_to_guess = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
game_won = False

while tries > 0 and not game_won:
    user_guess = int(input("What number is your guess?: "))

    if user_guess > number_to_guess:
        print(f"{user_guess} is too high")
        tries = decrease_tries(tries)
        print(f"You have {tries} tries left")
    elif user_guess < number_to_guess:
        print(f"{user_guess} is too low")
        tries = decrease_tries(tries)
        print(f"You have {tries} tries left")
    else:
        print("You guessed it! You win!")
        game_won = True

if tries == 0:
    print(f"Sorry, you lost! The number was {number_to_guess}")
