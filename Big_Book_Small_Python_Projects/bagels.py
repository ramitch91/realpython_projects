"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book_small_python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10.
MAX_GUESSES = 10  # (!) Try setting this to 1 or 100


def main() -> None:
    """
    Main module

    parameters: None

    return: None
    """

    print(
        f"""Bagels, a deductive logic game, by Al Sweigart al@inventwithpython.com
    (typed and modified by Ricky Mitchell)

    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
        Pico        One digit is correct but in the wrong position.
        Fermi       One digit is correct and in the correct position.
        Bagels      No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico."""
    )

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}:")
                guess = input("> ")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # The guess is correct so break out of the loop.
            if num_guesses > MAX_GUESSES:
                print("You are out of guesses.")
                print(f"The answer was {secret_num}")

        # Ask player if they would like to play again
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def get_secret_num() -> str:
    """
    Returns a string made up of NUM_DIGITS unique random digits.

    parameters: None

    return: secret_num as str
    """

    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle the numbers into a random order.

    # Get the first NUM_DIGITS digits in te list for the secret number:
    secret_num = ""
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess: str, secret_num: str) -> list:
    """
    Returns a string with the Pico, Fermi, Bagels clues for a guess
    and secret number pair.

    parameters:
    guess as str,
    secret_num as str

    return: clues as list
    """

    if guess == secret_num:
        return "You got it!"

    clues = []

    for i in enumerate(guess):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append("Pico")
    if len(clues) == 0:
        clues.append("Bagels")  # There are no correct digits at all.
        return clues

    # Sort the clues into alphabetical order so their  original order
    # doesn't give information away.
    clues.sort()
    # Make a single string from the list of string clues.
    return " ".join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
