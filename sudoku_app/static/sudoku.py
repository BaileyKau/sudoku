board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for i in range (len(board)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - ")
        for j in range (len(board[0])):
            if j % 3 == 0 and j != 0:
                print (" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j]) == 0:
                return (i, j)  #i is row, j is column
    return None

def validate(board, num, pos):
    #Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    # We know if they are no more empty spaces, we finished the sudoku (Base Case)
    empty = find_empty(board)
    if not empty:
        return True
    else:
        row, col = empty
    
    for i in range (1, 10):
        #Try numbers 0-9 for each position
        if validate(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


# print("Initial Board:")
# print_board(board)
# print("Solving ...")
solve(board)
print("Solved!")
print_board(board)
# print("-------------------------------------------------")

result = "780400120600075009000601078007040260001050930904060005070300012120007400049206007"
def help(result):
    arr = []
    for i in range(9):
        col = []
        for j in range(9):
            col.append(result[i*9+j])
        arr.append(col)
    return arr
# print_board(help(result))