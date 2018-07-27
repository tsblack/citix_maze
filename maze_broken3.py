#/bin/python

import sys

###
# Start in upper-left corner and walk the maze. This is a 
# brute-force approach and is too slow with larger mazes 
###
def maze_walk(maze, maze_dimension):
    startcolumn = 0
    success = False
    while startcolumn < maze_dimension - 1:
        column = startcolumn
        row = 0
        direction = "down"
        exit = False
        while not exit:
            # Finding a \ in maze position
            if maze[(maze_dimension * row) + column] == '1':
                if direction == "down":
                    column += 1
                    direction = "right"
                elif direction == "right":
                    row += 1
                    direction = "down"
                elif direction == "up":
                    column -= 1
                    direction = "left"
                else:
                    row -= 1
                    direction = "up"
            # Finding a \ in maze position
            else:
                if direction == "down":
                    column -= 1
                    direction = "left"
                elif direction == "right":
                    row -= 1
                    direction = "up"
                elif direction == "up":
                    column += 1
                    direction = "left"
                else:
                    row += 1
                    direction = "down"
            if row < 0:
                exit = True
                startcolumn += 1
            elif column not in range(0, maze_dimension):
                exit = True
                startcolumn += 1
            elif row == maze_dimension:
                exit = True
                success = True
    if success == True:
        return maze
    else:
        return false


###
# Set-up the total number of mazes and pass it to the
# brute-force maze walker 
###
def run_maze(maze_dimension):

    # Calculate some dimensions for limits in loops
    max_mazes = 2**(maze_dimension ** 2)

    # Initial line, fabricate tracker line
    for mazecount in range(0, max_mazes):
        result = maze_walk(format(mazecount, "0" + str(maze_dimension ** 2) + "b"), maze_dimension)
        if result != False:
            print(result)

###
# Main Handler, pass system parameters to execution
###
if __name__ == "__main_":
    if len(sys.argv) == 2:
        run_maze(int(sys.argv[1]))
    else:
        print("Please make sure you enter the correct arguments, arg1: dimension of maze.")
