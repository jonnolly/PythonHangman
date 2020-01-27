# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main game loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import GameData
from Display import Display

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Request user to play again. 
# Return True/False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def playAgain(isPlayAgain):
    if(isPlayAgain):
        GameData.InitialiseGame()
        return MainGameLoop()
    else:
        exit()

# the primary function to call to play the game
def MainGameLoop():
    while(True):
        numberOfLives = GameData.GetNumberOfLives()
        guessedLetters = GameData.GetGuessedLetters()
        currentWord = GameData.GetCurrentWord()
        
        if numberOfLives == 0:
            return playAgain(Display.DisplayGameOverScreen())

        # get masked word to be displayed on the screen
        displayedWord = Display.MaskWord(currentWord, guessedLetters)

        # has the word been completely uncovered?
        if displayedWord.count('_') is 0:
            return playAgain(Display.DisplaySuccessScreen())

        # print new updated screen
        Display.DisplayGameScreen(numberOfLives, guessedLetters, displayedWord)

        # ask for letter guess from user
        guessedLetter = Display.RequestLetter(guessedLetters)

        # check if letter is correct
        if(guessedLetter not in currentWord):
            GameData.DecreaseLives()
        
        # add to guesses
        GameData.AddGuessedLetter(guessedLetter)

print("Welcome to hangman.")
GameData.InitialiseGame()
MainGameLoop()