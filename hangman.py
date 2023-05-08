""" Command line hangman game. """

# Standard library imports
import re
import requests


difficulty_levels = {"easy": 15, "medium": 10, "hard": 5}

def select_parameters():
    """ Allow user to input game parameters via command line. """

    # Choose difficulty level
    print("\nChoose your difficult level: easy, medium, or hard.\n")
    difficulty = str(input()).lower()
    print("") # For whitespacing

    return difficulty

def guess_letter(guess, word, number_of_lives, correct_guesses):
    """ Check if the user guesses correctly, should they guess a letter. """

    if guess in word:

        print(f"{guess} is in the word")
        match_indexes = [m.span() for m in re.finditer(guess, word)]

        for idx in match_indexes:
            correct_guesses = correct_guesses[:idx[0]]+guess+correct_guesses[(idx[0]+1):]

    else:

        print(f"{guess} is not in the word")
        number_of_lives -= 1

    return number_of_lives, correct_guesses


def guess_word(guess, word, number_of_lives, correct_guesses):
    """ Check if the user guesses correctly, should they guess a whole word. """

    if guess == word:
        correct_guesses = word

    else:

        print(f"{guess} is not the word")
        number_of_lives -= 1

    return number_of_lives, correct_guesses


def hangman():
    """Main function to run the hangman game. """

    # Select a random word using the Random Word API
    # Used under the DWTFYW license
    word = requests.get("https://random-word-api.herokuapp.com/word").json()[0]

    correct_guesses = "*" * len(word)                  # Variable displays blank, unguessed letters, and those correctly guessed
    difficulty = select_parameters()                   # Difficulty level chosen
    number_of_lives = difficulty_levels[difficulty]    # The number of lives the user receives when they start the game

    while correct_guesses != word:

        print("\n", correct_guesses, "\n")

        if number_of_lives == 0:

            print(f"Game over! Unfortunately you weren't able to guess the word '{word}' in {difficulty_levels[difficulty]} guesses.")
            return 1

        # Ask for a guess until an input is given
        guess = ""
        while len(guess) == 0:
            guess = str(input("Guess a letter: ")).rstrip().lower()

        # Check if the guess is correct
        if len(guess) == 1:
            # If the user guesses a letter
            number_of_lives, correct_guesses = guess_letter(guess, word, number_of_lives, correct_guesses)

        else:
            # If the user guesses a word
            number_of_lives, correct_guesses = guess_word(guess, word, number_of_lives, correct_guesses)

    # If the word is correctly guessed
    print(f"Well done! The word was {word}, which you guessed with {number_of_lives} lives left\n\n")
    return 0

def main():
    hangman()

if __name__ == "__main__":
    main()