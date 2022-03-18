"""
wordle_list
.py created by Ricky Mitchell ramitch91@gmail.com on 2/26/2022
Creates a unique wordle word list to use in the wordle.py program. It will
also allow you to add words to the list and remove words from the list.
"""
import csv


def get_wordle_word_list():
    wordle_list = []
    with open("wordle_list.csv", "r", encoding="utf-8") as file_in:
        for line in file_in:
            word = line[:5]
            wordle_list.append(word)

    return wordle_list


def convert_list_to_list_of_list(list_to_convert):
    converted_list = []
    for word in list_to_convert:
        temp_list = []
        temp_list.append(word)
        converted_list.append(temp_list)

    return converted_list


def save_wordle_list_to_file(list_to_save):
    wordle_list_to_save = convert_list_to_list_of_list(list_to_save)
    with open("lingolist.csv", "w", encoding="utf-8") as file_out:
        write = csv.writer(file_out)
        write.writerows(wordle_list_to_save)


def add_word_to_wordle_list(new_word):
    current_wordle_list = get_lingo_word_list()
    if new_word in current_wordle_list:
        print(f"The word {new_word} is already in the lingo word list")
        return False
    else:
        current_wordle_list.append(new_word)
        save_wordle_list_to_file(current_wordle_list)
        print(f"The word {new_word} has been added to the lingo word list")
        return True


def remove_word_from_wordle_list(word_to_remove):
    current_wordle_list = get_lingo_word_list()
    if word_to_remove not in current_wordle_list:
        print(f"The word {word_to_remove} is not in the lingo word list.")
        return False
    else:
        current_wordle_list.remove(word_to_remove)
        save_wordle_list_to_file(current_wordle_list)
        print(f"The word {word_to_remove} has been removed from the lingo word list")
        return True
