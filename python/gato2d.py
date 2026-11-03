##
# Simple tic tac toe game using a 2D array
##

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

# procedure to display the board nicely
def print_board():
    print("-------")
    for row in range(3):
        print("|", end="")
        for column in range(3):
            print(board[row][column], end="|")
        print("\n-------")
    
print_board()
col = 0
row = 0
# starting player
player_turn = "X"
game_won = False

# play until all 9 spaces are taken (tie) (or until there is a winner)
for counter in range(1, 10):
    # input check for valid move
    valid_move = False
    while (valid_move == False):
        col = 0
        row = 0
        while (row < 1 or row > 3):
            row = int(input(player_turn + " player, select a row 1-3: "))
            if (row < 1 or row > 3):
                print("The row must be between 1 and 3.")
        while (col < 1 or col > 3):
            col = int(input(player_turn + " player, select a column 1-3: "))
            if (col < 1 or col > 3):
                print("The column must be between 1 and 3.")
        # adjust for Python 2D array/list indices
        col -= 1
        row -= 1
        if board[row][col] == '-':
            board[row][col] = player_turn
            valid_move = True
        else:
            print("Oops, that spot was already taken. Please select another spot.")

    print_board()

    # Win detection logic
    has_won = False

    # Check rows and columns
    for i in range(3): # there are 3 rows and 3 columns
        # check if each row is taken by the player
        if board[i][0] == board[i][1] == board[i][2] == player_turn:
            has_won = True
        # check if each column is taken by the player
        if board[0][i] == board[1][i] == board[2][i] == player_turn:
            has_won = True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player_turn:
        has_won = True
    if board[0][2] == board[1][1] == board[2][0] == player_turn:
        has_won = True

    # End game if a win is detected
    if has_won:
        print("\nPlayer " + player_turn + " wins!")
        game_won = True
        break

    # Switch player turn
    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"

# Announce tie if all 9 turns complete without a winner
if not game_won:
    print("\nIt's a tie!")