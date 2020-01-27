# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main game loop
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from GameData import GameData
from ConfigReader import ConfigReader
from Display import Display

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Initialize all data for a new game of Hangman
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setupNewGame():
    print(ConfigReader.GetHangmanLogo())
    newWord = ConfigReader.GetRandomWord()
    initialNumberOfLives = ConfigReader.GetConfigField('INITIAL_NUMBER_OF_LIVES')
    GameData.InitialiseGameData(newWord, initialNumberOfLives)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Request user to play again. 
# Return True/False
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def playAgain(isPlayAgain):
    if(isPlayAgain):
        setupNewGame()
        return MainGameLoop()
    else:
        exit()

# the primary function to call to play the game
def MainGameLoop():
    while(True):
        numberOfLives = GameData.GetNumberOfLives()
        guessedLetters = GameData.GetGuessedLetters()
        currentWord = GameData.GetCurrentWord()

        # get masked word to be displayed on the screen
        displayedWord = Display.MaskWord(currentWord, guessedLetters)

        # print new updated screen
        Display.DisplayGameScreen(ConfigReader.GetHangmanLogo(), ConfigReader.GetHangmanStageIcon(numberOfLives), numberOfLives, guessedLetters, displayedWord)
        
        # check if game over
        if numberOfLives == 0:
            gameOverLogo = ConfigReader.GetGameOverIcon()
            return playAgain(Display.DisplayGameOverScreen(gameOverLogo))

        # check if success
        if displayedWord.count('_') is 0:
            successLogo = ConfigReader.GetSuccessIcon()
            return playAgain(Display.DisplaySuccessScreen(successLogo))

        # ask for letter guess from user
        guessedLetter = Display.RequestLetter(guessedLetters)

        # check if letter is correct
        if(guessedLetter not in currentWord):
            GameData.DecreaseLives()
        
        # add to guesses
        GameData.AddGuessedLetter(guessedLetter)

setupNewGame()

# Start Game
MainGameLoop()