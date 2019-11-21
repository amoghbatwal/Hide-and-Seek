# hide.py : a simple friend-hider
#
# Submitted by : Amogh Batwal
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state along with condition checking
def successors(board):
    return [ add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if board[r][c] == '.' and conditionchecking(r, c, board)]

# Checking for all conditions required to place a friend
def conditionchecking(r, c, board):
    row_val = False
    col_val = False
    row_condition_1 = False
    row_condition_2 = False
    col_condition_1 = False
    col_condition_2 = False
    
    # Row validation - Checking if F can be placed in the row
    F_found = False
    element = c
    # Checking if the rth row contains 'F' & '&' after current position
    while(element < len(board[r])-1):
        element+=1
        if board[r][element] == 'F':   # Check if Friend is present in the row after my current position
            F_found = True
            position_x, position_y = r, element
            #Check if there is & between current position and F's posiiton i.e. r, element
            for x in range(c,position_y): # Current position to F's position
                if (board[r][x] == '&' or board[r][x] == '@'):   # Check if & or @ is present in the places b/w current position and F found
                    row_condition_1 = True   # If yes, return row condition-1 flag true
                    break
            break
            
    if(element == len(board[r])-1 and not row_condition_1 and not F_found):
        row_condition_1 = True
        
    # Checking if the rth row contains 'F' & '&' before current position
    F_found = False
    element  = c
    while( element > 0):
        element -= 1
        if board[r][element] == 'F':   # Check if Friend is present in the row before my current position
            F_found = True
            # Check if there is & between current position and F's posiiton
            for z in range(element, c):
                if (board[r][z] == '&' or board[r][z] == '@'):   # Check if & or @ is present in the places b/w current position and F found, in reverse order
                    row_condition_2 = True   # If yes, return row condition-2 flag true
                    break
            break
    
    if(element == 0 and not row_condition_2 and not F_found):  
        row_condition_2 = True
            
    if row_condition_1 and row_condition_2:
        row_val = True
        
        
    # Column validation - Checking if F can be placed in the column
    element = r
    F_found = False
    # Checking if the cth row contains 'F' after current position
    while(element < len(board)-1):
        element+=1
        if board[element][c] == 'F':   # Check if Friend is present in the column after my current position
            F_found = True
            position_x, position_y = element, c
            # Check if there is & between r,c and F's posiiton i.e. element,c
            for x in range(r, position_x): 
                if (board[r][c] == '&' or board[r][c] == '@'):  # Check if there is & or @ between current position and F found
                    col_condition_1 = True
                    break
            break
     
    if(element == len(board)-1 and not col_condition_1 and not F_found):
        col_condition_1 = True               
    
    # Checking if the cth row contains 'F' before current position
    F_found = False
    element = r
    while(element > 0):
        element -= 1
        if board[element][c] == 'F':   # Check if Friend is present in the column before my current position
            F_found = True
            for z in range(element, r):
                if (board[z][c] == '&' or board[z][c] == '@'):   # Check if there is & or @ between current position and F found, in reverse order
                    col_condition_2 = True
                    break
            break
 
    if(element == 0 and not col_condition_2 and not F_found):
        col_condition_2 = True 
               
    if col_condition_1 and col_condition_2:
        col_val = True
    
    if row_val and col_val:
        return True # If 'F' is not present in both row and column, returning a valid position to put 'F'
    else:
        return False
    
# Check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

# Solve n-rooks!
def solve(initial_board):
    visited = []
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors( fringe.pop() ):
            if s in visited:
                continue
            visited.append(s)
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])
    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    if K == 0:   # If no friends are to be placed, return the original map
        print (printable_board(IUB_map))
    else:      
        solution = solve(IUB_map)
        print ("Here's what we found:")
        print (printable_board(solution) if solution else "None")   # If solution is found - return the board , else return with No solution  
