import GameData
import re
import sys

# Set variables for a new game
def InitializeHangman():
    print("Welcome to hangman.")
    GameData.InitialiseGame()

# display primary hangman screen
def displayGameScreen(numberOfLives, guessedLetters, maskedWord):
    print("\n\n\n\nLIVES: " + str(numberOfLives) + "\tGuessed Letters: " + guessedLetters + '\n\n\t' + maskedWord)

# display generic play again y/n selection screen
def playAgainScreen(userPrompt):
    playAgain = input(userPrompt)
    test = playAgain.lower()
    if(playAgain.lower() == 'y'):
        GameData.InitialiseGame()
        return MainGameLoop()
    elif(playAgain.lower() == 'n'):
        exit()
    else:
        return playAgainScreen(userPrompt)

# display game over screen
def displayGameOverScreen():
    playAgainScreen('GAME OVER! Play again? y/n')
    
# display success screen
def displaySuccessScreen():
    playAgainScreen('SUCCESS! Play again? y/n')

def requestLetter(previouslyGuessedLetters, requestString = "Enter your letter: "):

    # ask the user 'requestString' and retrieve letter
    guessedLetter = input(requestString)

    # if input still not valid, call function again
    if(not GameData.IsValidCharacter(guessedLetter)):
        return requestLetter(previouslyGuessedLetters, "Please enter a valid single character from a-z: ")
    elif(not GameData.IsNewGuess(guessedLetter)):
        return requestLetter(previouslyGuessedLetters, "Please enter a character you have not already guessed: ")
    else:
        return guessedLetter

def maskWord(word, guessedLetters):
    letterList = list(word)
    guessedLetterList = list(guessedLetters)
    maskedWord = ''

    for letter in letterList:
        if guessedLetterList.count(letter) is 0:
            maskedWord += '_'
        else:
            maskedWord += letter

    return maskedWord

# the primary function to call to play the game
def MainGameLoop():
    while(True):
        numberOfLives = GameData.GetNumberOfLives()
        guessedLetters = GameData.GetGuessedLetters()
        currentWord = GameData.GetCurrentWord()
        
        if numberOfLives == 0:
            return displayGameOverScreen()

        # get masked word to be displayed on the screen
        displayedWord = maskWord(currentWord, guessedLetters)

        if displayedWord.count('_') is 0:
            return displaySuccessScreen()

        # print new updated screen
        displayGameScreen(numberOfLives, guessedLetters, displayedWord)

        # ask for letter guess from user
        guessedLetter = requestLetter(guessedLetters)

        # check if letter is correct
        if(guessedLetter not in currentWord):
            GameData.DecreaseLives()
        
        # add to guesses
        GameData.AddGuessedLetter(guessedLetter)

InitializeHangman()
MainGameLoop()