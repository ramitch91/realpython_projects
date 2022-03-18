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
import wordle_list
import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)
MAX_GUESSES = 6


def choose_a_word_from_wordle_list():
    word_list = wordle_list.get_wordle_word_list()
    wordle_word = random.choice(word_list)
    return wordle_word


def check_response(response, wordle_word):
    if response == "add":
        word_to_add = input("Enter new 5 letter word to add to wordle list: ").lower()
        wordle_list.add_word_to_wordle_list(word_to_add)
    elif response == "delete":
        word_to_remove = input(
            "Enter new 5 letter word to delete from the wordle list: "
        ).lower()
        wordle_list.remove_word_from_wordle_list(word_to_remove)
    elif len(response) != 5:
        print("You must enter a 5 letter word")
    else:
        check_word(response, wordle_word)


def check_word(word_to_check, wordle_word):
    for i in range(5):
        if word_to_check[i] == wordle_word[i]:
            print(f"{Fore.GREEN}{word_to_check[i]}", end='')
        elif word_to_check[i] in wordle_word:
            print(f"{Fore.YELLOW}{word_to_check[i]}", end='')
        else:
            print(f"{Fore.RED}{word_to_check[i]}", end='')

    print()


def print_header():
    print()
    print(f"{Fore.BLUE}---------------------------------")
    print(f"{Fore.BLUE}      Welcome to wordle")
    print(f"{Fore.BLUE}  Written by Ricky Mitchell")
    print(f"{Fore.BLUE}---------------------------------")
    print()


def print_instructions():
    pass


def play_game(wordle_word):
    print(f"Your word is {Fore.BLUE}_____")
    count = 0
    while count in range(MAX_GUESSES):
        word_guess = input("Enter your word guess: ").lower()
        check_response(word_guess, wordle_word)
        if word_guess == wordle_word:
            print(f"Congratulations, you guessed the word in {count + 1} tries!")
            break
        elif count == 5:
            print(f"Sorry, the word was {wordle_word.upper()}. Better luck next time")
            break
        else:
            count += 1


def main():
    print_header()
    print_instructions()
    wordle_word = choose_a_word_from_wordle_list()
    while True:
        play_game(wordle_word)
        answer = input("Would you like to play again? ").lower()
        if answer[0] == 'y':
            continue
        else:
            break

# Ask the user to guess a word
# Convert the response to lowercase
# Compare the guess to the wordle word letter by letter
# If the letter is correct and in the correct position, change the
# color of that letter to green.
# If the letter is in the word but in the incorrect position, change
# the color of the letter to red.
# Replace the '_' spaces with the correct letters in their respective
# colors


if __name__ == '__main__':
    main()