import sys

filename = sys.argv[1]

def solver(grid):

    empty = empty_square(grid)

    if empty == None:
        return True

    for i in range(1,10):
        if valid_input(grid, i, empty):
            grid[empty[0]][empty[1]] = i

            if solver(grid):
                return True
            grid[empty[0]][empty[1]] = 0
        
    return False


def valid_input(grid, number, position):
    """Given a grid, a number and its position check if it is valid"""

    # check the row
    for i in range(len(grid[position[0]])):
        if grid[position[0]][i] == number and i != position[1]:
            return False

    # check the column
    for j in range(len(grid)):
        if grid[j][position[1]] == number and j != position[0]:
            return False

    # check the 3x3 box
    x_box = position[1] // 3
    y_box = position[0] // 3

    for j in range(3*y_box, (3*y_box)+3): 
        for i in range(3*x_box, (3*x_box)+3):
            if grid[j][i] == number and (j, i) != position:
                return False

    return True    
        

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
                # (x,y) = (row, column)
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

def main(filename):

    grid = get_grid(filename)
    print_board(grid)
    solver(grid)
    print_board(grid)

main(filename)