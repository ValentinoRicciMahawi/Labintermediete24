def updateText(secretWord, guessedLetter):
    guessedWord = ""
    for i in range(len(secretWord)):
        for j in range(len(guessedLetter)):
            if secretWord[i] == guessedLetter[j]: #kalo ketemu
                if j == len(guessedLetter) - 1:
                    print("Congrats, '", guessedLetter[j], "' is in the secret word!")
                guessedWord = guessedWord + secretWord[i]
                break
            elif j == len(guessedLetter) - 1: #kalo ga ketemu di ujung list guessedLetter
                guessedWord = guessedWord + '_'
        guessedWord = guessedWord + ' '
    return guessedWord

def main(secretWord):
    life = 6
    secretWord = secretWord.lower()
    guessedLetter = []
    while life > 0:
        print("Guesses:", life)
        letter = input("Guess a letter: ").lower()
        if len(letter) > 1:
            print("Letter can't be more than 1!")
        elif letter.isnumeric():
            print("Don't input number!")
        else:
            if letter in guessedLetter:
                print("Letter is already guessed!")
            else:
                guessedLetter.append(letter)
                guessedWord = updateText(secretWord, guessedLetter)
                
                print(guessedWord)

                for i in range(len(guessedWord)):
                    if guessedWord[i] == '_':
                        break
                    elif i == len(guessedWord) - 1:
                        print("Congratulations! You won!")
                        return

                life = life - 1
    print("You run out of guesses!")


main("kevin")
