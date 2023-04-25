"""
This script implements a simple Hangman game. The player has to guess letters
in a word and if they guess incorrectly too many times, they lose the game.
Author: Armand Amores
"""

import random
from asciiart import stages, hangman_logo
from words import word_list
import os

#selects randomly chosen word from imported word list
chosen_word = random.choice(word_list)
#controls state of game0
flag = False
#tracks user lives
lives = 6
#guessed letters gets appened to guessed list
guessed = []

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#sets up blank lines
display = []
for value in chosen_word:
    display.append("_")


#break chosen words into individual letters and create list
characters = list(chosen_word)


def clear_screen():
    """Clears cmd line screen to present cleaner ui"""
    os.system('cls' if os.name == 'nt' else 'clear')

#Game will run until Flag
while not flag:
    clear_screen()
    print(hangman_logo)
    print(f"Lives: {lives}")
    print("Guessed letters: " + ",".join(guessed))
    print(stages[lives])
    print(" ".join(display))
    # print(chosen_word) test code

    #ask user for user input
    guess = input("Enter a Letter: ")

    #checks to see if letter matches, replaces _ in display
    for letter in range(len(characters)):
        if guess == characters[letter]:
            display[letter] = guess

    #adds to letters guessed
    if guess not in guessed:
        guessed.append(guess)
    #checks to see if win
    if "_" not in display:
        flag = True
    #losing scenerio
    if guess not in characters:
        lives -= 1
        if lives == 0:
            clear_screen()
            flag = True

#once while loop ends updates screen
print(hangman_logo)
print(f"Lives: {lives}")
print("Guessed Words: " + ",".join(guessed))
print(stages[lives])
if lives == 0:
    print("Game Over!")
    print(f"The word was {chosen_word}")
elif lives > 0:
    print("You Win!")
