##########################################################################
# Write a program that meets the following requirements:
### counts and outputs the number of seats already booked for the evening
### allows the user to input the number of seats required
### validates the input
### checks if enough seats are available:
###### if they are available
######### changes the status of the seats
######### outputs the row number and seat number for each seat booked
###### if they are not available:
######### outputs a message giving the number of seats left or
######### "House full" if the theatre is fully booked.
##########################################################################

# Booking problem given 2D array data
evening = [ [True, True, True, False, True, False, False, False, True, True, True, False, False, False, False, True, False, False, False, True],
            [True, True, False, False, False, False, True, False, True, True, True, False, True, True, True, True, False, False, False, True],
            [True, False, True, True, False, True, False, False, False, False, False, True, False, False, True, False, False, True, True, False],
            [False, False, False, True, True, False, True, False, True, True, True, True, False, True, False, False, True, True, True, True],
            [False, True, False, True, False, False, False, True, True, False, False, True, False, False, True, False, False, False, True, False],
            [True, True, True, False, True, True, False, False, False, True, True, False, False, False, False, False, False, True, False, True],
            [True, False, False, True, True, False, False, False, True, True, True, True, False, True, False, True, True, True, True, False],
            [True, False, True, True, True, True, False, True, True, True, False, True, True, False, True, False, False, False, False, False],
            [False, False, True, False, False, False, True, True, False, True, True, True, True, True, True, True, False, False, False, False],
            [True, True, False, True, False, True, False, True, False, True, True, True, False, False, False, True, True, False, True, False] ]

MAXROWS:int = len(evening)            # or, 10
MAXCOLUMNS:int = len(evening[0])      # or, 20
FULLHOUSE: int = MAXROWS * MAXCOLUMNS # or = 200

def theatreLayout():
    # easiest way to print the column header
    print('\n   1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0\n')
    for row in range(MAXROWS):
        print( (row+1) % 10, end='  ')
        for column in range(MAXCOLUMNS):
            if evening[row][column]:
                print('B', end=' ')
            else:
                print('A', end=' ')
            # endif
        # next column
        print() # go to next row
    # next row
    print('\nB = Booked; A = Available')

