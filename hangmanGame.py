import random
import os


def displayHints(hint):
    print(" ".join(hint))


categories = {
    "Body Part": ["ARM", "LEG", "FACE", "NOSE", "MOUTH", "HAND", "FOOT", "EYE", "EAR", "BACK"],
    "Animal": ["PIG", "DOG", "ZEBRA", "BEAR", "CAT", "ELEPHANT", "TIGER", "LION", "WHALE", "DOLPHIN", "FOX", "EAGLE", "RABBIT", "KANGAROO"],
    "Car Brand": ["BMW", "KIA", "FORD", "HONDA", "MAZDA", "TOYOTA", "TESLA", "MERCEDES", "AUDI", "CHEVROLET", "NISSAN", "VOLKSWAGEN"],
    "Fruit": ["APPLE", "BANANA", "ORANGE", "GRAPE", "MANGO", "PEACH", "CHERRY", "STRAWBERRY", "PINEAPPLE", "WATERMELON", "KIWI", "BLUEBERRY"],
    "Country": ["USA", "CANADA", "MEXICO", "JAPAN", "FRANCE", "GERMANY", "AUSTRALIA", "CHINA", "INDIA", "BRAZIL", "SPAIN", "ITALY", "RUSSIA", "EGYPT"],
    "Color": ["RED", "BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE", "BLACK", "WHITE", "PINK", "GRAY", "BROWN", "VIOLET", "INDIGO"],
    "Sports": ["SOCCER", "BASKETBALL", "BASEBALL", "TENNIS", "SWIMMING", "CYCLING", "VOLLEYBALL", "CRICKET", "SKATEBOARDING", "HOCKEY", "GOLF"],
    "Movie Genre": ["ACTION", "COMEDY", "DRAMA", "THRILLER", "HORROR", "ROMANCE", "DOCUMENTARY", "ANIMATION", "FANTASY", "MYSTERY"],
    "Occupation": ["DOCTOR", "ENGINEER", "TEACHER", "LAWYER", "NURSE", "SCIENTIST", "ARTIST", "ACTOR", "POLICE", "CHEF", "WRITER", "MUSICIAN"]
}


HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  󰚌   |
 /|\\  |
 / \\  |
      |
=========''']


def main():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    hint = ["_"] * len(word)
    turns = 0
    guessedLetters = set()
    isRunning = True

    print("H A N G M A N")

    while isRunning:
        os.system("clear")
        print("======================")
        print("Category: ", category)
        print("======================")
        print(HANGMANPICS[turns])
        displayHints(hint)
        guess = input("Enter a letter: ").capitalize()

        if len(guess) != 1 or not guess.isalpha():
            print(" Invalid Input! ")
            input("Please Enter to Continue...")
            continue

        if guess in guessedLetters:
            print(" You already inputed that ")
            input("Please Enter to Continue...")
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hint[i] = guess
            guessedLetters.add(guess)
        else:
            print(" Incorrect! ")
            turns += 1
            guessedLetters.add(guess)
            input("Please Enter to Continue...")

        if "_" not in hint:
            displayHints(hint)
            print(" You Win! ")
            isRunning = False
        elif turns >= len(HANGMANPICS) - 1:
            os.system("clear")
            print(HANGMANPICS[turns])
            print("󰚌 No Turns Left, You Lose! 󰚌")
            print(word)
            isRunning = False


if __name__ == "__main__":
    main()
