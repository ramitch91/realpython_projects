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
    if response == 'quit' or response == 'exit':
        exit(0)
    elif response == "add":
        word_to_add = input("Enter new 5 letter word to add to wordle list: ").lower()
        wordle_list.add_word_to_wordle_list(word_to_add)
    elif response == "delete":
        word_to_remove = input("Enter new 5 letter word to delete from the wordle list: ").lower()
        wordle_list.remove_word_from_wordle_list(word_to_remove)
    elif len(response) != 5:
        print("You must enter a 5 letter word")
    else:
        check_word(response, wordle_word)


def check_word(word_to_check, wordle_word):
    for i in range(5):
        if word_to_check[i] == wordle_word[i]:
            print(f"{Fore.GREEN}{word_to_check[i]}", end=' ')
        elif word_to_check[i] in wordle_word:
            print(f"{Fore.YELLOW}{word_to_check[i]}", end=' ')
        else:
            print(f"{Fore.RED}{word_to_check[i]}", end=' ')

    print()


def print_header():
    print()
    print(f"{Fore.BLUE}---------------------------------")
    print(f"{Fore.BLUE}      Welcome to wordle")
    print(f"{Fore.BLUE}  Written by Ricky Mitchell")
    print(f"{Fore.BLUE}---------------------------------")
    print()


def print_instructions():
    print(f'A correct letter in the correct place will show up as {Fore.GREEN}GREEN')
    print(f'A correct letter in the wrong place will show up as {Fore.YELLOW}YELLOW')
    print(f'An incorrect letter will show up as {Fore.RED}RED')
    print()
    print(f'To add a new word to the wordle list type {Fore.CYAN}add')
    print(f'To delete a word from the wordle list type {Fore.CYAN}delete')
    print(f'To exit the game early, type {Fore.CYAN}quit or exit')
    print()


def play_game(wordle_word):
    print(f"Your word is {Fore.BLUE}_____")
    count = 0
    while count in range(MAX_GUESSES):
        word_guess = input("Enter your word guess: ").lower()
        # if word_guess == "add":
        #     word_to_add = input('What word would you like to add to the wordle list? ').lower()
        #     if len(word_to_add) != 5:
        #         print(f'{word_to_add} is not a 5-letter word.  You must enter a 5-letter word.')
        #         break
        #     else:
        #         wordle_list.add_word_to_wordle_list(word_to_add)
        #         break
        # elif word_guess == 'delete':
        #     word_to_delete = input('What word would you like to delete from the wordle list? ').lower()
        #     wordle_list.remove_word_from_wordle_list(word_to_delete)
        #
        check_response(word_guess, wordle_word)
        if word_guess == wordle_word:
            print(f"Congratulations, you guessed the word in {count + 1} tries!")
            break
        elif count == 5:
            print(f"Sorry, the word was {Fore.BLUE}{wordle_word.upper()}. {Fore.WHITE}Better luck next time")
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


if __name__ == '__main__':
    main()
