"""
wordle.py - Created by Ricky Mitchell ramitch91@gmail.com
Creates a wordle word game, where every word is 5 letters.

It will give you the first letter and will tell you when
you have a correct letter in the correct location, a correct
letter in the wrong location and letters that are incorrect.

Example:
if the wordle word is bagel, the game will give you the first
letter "b" and 4 blanks or '_'.  The "b" would be colored green because
it would be in the correct location.

If you guess a letter that is correct and in the correct location,
it will be placed in the word and shown in a green color. If you
guess a correct letter but the letter is in the wrong place,
it will be shown in the place in which you guessed it, but it will
be shown in a red color. Any of the letters that you guess are
incorrect, a blank or '_' will be shown in that location.

"""

import sys
import random
import colorama
from colorama import Fore

from Wordle import wordle_list

colorama.init(autoreset=True)
MAX_GUESSES = 6


def choose_a_word_from_wordle_list() -> str:
    """
    Retrieves a single word from the wordle_list file

    parameters: None

    return: wordle_word as str
    """

    word_list = wordle_list.get_wordle_word_list()
    wordle_word = random.choice(word_list)
    return wordle_word


def check_response(response: str, wordle_word: str) -> None:
    """
    Checks response from user input to determine what action to take:
    - if response == 'quit' then exit the game
    - if response == 'exit' then exit the game
    - if response == 'add' then add a new word to the wordle_list file
    - if response == 'delete' then remove a word from the wordle+_list file
    - if response == 'remove' then remove a word from the wordle_lsit file
    - if response is not 5 characters the let the user know that a 5 letter word must be entered

    parameters:
    response as str,
    wordle_word as str

    return: None
    """

    if response == "add":
        word_to_add = input("Enter new 5 letter word to add to wordle list: ").lower()
        wordle_list.add_word_to_wordle_list(word_to_add)
    elif response in ("delete", "remove"):
        word_to_remove = input(
            "Enter new 5 letter word to delete from the wordle list: "
        ).lower()
        wordle_list.remove_word_from_wordle_list(word_to_remove)
    elif response in ("quit", "exit"):
        sys.exit()
    elif len(response) != 5:
        print("You must enter a 5 letter word")
    else:
        check_word(response, wordle_word)


def check_word(word_to_check: str, wordle_word: str) -> None:
    """
    Checks each letter of the word_to_check is in the wordle_word.
    - If the letter is in the wordle_word and in the correct location,
    the letter will be printed to the screen in a green color.
    - If the letter is in the wordle_word but in the wrong location,
    the letter will be printed to the screen in a yellow color.
    - If the letter is not in the wordle_word, the letter will be
    printed to the screen in a red color.


    paramters:
    word_to_check as str,
    wordle_word as str

    return: None
    """

    for i in range(5):
        if word_to_check[i] == wordle_word[i]:
            print(f"{Fore.GREEN}{word_to_check[i]}, end=''")
        elif word_to_check[i] in wordle_word:
            print(f"{Fore.YELLOW}{word_to_check[i]}, end=''")
        else:
            print(f"{Fore.RED}{word_to_check[i]}, end=''")

    print()


def print_header():
    """
    Prints a welcome header for the game to the screen

    parameters: None

    return: None
    """

    print()
    print(f"{Fore.BLUE}---------------------------------")
    print(f"{Fore.BLUE}      Welcome to wordle")
    print(f"{Fore.BLUE}  Written by Ricky Mitchell")
    print(f"{Fore.BLUE}---------------------------------")
    print()


def print_instructions() -> None:
    """
    Prints the instructions to the screen

    parameters: None

    return: None
    """

    pass


def play_game(wordle_word: str) -> None:
    """
    Plays the game until the answer is correct or you reach the maximum number of guesses

    parameters:
    wordle_word as str

    return: None
    """

    print(f"Your word is {Fore.GREEN}{wordle_word[0]}{Fore.BLUE}____")
    count = 0
    while count in range(MAX_GUESSES):
        word_guess = input("Enter your word guess: ").lower()
        check_response(word_guess, wordle_word)


def main() -> None:
    """
    Main Function

    parameters: None

    return: None
    """

    print_header()
    print_instructions()
    wordle_word = choose_a_word_from_wordle_list()
    print(f"{Fore.GREEN}{wordle_word[0]}{Fore.BLUE}____")
    while True:
        play_game(wordle_word)


# Ask the user to guess a word
# Convert the response to lowercase
# Compare the guess to the wordle word letter by letter
# If the letter is correct and in the correct position, change the
# color of that letter to green.
# If the letter is in the word but in the incorrect position, change
# the color of the letter to red.
# Replace the '_' spaces with the correct letters in their respective
# colors


if __name__ == "__main__":
    main()
