import random

rps = ["Rock", "Paper", "Scissor"]
opp = random.choice(rps).lower()

def main():
    choice = input("Enter your choice: ").lower()
    if tie(choice, opp):
        print("Its a Tie!")
    elif win(choice, opp):
        print("You Won!")
    else:
        print("LOL, YOU LOSE!")

def tie(x, y):
    return x==y
    
def win(x, y):
    if (x == "rock" and y == "scissors") or (x == "scissors" and y == "paper") or (x == "paper" and y == "rock"):
        return True

if __name__ == "__main__":
    main()