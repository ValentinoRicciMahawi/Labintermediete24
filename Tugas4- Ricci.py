import random
secret_word_list = ["ayam", "sapi", "bebek", "buaya", "ikan"]

used_word = []
score = 0
win = 0
lose = 0

def pickSecretWord(secret_word_list):
    length = len(secret_word_list)
    if length == len(used_word):
        return "win"
    while True:
        index = random.randint(1,length)
        if index not in used_word:
            break
    secret_word = secret_word_list[index-1]
    used_word.append(index)
    return secret_word

def updateText(secretWord, guessedLetter):
    guessedWord = ""
    flag = 0
    for i in range(len(secretWord)):
        for j in range(len(guessedLetter)):
            if secretWord[i] == guessedLetter[j]: #kalo ketemu
                if j == len(guessedLetter) - 1 and flag == 0:
                    print("Congrats, '", guessedLetter[j], "' is in the secret word!")
                    flag = 1
                guessedWord = guessedWord + secretWord[i]
                break
            elif j == len(guessedLetter) - 1: #kalo ga ketemu di ujung list guessedLetter
                guessedWord = guessedWord + '_'
        guessedWord = guessedWord + ' '
    return guessedWord

def playAgain():
    print(f"Score: {score}, Win: {win}, Lose: {lose}")
    again = input("Play again? (yes/no): ").lower()
    if again == "yes":
        main(pickSecretWord(secret_word_list))
    elif again == "no":
        print("Thank you for playing! Final score :", score)
        return True
    else:
        print("Invalid input!")
        playAgain()
    return False

def main(secretWord):
    global score, win, lose
    if secretWord == "win":
        print("There are no words left! Final score:", score)
        return
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
                        score = score + 100
                        win = win + 1
                        print("Score: ", score)
                        if playAgain():
                            return
                life = life - 1
    print("You run out of guesses!")
    score = score - 50
    lose = lose + 1
    if playAgain():
        return

main(pickSecretWord(secret_word_list))