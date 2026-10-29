##
# Simple tic tac toe game using a 2D array
##

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

print(board[0])
print(board[1])
print(board[2])

col = 0
row = 0
# starting player
playerTurn = "X"
game_won = False

# play until all 9 spaces are taken (tie) (or until there is a winner)
for counter in range(1, 10):
    # input check for valid move
    validMove = False
    while (validMove == False):
        col = 0
        row = 0
        while (row < 1 or row > 3):
            row = int(input(playerTurn + " player, select a row 1-3: "))
            if (row < 1 or row > 3):
                print("The row must be between 1 and 3.")
        while (col < 1 or col > 3):
            col = int(input(playerTurn + " player, select a column 1-3: "))
            if (col < 1 or col > 3):
                print("The column must be between 1 and 3.")
        # adjust for Python 2D array/list indices
        col -= 1
        row -= 1
        if board[row][col] == '-':
            board[row][col] = playerTurn
            validMove = True
        else:
            print("Oops, that spot was already taken. Please select another spot.")

    print(board[0])
    print(board[1])
    print(board[2])

    # Win detection logic
    has_won = False

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == playerTurn:
            has_won = True
        if board[0][i] == board[1][i] == board[2][i] == playerTurn:
            has_won = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == playerTurn:
        has_won = True
    if board[0][2] == board[1][1] == board[2][0] == playerTurn:
        has_won = True

    # End game if a win is detected
    if has_won:
        print("\nPlayer " + playerTurn + " wins!")
        game_won = True
        break

    # Switch player turn
    if playerTurn == "X":
        playerTurn = "O"
    else:
        playerTurn = "X"

# Announce tie if all 9 turns complete without a winner
if not game_won:
    print("\nIt's a tie!")