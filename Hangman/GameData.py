# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class responsible for game state
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re
import json

class GameData:

    CURRENT_WORD = None
    NUMBER_OF_LIVES = None
    GUESSED_LETTERS = ''

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Getters
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetNumberOfLives():
        return NUMBER_OF_LIVES

    def GetGuessedLetters():
        return GUESSED_LETTERS

    def GetCurrentWord():
        return CURRENT_WORD

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Reads values from config
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def InitialiseGameData(newWord, initialNumberOfLives):

        # generate random word from available words
        global CURRENT_WORD
        CURRENT_WORD = newWord

        # get default initial number of lives
        global NUMBER_OF_LIVES
        NUMBER_OF_LIVES = initialNumberOfLives

        global GUESSED_LETTERS
        GUESSED_LETTERS = ''

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Verifies that letter is single abcABC character
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def IsValidCharacter(letter):
        pattern = re.compile("^[a-zA-Z0-9]{1}$")
        return pattern.match(letter)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Verifies that letter has not already been guessed
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def IsNewGuess(letter):
        return letter not in GUESSED_LETTERS

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Check guessed letters with word
    # Update score
    # Return score
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def DecreaseLives():
        global NUMBER_OF_LIVES
        NUMBER_OF_LIVES = NUMBER_OF_LIVES - 1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Save guessed letter
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def AddGuessedLetter(letter):
        global GUESSED_LETTERS
        GUESSED_LETTERS += letter