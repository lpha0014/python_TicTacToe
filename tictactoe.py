def display(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print('-----')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-----')
    print(board[6] + "|" + board[7] + "|" + board[8])

def userinput():
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    winner = ""
    while len(options) != 0:
        moveX = int(input('Player X: Enter position number: '))
        if moveX in options:
            inputX(moveX, board)
            del options[options.index(moveX)]
            print(options)
        else:
            print("ERROR, Please enter a number that hasn't been already used on your next turn")

        # check for winner
        wincheck()
        if winner == "Y" or winner == "X":
            exit()

        moveO = int(input('Player Y: Enter position number: '))
        if moveO in options:
            inputO(moveO, board)
            del options[options.index(moveO)]
            print(options)
        else:
            print("ERROR, Please enter a number that hasn't been already used on your next turn")

        wincheck()
        if winner == "Y" or winner == "X":
            break

    else:
        print("Game is finished! It was a tie!")


def inputX(moveX, board):
    player = "X"
    updateBoard = replace(moveX, board, player)
    display(updateBoard)


def inputO(moveO, board):
    player = "O"
    updateBoard = replace(moveO, board, player)
    display(updateBoard)


def replace(index, board, player):
    if player == "X":
        board[index] = "X"
    elif player == "O":
        board[index] = "O"
    else:
        print('Input did not register')
    return board


# function for checking the winning combinations
def wincheck():
    if ((board[0] == "X" and board[4] == "X" and board[8] == "X") or
            (board[2] == "X" and board[4] == "X" and board[8] == "X") or
            (board[0] == "X" and board[1] == "X" and board[2] == "X") or
            (board[0] == "X" and board[3] == "X" and board[6] == "X") or
            (board[2] == "X" and board[5] == "X" and board[8] == "X") or
            (board[3] == "X" and board[4] == "X" and board[5] == "X") or
            (board[1] == "X" and board[4] == "X" and board[7] == "X") or
            (board[6] == "X" and board[7] == "X" and board[8] == "X")):
        print("X has won the game!")
        winner = "X"
    elif ((board[0] == "O" and board[4] == " O" and board[8] == "O") or
          (board[2] == "O" and board[4] == "O" and board[8] == "O") or
          (board[0] == "0" and board[1] == "0" and board[2] == "O") or
          (board[0] == "0" and board[3] == "0" and board[6] == "0") or
          (board[2] == "0" and board[5] == "0" and board[8] == "0") or
          (board[3] == "O" and board[4] == "O" and board[5] == "O") or
          (board[1] == "O" and board[4] == "O" and board[7] == "O") or
          (board[6] == "0" and board[7] == "0" and board[8] == "0")):
        print("O has won the game!")
        winner = "Y"
    else:
        winner = ""
    return winner


# main execution steps:
print("Welcome to the game of Tic Tac Toe!! Enter numbers 0-8 to place your X or O. The layout is:")
print("0" + "|" + "1" + "|" + "2")
print('-----')
print("3" + "|" + "4" + "|" + "5")
print('-----')
print("6" + "|" + "7" + "|" + "8")
print('-----Lets start!!!-----')
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
userinput()
