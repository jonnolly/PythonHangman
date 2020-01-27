import ConfigReader
import re
import json

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
def InitialiseGame():

    # generate random word from available words
    global CURRENT_WORD
    CURRENT_WORD = ConfigReader.GetRandomWord()

    # get default initial number of lives
    global NUMBER_OF_LIVES
    NUMBER_OF_LIVES = ConfigReader.GetConfigField('INITIAL_NUMBER_OF_LIVES')

    global GUESSED_LETTERS
    GUESSED_LETTERS = ''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# verifies that letter is single abcABC character
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def IsValidCharacter(letter):
    pattern = re.compile("^[a-zA-Z0-9]{1}$")
    return pattern.match(letter)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# verifies that letter has not already been guessed
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def IsNewGuess(letter):
    return letter not in GUESSED_LETTERS

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# check guessed letters with word
# update score
# return score
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def DecreaseLives():
    global NUMBER_OF_LIVES
    NUMBER_OF_LIVES = NUMBER_OF_LIVES - 1

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# save guessed letter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def AddGuessedLetter(letter):
    global GUESSED_LETTERS
    GUESSED_LETTERS += letter