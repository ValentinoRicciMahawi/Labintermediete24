secret_word = "logic"
letter = ["_"] * 5

print ("Selamat adatang di permainan Hangman")
print (f"Kata tersebut mengandung {len(secret_word)} huruf")

while "_" in letter:
    guess = input("Input a letter: ")
    if guess in secret_word:
        print ("Betul!")
        for i in range(5):
            if secret_word[i] == guess:
                letter[i] = guess
    else:
        print ("Salah!")
    print (" ".join(letter))
    if "_" not in letter:
        print("Selamat!")