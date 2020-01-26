import json

def SetConfigField(fieldName, fieldValue, isAppended = False):
    
    # todo: add exception handling
    # Create file and field if not available 
    with open('./config.json', 'r+') as json_file:
        data = json.load(json_file)

        if(isAppended): data[fieldName] += fieldValue
        else: data[fieldName] = fieldValue
        
        json_file.seek(0)        # reset file position to the beginning.
        json.dump(data, json_file)
        json_file.truncate()     # remove remaining part

# Save new word to back-end
def SaveNewWord(word):
    # write word into config
    print("writing new word: " + word)
    SetConfigField('CURRENT_WORD', list(word))

# check guessed letters with word
# update score
# return score
def UpdateScore():
    return 0

# save guessed letter
def AddGuessedLetter(letter):

    SetConfigField("GUESSED_LETTERS", letter, True)