import os


def main():
    board = [' '] * 10
    initBoard(board)
    playing = 'X'

    for turn in range(9):
        os.system('clear')
        printBoard(board)
        while True:
            player = int(input((f"Player: {playing}, enter your choice: ")))

            if board[player] == 'X' or board[player] == 'O':
                print(f"{player} is invalid. Try again.\n")
            else:
                break

        board[player] = playing

        if checkWin(board, playing):
            os.system('clear')
            printBoard(board)
            print(f"Player {playing} won!")
            return

        playing = 'O' if playing == 'X' else 'X'

        printBoard(board)

    print("It's a tie!\n")


def checkWin(board, playing):
    for i in range(7, 0, -3):
        if board[i] == playing and board[i+1] == playing and board[i+2] == playing:
            return True

    for i in range(1, 4):
        if board[i] == playing and board[i+3] == playing and board[i+6] == playing:
            return True

    if (board[7] == playing and board[5] == playing and board[3] == playing) or (board[1] == playing and board[5] == playing and board[9] == playing):
        return True

    return False


def initBoard(board):
    for i in range(9, 0, -1):
        board[i] = str(i)


def printBoard(board):
    for i in range(7, 0, -3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i > 1:
            print("---+---+---")


if __name__ == "__main__":
    main()
