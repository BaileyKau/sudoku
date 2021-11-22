from sudoku_app.config.mysqlconnection import connectToMySQL

class Board:
    def __init__ (self, data):
        self.id = data['id']
        self.board = data['board']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_board(cls):
        query = "SELECT board FROM boards"
        result = connectToMySQL('sudoku_schema').query_db(query)
        result = result[0]['board']
        arr = []
        for i in range(9):
            col = []
            for j in range(9):
                num = int(result[i*9+j])
                col.append(num)
            arr.append(col)
        return arr
    
    @classmethod 
    def solve_board(cls):
        board = Board.get_board()
        solutions = []
        # Find Empty
        def find_empty(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if (board[i][j]) == 0:
                        return (i, j)
            return None
        # Validate 
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
        # Solve
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
        
        solve(board)
        return board
        


    # def validate_board
    # def new_board