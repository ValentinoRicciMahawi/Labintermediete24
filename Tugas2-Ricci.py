def hangman(word):
    life = 6
    word = word.lower()
    guessedLetter = []
    while life > 0:
        print("Guesses:", life)
        letter = input("Guess a letter: ").lower()
        if len(letter) > 1:
            print("Letter can't be more than 1!")
        else:
            if letter in guessedLetter:
                print("Letter is already guessed!")
            else:
                guessedLetter.append(letter)
                guessedWord = ""
                for i in range(len(word)):
                    for j in range(len(guessedLetter)):
                        if word[i] == guessedLetter[j]: #kalo ketemu
                            guessedWord = guessedWord + word[i]
                            break
                        elif j == len(guessedLetter) - 1: #kalo ga ketemu di ujung list guessedLetter
                            guessedWord = guessedWord + '_'
                    guessedWord = guessedWord + ' '
                print(guessedWord)

                for i in range(len(guessedWord)):
                    if guessedWord[i] == '_':
                        break
                    elif i == len(guessedWord) - 1:
                        print("Congratulations! You won!")
                        return

                life = life - 1
    print("You run out of guesses!")


hangman("Ricci")
