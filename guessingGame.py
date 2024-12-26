import random
randNumber = random.randint(1, 10)
turns = 3

while turns != 0:
    guess = int(input("Guess the number from 1 - 10: "))
    
    if guess == randNumber:
        print("You Win!")
        break
    elif guess < randNumber:
        print("Wrong! Guess higher!")
        turns -= 1
    elif guess < randNumber:
        print("Wrong! Guess lower!")
        turns -= 1

if turns == 0:
    print("No turns left, You Lose!")