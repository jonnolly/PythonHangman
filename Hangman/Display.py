# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class responsible for the display
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from GameData import GameData
import re
import sys

class Display:

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Display primary hangman screen
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def DisplayGameScreen(mainLogo, stageLogo, numberOfLives, guessedLetters, maskedWord):
        print('\n' * 40)
        print(mainLogo)
        print(stageLogo)
        print("\n\nLIVES: " + str(numberOfLives) + "\tGuessed Letters: " + guessedLetters + '\n\n\t' + maskedWord)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Display generic play again y/n selection screen
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def PlayAgainScreen(userPrompt):
        playAgain = input(userPrompt)
        if(playAgain.lower() == 'y'):
            return True
        elif(playAgain.lower() == 'n'):
            return False
        else:
            return Display.PlayAgainScreen(userPrompt)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Display game over screen
    # Returns a bool corresponding to 'play again'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def DisplayGameOverScreen(gameOverLogo):
        return Display.PlayAgainScreen(gameOverLogo + '\n\n Play again? y/n')
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Display success screen
    # Returns a bool corresponding to 'play again'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def DisplaySuccessScreen(successLogo):
        return Display.PlayAgainScreen(successLogo + '\n\n Play again? y/n')

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Ask the user for their guessed letter
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def RequestLetter(previouslyGuessedLetters, requestString = "Enter your letter: "):

        # ask the user 'requestString' and retrieve letter
        guessedLetter = input(requestString)

        # if input still not valid, call function again
        if(not GameData.IsValidCharacter(guessedLetter)):
            return Display.RequestLetter(previouslyGuessedLetters, "Please enter a valid single character from a-z: ")
        elif(not GameData.IsNewGuess(guessedLetter)):
            return Display.RequestLetter(previouslyGuessedLetters, "Please enter a character you have not already guessed: ")
        else:
            return guessedLetter

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Return covered word to be displayed to user
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def MaskWord(word, guessedLetters):
        letterList = list(word)
        guessedLetterList = list(guessedLetters)
        maskedWord = ''

        for letter in letterList:
            if guessedLetterList.count(letter) is 0:
                maskedWord += '_'
            else:
                maskedWord += letter

        return maskedWord