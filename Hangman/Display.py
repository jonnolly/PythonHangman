import Reader
import Writer

import sys

NUMBER_OF_LIVES = None

# Set variables for a new game
def InitializeHangman():
    print("Welcome to hangman.")

    # generate random word from available words
    randomWord = Reader.GetRandomWord()
    
    # get initial number of lives
    global NUMBER_OF_LIVES
    NUMBER_OF_LIVES = Reader.GetConfigField("NUMBER_OF_LIVES")

    # save word to back-end
    Writer.SaveNewWord(randomWord)

# the primary function to call to play the game
def MainGameLoop():

    while(NUMBER_OF_LIVES > 0):
        guessedLetters = Reader.GetConfigField("GUESSED_LETTERS")

        print("LIVES: " + str(NUMBER_OF_LIVES) + "\tGuessed Letters: " + guessedLetters)

        # todo: add regex so only one abcABC letter is entered
        guessedLetter = input("Enter your letter: ")

        Writer.AddGuessedLetter(guessedLetter)
        Writer.UpdateScore()

        print("guessed letter" + guessedLetter + "\t")

InitializeHangman()
MainGameLoop()