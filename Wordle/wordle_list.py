"""
wordle_list
.py created by Ricky Mitchell ramitch91@gmail.com on 2/26/2022
Creates a unique wordle word list to use in the wordle.py program. It will
also allow you to add words to the list and remove words from the list.
"""

import csv


def get_wordle_word_list() -> list:
    """
    Retrieves the wordle_list from the wordle_list file

    parameters: None

    return: wordle_list as list
    """

    wordle_list = []
    with open("wordlelist.csv", "r", encoding="utf-8") as file_in:
        for line in file_in:
            word = line[:5]
            wordle_list.append(word)

    return wordle_list


def convert_list_to_list_of_list(list_to_convert: list) -> list:
    """
    Takes a list and converts it to a list of list in order to save
    it in the proper format.

    parameters: list_to_convert as list

    return converted_list as list
    """

    converted_list = []
    for word in list_to_convert:
        temp_list = []
        temp_list.append(word)
        converted_list.append(temp_list)

    return converted_list


def save_wordle_list_to_file(list_to_save: list) -> None:
    """
    Takes a list of words and saves it to the wordle_list csv

    parameters: list_to_save as list

    return: None
    """

    wordle_list_to_save = convert_list_to_list_of_list(list_to_save)
    with open("wordle_list.csv", "w", encoding="utf-8") as file_out:
        write = csv.writer(file_out)
        write.writerows(wordle_list_to_save)


def add_word_to_wordle_list(new_word: str) -> bool:
    """
    Attemps to add a new word to the wordle_list file
    - Checks to make sure the word is a 5 letter word, if not it returns False
    - Checks to see if the new_word is already in the word_list file, if so returns False
    - Returns True if the new word was added to the word_list file

    parameters: new_word as str

    retun: bool
    """

    current_wordle_list = get_wordle_word_list()
    if new_word in current_wordle_list:
        print(f"The word {new_word} is already in the wordle word list")
        return False

    current_wordle_list.append(new_word)
    save_wordle_list_to_file(current_wordle_list)
    print(f"The word {new_word} has been added to the wordle word list")
    return True


def remove_word_from_wordle_list(word_to_remove: str) -> bool:
    """
    Attemps to remove a word from the wordle_list file
    - Checks to make sure if the word is in the word_list file
        - if not, it returns False
        - if so, it will remove the word from the word_list file and return True

    parameters: new_word as str

    retun: bool
    """

    current_wordle_list = get_wordle_word_list()
    if word_to_remove not in current_wordle_list:
        print(f"The word {word_to_remove} is not in the wordle word list.")
        return False

    current_wordle_list.remove(word_to_remove)
    save_wordle_list_to_file(current_wordle_list)
    print(f"The word {word_to_remove} has been removed from the wordle word list")
    return True
