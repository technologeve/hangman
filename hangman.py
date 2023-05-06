""" Hangman game. """

# Standard library imports
import random
import re

MAX_NO_OF_WRONG_GUESSES = 10

def hangman():
    """Main function to run the hangman game. """

    word = random.choice(["hello", "one", "eleven", "four"]) # Select a random word from the list

    correct_guesses = "*" * len(word)
    guess_attempts = 0

    while correct_guesses != word:
        print(correct_guesses)
        if guess_attempts == MAX_NO_OF_WRONG_GUESSES:

            print(f"You're dead, it took you 10 guesses and you didn't guess the word was {word}.")
            return 1

        guess = str(input("Guess a letter: "))[0].lower()

        if guess in word:

            print(f"{guess} is in the word")
            match_indexes = [m.span() for m in re.finditer(guess, word)]

            for idx in match_indexes:
                correct_guesses = correct_guesses[:idx[0]]+guess+correct_guesses[(idx[0]+1):]

        else:

            print(f"{guess} is not in the word")
            guess_attempts += 1

    print(f"Well done! The word was {word}, which you guessed with {MAX_NO_OF_WRONG_GUESSES-guess_attempts} lives left")
    return 0

