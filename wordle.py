import pathlib
import random

def getRandomWord ():
    wordlist = pathlib.Path("wordlist.txt").read_text(encoding = "utf-8")
    words = wordlist.split("\n")
    word = random.choice(words)
    return word

def showGuess(guess, word):
    correctLetters = {
    letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplacedLetters = set(guess) & set(word) - correctLetters
    wrongLetters = set(guess) - set(word) 
    print ("Correct letters: ", ",".join(sorted(correctLetters)))
    print ("Misplaced letters: ",",".join(sorted(misplacedLetters)))
    print ("Wrong letters: ",",".join(sorted(wrongLetters)))

def gameOver(word):
    print (f"The correct word is: {word}")

def main():
    word = getRandomWord ()
    for i in range(1, 7):
        guess = input (f"\nGuess {i}:").lower()
        showGuess(guess,word)
        if guess == word:
            print ("correct")
            break

    else:
        gameOver()
if __name__ == "__main__":
    main()
        