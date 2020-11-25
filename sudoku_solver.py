filename = "test_sudoku_1.txt"

def valid_input(grid, number, position):
    """Given a grid, a number and its position check if it is valid"""

    # check the row

    # check the column

    # check the 3x3 box

def get_grid(filename):
    """Convert the grid from the txt file in a list of lists"""

    # get txt file
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    # define empty grid
    grid = []

    # loop through the txt file and add to grid
    for rows in lines:
        row = []
        for number in rows:
            row.append(int(number))
        grid.append(row)
    
    # make sure the grid is valid
    for i in range(len(grid)):
        if len(grid) != 9 or len(grid[i]) != 9:
            print("Invalid grid")
            return None

    return grid

def empty_square(grid):
    """Given a grid, this function returns a tuple of an empty square"""

    # check every element for a row if equals 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:

                # i is the row and j is the column
                return (i,j)

    return None

def print_board(grid):
    """Given a grid in list format, print the sudoku board"""

    for i in range(len(grid)):
        print('')
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(grid[i])):
            if j % 3 == 0 and j != 0:
                print("|", end = ' ')
            print(grid[i][j], end = ' ')
    print('\n')


            

