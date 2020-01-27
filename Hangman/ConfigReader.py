from random import seed
from random import random
from random import randint
import json

# Retrieve storage data with name fieldName
def GetConfigField(fieldName):
    try:
        with open('./config.json', 'r+') as json_file:
            data = json.load(json_file)
            return data[fieldName]
    except:
        return ''

# Search available words in storage and select one out of random
def GetRandomWord():
    availableWords = GetConfigField('WORDS')
    randomWordIndex = randint(0, len(availableWords) - 1)
    return availableWords[randomWordIndex]