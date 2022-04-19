# wordle clone that doesnt use words with duplicate letters

import random
from colorama import Fore, Back, Style

words = []
illegal_char = ('\'', '-')
repeat_test = set()


# function to filter out the unusable words
def correct_words():
    f = open('words.txt')
    for line in f:
        word = line[:-1]
        if len(word) == 5:
            if word.isalpha() and str(illegal_char) not in word:
                for char in word:
                    repeat_test.add(char)
                if len(repeat_test) == 5:
                    words.append(word)
                repeat_test.clear()
    f.close()


# function to choose a random word from the usable words
def choose_word():
    return random.choice(words)


# function to run the main game
def game(chosen_word):
    history = []
    history_string = ''
    displayed_scores = ''
    won = False
    print('------WORDLE-----\n')
    # run the number of rounds
    for i in range(6):
        while True:
            guess = input(Fore.LIGHTWHITE_EX + 'make a guess at the word: ')
            if guess not in words:
                print('\nplease input a valid word, no duplicate letters\n')
            else:
                break
                # go through each character of the guess
        for ii in range(len(guess)):
            if guess[ii] in chosen_word:
                if guess[ii] == chosen_word[ii]:
                    displayed_scores += (Fore.GREEN + f'{guess[ii]}')
                    history_string += (Back.GREEN + ' ' + Style.RESET_ALL)
                else:
                    displayed_scores += (Fore.LIGHTYELLOW_EX + f'{guess[ii]}')
                    history_string += (Back.LIGHTYELLOW_EX + ' ' + Style.RESET_ALL)
            else:
                displayed_scores += (Fore.RED + f'{guess[ii]}')
                history_string += (Back.RED + ' ' + Style.RESET_ALL)

        history.append(history_string)
        print(displayed_scores)
        displayed_scores = ''
        history_string = ''

        if guess == chosen_word:
            outcome(chosen_word, history, True)
            break
    if guess != chosen_word:
        outcome(chosen_word, history, False)

    # function to display the win or loss, as well as the guessing history


def outcome(chosen_word, history, result):
    if result:
        print(Fore.LIGHTWHITE_EX + f'\nyou won! the correct word was {chosen_word}\n')
    else:
        print(Fore.LIGHTWHITE_EX + f'\nyou lost! the word was {chosen_word}\n')

    for block in history:
        print(block)

    # function to run the script


def setup():
    correct_words()
    chosen_word = choose_word()
    game(chosen_word)


setup()