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
    # print the column header
    print('\n   ', end='')
    for column_header in range(MAXCOLUMNS):
        print(column_header % 10, end=' ')
    print()
    
    # print the row headers and the data next to each header
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

def count_booked_seats() -> int:
    count: int = 0
    for row in range(MAXROWS):
        for column in range(MAXCOLUMNS):
            if evening[row][column]:
                count = count + 1
            #endif
        #next col
    #next row
    return count
                
theatreLayout()
print( "Number of booked seats: ", count_booked_seats() )
