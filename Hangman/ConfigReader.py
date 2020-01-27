# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class responsible for reading config
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from random import randint
import json

class ConfigReader:

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Retrieve storage data with name fieldName
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetConfigField(fieldName):
        try:
            with open('./config.json', 'r+') as json_file:
                data = json.load(json_file)
                return data[fieldName]
        except:
            return ''

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Search available words in storage and select one out of random
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetRandomWord():
        availableWords = ConfigReader.GetConfigField('WORDS')
        randomWordIndex = randint(0, len(availableWords) - 1)
        return availableWords[randomWordIndex]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get Hangman logo
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetHangmanLogo():
        logoFile = ConfigReader.GetConfigField('HANGMAN_LOGO_FILE')
        f = open(logoFile, "r")
        return f.read()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get Hangman stage icon
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetHangmanStageIcon(stageNumber):
        iconsDirectory = ConfigReader.GetConfigField('HANGMAN_ICONS_DIRECTORY')
        f = open(iconsDirectory + '/' + str(stageNumber) + '.txt', "r")
        return f.read()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get GAMEOVER icon
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetGameOverIcon():
        logoFile = ConfigReader.GetConfigField('GAMEOVER_LOGO_FILE')
        f = open(logoFile, "r")
        return f.read()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Get SUCCESS icon
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def GetSuccessIcon():
        logoFile = ConfigReader.GetConfigField('SUCCESS_LOGO_FILE')
        f = open(logoFile, "r")
        return f.read()