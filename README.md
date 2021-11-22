# Sudoku Shinobi
#### Video Demo: https://youtu.be/SgkEdyUBVjE
## Description:
#### Application Uses: Sudoku Shinobi uses a backtracking algorithm to solve any sudoku put into the connected MySQL Schema.
#### Purpose of the Folders and Files:
    - Config Folder: (mysqlconnection.py) connects the MySQL Schema to the Python application, allowing the Board class to make database queries using PyMySQL.
    - Controllers Folder: (boards.py) sets up the app routes of the web application, utilizing both display and action methods to display the solution of the sudoku
        - Display Methods:
             - Index Route: (index.html) sets up the page the user begins on, allowing them to press a button to move onto the sudoku
             - Sudoku Route: (sudoku.html) runs the .get_board() function from the Board class to display the starter sudoku board
             - Solution Route: (solution.html) runs the .solve_board() function from the Board class to display the solution to the sudoku board (This is solved by the backtracking algorithm)
        - Action Methods:
             - Board/Solve Route: (Future Development) Shows how the board is solved step-by-step by sending each step of solving the sudoku through a 3D array
             - Board/New Route: (Future Development) Creates a new board for the user by shuffling the numbers of the initial board
    - Models Folder (board.py) supplies the methods used in the controllers file to display and solve the sudoku
        - Class Board Attributes:
            - ID: (self.id [primary key]) gives each board a special ID for easier access
            - Board: (self.board) stores the actual board as a string of 81 characters
            - Created At: (self.created_at) keeps track of when each board was created
            - Updated At: (self.updated_at) keeps track of when each board was updated
        - Class Board Methods:
            - Get Board: (get_board) catches the board using the SQL query ("SELECT board from boards") and converts the string of 81 numerical characters into a 2D array representing the sudoku board
            - Solve Board: (solve_board) solves the board using a backtracking algorithm using 3 mini-methods
                - Find Empty: (find_empty) finds if there are any unsolved spaces on a given sudou board, returning the open space if True or None if False
                - Validate: (validate) finds if the given 2D array has not violated any sudoku rules (1-9 in a row, 1-9 in a column, 1-9 in the box), returning True or False
                - Solve (solve) solves the board by putting values in the open spaces found by the find_empty method and checking them using the validate method, returning True if the sudoku is solved or False otherwise
    - Static Folder: stores files not neccesary for deployment
        - SQL Schema (erd.mwb) stores the sudoku boards and sends them to the Board class when get_board is called
        - Backtracking Algorithm (sudoku.py) contains the backtracking algorithm in a non-class format
    - Templates Folder: stores the front-end .html files for our Flask application
        - Index.html: Welcomes the user to the web application and creates a button to move onto the sudoku board
        - Sudoku.html: Displays the sudoku board using the Board class (get_board method) and creates a button to show the solution
        - Solution.html: Displays the solution to the sudoku board using the Board class (solve_board method) and creates a button to go back to the unsolved board
    - Dunderinit File: (__init__.py) runs the Flask app and initializes the secret_key needed
    - Server File: (server.py) imports the Flask application and runs the server when called by the terminal
    - Pipfile/Pipfile.lock: creates our virtual environment and allows me to run the application in a development server